from llvmlite import ir
import llvmlite.binding as llvm
from parser.analizadorVisitor import analizadorVisitor

class IRVisitor(analizadorVisitor):
    def __init__(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        self.module = ir.Module(name="main")
        self.module.triple = llvm.get_default_triple()
        self.target_machine = llvm.Target.from_default_triple().create_target_machine()
        self.module.data_layout = self.target_machine.target_data

        self.printf = ir.Function(
            self.module,
            ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True),
            name="printf"
        )
        self.sprintf = ir.Function(
            self.module,
            ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))] * 2, var_arg=True),
            name="sprintf"
        )
        self.funciones = {}
        self.builder = None
        self.variables = {}

    def visitPrograma(self, ctx):
        func_type = ir.FunctionType(ir.IntType(32), [])
        main_func = ir.Function(self.module, func_type, name="main")
        block = main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        for child in ctx.getChildren():
            self.visit(child)

        self.builder.ret(ir.Constant(ir.IntType(32), 0))

    def visitDeclaracion(self, ctx):
        #pruebas para validar datos
        #print(f"➡️ Declarando {ctx.ID().getText()}") 
        tipo = ctx.tipo().getText()
        nombre = ctx.ID().getText()
        ir_tipo = self._get_ir_type(tipo)
        ptr = self.builder.alloca(ir_tipo, name=nombre)
        self.variables[nombre] = ptr

        if ctx.expresion():
            valor = self.visit(ctx.expresion())
            if valor is None:
                print(f"❌ Error: Valor inválido al declarar '{nombre}'")
                return  # <-- previene el crash
            if valor and valor.type != ptr.type.pointee:
                valor = self._convert_type(valor, ptr.type.pointee)
            self.builder.store(valor, ptr)

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        ptr = self.variables.get(nombre)
        if ptr:
            self.builder.store(valor, ptr)

    def visitSuma(self, ctx):
        nombre = ctx.ID().getText()
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        result = self._emit_op('+', left, right)
        ptr = self.variables.get(nombre)
        if not ptr:
            ptr = self.builder.alloca(result.type, name=nombre)
            self.variables[nombre] = ptr
        self.builder.store(result, ptr)

    def visitReturnStmt(self, ctx):
        valor = self.visit(ctx.expresion())
        if valor:
                self.builder.ret(valor)

    def visitExpresion(self, ctx):
        if ctx.NUM():
            num = ctx.NUM().getText()
            return ir.Constant(ir.DoubleType() if '.' in num else ir.IntType(32), float(num) if '.' in num else int(num))
        
        elif ctx.STRING():
            raw = ctx.STRING().getText()[1:-1]
            return self._str(raw)

        elif ctx.TRUE():
            return ir.Constant(ir.IntType(1), 1)

        elif ctx.FALSE():
            return ir.Constant(ir.IntType(1), 0)

        elif ctx.ID():
            nombre = ctx.ID().getText()
            if nombre not in self.variables:
                print(f"❌ Error: Variable '{nombre}' no declarada en IRVisitor.")
                return None
            return self.builder.load(self.variables[nombre])

        elif ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())

        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
                # Caso: (expresion)
                return self.visit(ctx.getChild(1))

            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            # Traza útil para entender la operación ///comentado solo pruebas
            #left_repr = str(left) if left else "None"
            #right_repr = str(right) if right else "None"
            #print(f"➡️ Operación: {ctx.getText()} → {left_repr} {op} {right_repr}")

            if left is None or right is None:
                print(f"❌ Error en operación '{ctx.getText()}': operandos nulos.")
                return None

            try:
                return self._emit_op(op, left, right)
            except Exception as e:
                print(f"❌ Excepción en _emit_op para '{ctx.getText()}': {e}")
                return None

        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        return None


    def visitAccion(self, ctx):
        args = []
        format_parts = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getText() in ["mostrar", "(", ")", ","]:
                continue

            val = self.visit(child)
            if not val:
                continue

            if isinstance(val.type, ir.PointerType):  # string
                format_parts.append("%s")
            elif isinstance(val.type, ir.DoubleType):
                format_parts.append("%f")
            elif isinstance(val.type, ir.IntType):
                format_parts.append("%d")
            else:
                print(f"⚠️ Tipo no soportado: {val.type}")
                continue

            args.append(val)

        if args:
            fmt_str = " ".join(format_parts)
            fmt = self._strfmt(fmt_str)
            self.builder.call(self.printf, [fmt] + args)




    def visitIfElse(self, ctx):
        cond = self.visit(ctx.expresion())
        func = self.builder.function

        then_bb = func.append_basic_block("then")
        else_bb = func.append_basic_block("else") if ctx.bloque(1) else None
        merge_bb = func.append_basic_block("merge")

        if else_bb:
            self.builder.cbranch(cond, then_bb, else_bb)
        else:
            self.builder.cbranch(cond, then_bb, merge_bb)

        self.builder.position_at_start(then_bb)
        self.visit(ctx.bloque(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(merge_bb)

        if else_bb:
            self.builder.position_at_start(else_bb)
            self.visit(ctx.bloque(1))
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_bb)

        self.builder.position_at_start(merge_bb)

    def visitWhileLoop(self, ctx):
        func = self.builder.function
        cond_bb = func.append_basic_block("while.cond")
        body_bb = func.append_basic_block("while.body")
        exit_bb = func.append_basic_block("while.exit")

        self.builder.branch(cond_bb)
        self.builder.position_at_start(cond_bb)
        cond = self.visit(ctx.expresion())
        self.builder.cbranch(cond, body_bb, exit_bb)

        self.builder.position_at_start(body_bb)
        self.visit(ctx.bloque())
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_bb)

        self.builder.position_at_start(exit_bb)

    def visitForLoop(self, ctx):
        self.visit(ctx.asignacion(0))

        func = self.builder.function
        cond_bb = func.append_basic_block("for.cond")
        body_bb = func.append_basic_block("for.body")
        step_bb = func.append_basic_block("for.step")
        exit_bb = func.append_basic_block("for.exit")

        self.builder.branch(cond_bb)
        self.builder.position_at_start(cond_bb)
        cond = self.visit(ctx.expresion())
        self.builder.cbranch(cond, body_bb, exit_bb)

        self.builder.position_at_start(body_bb)
        self.visit(ctx.bloque())
        if not self.builder.block.is_terminated:
            self.builder.branch(step_bb)

        self.builder.position_at_start(step_bb)
        self.visit(ctx.asignacion(1))
        self.builder.branch(cond_bb)

        self.builder.position_at_start(exit_bb)

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        funcion = self.funciones.get(nombre)
        if not funcion:
            print(f"❌ Error: Función '{nombre}' no encontrada.")
            return None

        argumentos = []
        if ctx.argumentos():
            for expr in ctx.argumentos().expresion():
                val = self.visit(expr)
                if val is None:
                    print(f"❌ Error: Argumento en llamada a '{nombre}' no evaluado.")
                    return None
                argumentos.append(val)

        return self.builder.call(funcion, argumentos)
    
    
    def visitFuncionDecl(self, ctx):
        nombre = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()
        ret_type = self._get_ir_type(tipo_retorno)

        # Obtener tipos y nombres de parámetros
        param_types = []
        param_names = []
        if ctx.parametros():
            for param in ctx.parametros().parametro():
                t = self._get_ir_type(param.tipo().getText())
                param_types.append(t)
                param_names.append(param.ID().getText())

        # Crear la función en LLVM
        func_type = ir.FunctionType(ret_type, param_types)
        funcion = ir.Function(self.module, func_type, name=nombre)
        self.funciones[nombre] = funcion

        # Crear bloque de entrada
        block = funcion.append_basic_block("entry")
        builder = ir.IRBuilder(block)

        # Guardar el builder anterior y scope de variables
        old_builder = self.builder
        old_vars = self.variables

        self.builder = builder
        self.variables = {}

        # Registrar y alocar parámetros
        for i, arg in enumerate(funcion.args):
            arg.name = param_names[i]
            ptr = builder.alloca(arg.type, name=arg.name)
            builder.store(arg, ptr)
            self.variables[arg.name] = ptr  # ✅ Registrar variable en el nuevo scope

        # Visitar el cuerpo de la función
        self.visit(ctx.bloque())

        # Retorno por defecto si no hay return explícito
        if not builder.block.is_terminated:
            if isinstance(ret_type, ir.IntType):
                builder.ret(ir.Constant(ret_type, 0))
            elif isinstance(ret_type, ir.DoubleType):
                builder.ret(ir.Constant(ret_type, 0.0))
            elif isinstance(ret_type, ir.IntType) and ret_type.width == 1:  # bool
                builder.ret(ir.Constant(ret_type, 0))
            else:
                builder.ret(ir.Constant(ret_type, None))

        # Restaurar estado
        self.builder = old_builder
        self.variables = old_vars

    def visitBloque(self, ctx):
        for instruccion in ctx.instruccion():
            self.visit(instruccion)

    def _get_ir_type(self, tipo):
        if tipo == "int": return ir.IntType(32)
        if tipo == "float": return ir.DoubleType()
        if tipo == "bool": return ir.IntType(1)
        if tipo == "string": return ir.PointerType(ir.IntType(8))

    def _str(self, text: str):
        """Literal normal: sólo añade terminador nulo."""
        if not text.endswith("\0"):
            text += "\0"
        encoded = bytearray(text.encode("utf8"))
        const = ir.Constant(ir.ArrayType(ir.IntType(8), len(encoded)), encoded)
        var   = ir.GlobalVariable(self.module, const.type,
                                name=f".str{len(self.module.globals)}")
        var.linkage         = "internal"
        var.global_constant = True
        var.initializer     = const
        return self.builder.bitcast(var, ir.PointerType(ir.IntType(8)))

    def _strfmt(self, fmt: str):
        """Cadenas **de formato** para printf: añade '\n' y luego terminador."""
        if not fmt.endswith("\n"):
            fmt += "\n"
        return self._str(fmt)        # _str ya agrega el '\0'




    def _concat_strings(self, left, right):
        # Crea una variable global para almacenar el resultado (128 bytes)
        buffer_type = ir.ArrayType(ir.IntType(8), 128)
        name = f"concat_str{len(self.module.globals)}"
        global_buffer = ir.GlobalVariable(self.module, buffer_type, name=name)
        global_buffer.linkage = "internal"
        global_buffer.global_constant = False
        global_buffer.initializer = ir.Constant(buffer_type, bytearray(128))

        # Obtener puntero a la cadena global
        buffer_ptr = self.builder.bitcast(global_buffer, ir.PointerType(ir.IntType(8)))

        # Formato "%s%s"
        fmt = self._strfmt("%s%s")

        # sprintf(buffer_ptr, "%s%s", left, right)
        self.builder.call(self.sprintf, [buffer_ptr, fmt, left, right])

        return buffer_ptr

    
    def _emit_op(self, op, left, right):
        # Concatenación de strings (ambos punteros i8*)
        if op == '+' and isinstance(left.type, ir.PointerType) and isinstance(right.type, ir.PointerType):
            return self._concat_strings(left, right)

        # ❌ Prohibir otras operaciones con strings
        if isinstance(left.type, ir.PointerType) or isinstance(right.type, ir.PointerType):
            print(f"❌ Error: Operación '{op}' no permitida sobre strings.")
            return None

        # Promoción automática entre int y float
        if left.type != right.type:
            if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.DoubleType):
                left = self.builder.sitofp(left, ir.DoubleType())
            elif isinstance(left.type, ir.DoubleType) and isinstance(right.type, ir.IntType):
                right = self.builder.sitofp(right, ir.DoubleType())
            else:
                print(f"❌ Error: Tipos incompatibles en operación '{op}': {left.type} vs {right.type}")
                return None

        if op == '+':
            return self.builder.fadd(left, right) if left.type == ir.DoubleType() else self.builder.add(left, right)
        elif op == '-':
            return self.builder.fsub(left, right) if left.type == ir.DoubleType() else self.builder.sub(left, right)
        elif op == '*':
            return self.builder.fmul(left, right) if left.type == ir.DoubleType() else self.builder.mul(left, right)
        elif op == '/':
            return self.builder.fdiv(left, right) if left.type == ir.DoubleType() else self.builder.sdiv(left, right)
        elif op == '%':
            return self.builder.frem(left, right) if left.type == ir.DoubleType() else self.builder.srem(left, right)
        elif op in ('<', '>', '<=', '>=', '==', '!='):
            if isinstance(left.type, ir.IntType):
                return self.builder.icmp_signed(op, left, right)
            elif isinstance(left.type, ir.DoubleType):
                return self.builder.fcmp_ordered(op, left, right)
            else:
                print(f"❌ Error: Comparación no soportada para tipo {left.type}")
                return None

        print(f"❌ Operador '{op}' no soportado.")
        return None

    def _convert_type(self, valor, tipo_destino):
        if valor.type == tipo_destino:
            return valor
        elif valor.type == ir.IntType(32) and tipo_destino == ir.DoubleType():
            return self.builder.sitofp(valor, ir.DoubleType())
        return valor
