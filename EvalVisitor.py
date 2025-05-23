
from parser.analizadorVisitor import analizadorVisitor
class EvalVisitor(analizadorVisitor):
    def __init__(self):
        self.scopes = [{}]  # Variables globales o locales
        self.funciones = {}  # Funciones definidas
        self.hayErrores = False
        self.retorno = None



    def visitPrograma(self, ctx):
        for child in ctx.getChildren():
            if self.hayErrores:
                print("⛔ Ejecución detenida por errores.")
                break
            self.visit(child)

    def visitDeclaracion(self, ctx):
        tipo = ctx.tipo().getText()
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion()) if ctx.expresion() else None

        if valor is not None and not self._verificar_tipo(tipo, valor):
            print(f"❌ Error de tipo: No se puede asignar '{valor}' al tipo '{tipo}'")
            self.hayErrores = True
            return

        self._insertar_variable(nombre, tipo, valor)
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self._asignar_variable(nombre, valor)
        return valor
       
    def visitSuma(self, ctx):
        nombre = ctx.ID().getText()
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        resultado = left + right

        var = self._buscar_variable(nombre)
        if var is None:
            return

        tipo = var['tipo']
        if not self._verificar_tipo(tipo, resultado):
            print(f"❌ Error: Resultado incompatible con el tipo de '{nombre}'")
            self.hayErrores = True
            return

        self._asignar_variable(nombre, resultado)
        return resultado


    def visitIfElse(self, ctx):
        condicion = self.visit(ctx.expresion())
        #print(f"🧪 Condición del if: {condicion} (tipo: {type(condicion)})") pruebas
        if isinstance(condicion, bool) and condicion is True:
            self.visit(ctx.bloque(0))
        elif ctx.bloque(1):
            self.visit(ctx.bloque(1))


    def visitWhileLoop(self, ctx):
        while True:
            condicion = self.visit(ctx.expresion())
            if not condicion:
                break
            self.visit(ctx.bloque())

    def visitForLoop(self, ctx):
        self.visit(ctx.asignacion(0))
        while True:
            condicion = self.visit(ctx.expresion())
            if not condicion:
                break
            self.visit(ctx.bloque())
            self.visit(ctx.asignacion(1))

    def visitAccion(self, ctx):
        partes = []
        for child in ctx.children:
            if child.getText() in ["mostrar", "(", ")", ","]:
                continue
            valor = self.visit(child)
    
            if valor is not None:                
                partes.append(str(valor))
            else:
                if hasattr(child, 'getText'):
                    raw = child.getText()
                    if raw.startswith('"') and raw.endswith('"'):
                        raw = raw[1:-1]
                partes.append(raw)
        #print(f"🧾 Acción: {partes}") debug
        #print("🖨️ Mostrando:", " ".join(partes))  pruebas
        print(" ".join(partes))

    def visitReturnStmt(self, ctx):
        self.retorno = self.visit(ctx.expresion())

    def visitFuncionDecl(self, ctx):
        tipo = ctx.tipo().getText()
        nombre = ctx.ID().getText()
        if nombre in self.funciones:
            print(f"❌ Error: Función '{nombre}' ya fue declarada.")
            self.hayErrores = True
            return


        parametros = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                tipo_param = p.tipo().getText()
                id_param = p.ID().getText()
                parametros.append((tipo_param, id_param))

        self.funciones[nombre] = {
            'tipo': tipo,
            'parametros': parametros,
            'ctx': ctx.bloque()
        }

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        if nombre not in self.funciones:
            print(f"❌ Error: Función '{nombre}' no está definida.")
            self.hayErrores = True
            return None

        funcion = self.funciones[nombre]
        parametros = funcion['parametros']
        cuerpo = funcion['ctx']
        tipo_retorno = funcion['tipo']

        argumentos = []
        if ctx.argumentos():
            argumentos = [self.visit(e) for e in ctx.argumentos().expresion()]

        if len(argumentos) != len(parametros):
            print(f"❌ Error: Número de argumentos incorrecto en llamada a '{nombre}'")
            self.hayErrores = True
            return None

        scope_anterior = self.scopes.copy()
        self.scopes.append({})

        for (tipo, id_param), valor in zip(parametros, argumentos):
            if not self._verificar_tipo(tipo, valor):
                print(f"❌ Error: Argumento inválido para parámetro '{id_param}' de tipo '{tipo}'")
                self.hayErrores = True
                self.scopes = scope_anterior
                return None
            self._insertar_variable(id_param, tipo, valor) #pruebas
           
        # ⛑️ Manejo seguro de retorno
        prev_retorno = self.retorno
        self.retorno = None

        self.visit(cuerpo)
        resultado = self.retorno

        self.retorno = prev_retorno
        self.scopes = scope_anterior

        # Validar tipo de retorno
        if not self._verificar_tipo(tipo_retorno, resultado):
            print(f"❌ Error: Valor retornado incompatible en '{nombre}', se esperaba '{tipo_retorno}'")
            self.hayErrores = True
            return None

        return resultado


    def visitExpresion(self, ctx):
        if ctx.NUM():
            text = ctx.NUM().getText()
            return float(text) if '.' in text else int(text)
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
        elif ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())
        elif ctx.ID():
            nombre = ctx.ID().getText()
            var = self._buscar_variable(nombre)
            if var is not None:
                return var['valor']
            return None
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
                return self.visit(ctx.getChild(1))
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            if left is None or right is None:
                return None

            try:
                if op == '+': return left + right
                elif op == '-': return left - right
                elif op == '*': return left * right
                elif op == '/': return left / right if right != 0 else None
                elif op == '%': return left % right if right != 0 else None
                elif op == '<': return left < right
                elif op == '>': return left > right
                elif op == '<=': return left <= right
                elif op == '>=': return left >= right
                elif op == '==': return left == right
                elif op == '!=': return left != right
            except TypeError:
                print(f"❌ Error de tipo: no se puede operar '{left}' y '{right}' con '{op}'")
                self.hayErrores = True
                return None
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        print(f"❌ Error: Expresión inválida '{ctx.getText()}'")
        self.hayErrores = True
        return None

    def visitBloque(self, ctx):
        from antlr4.tree.Tree import TerminalNodeImpl  # asegúrate de tenerlo importado

        self.scopes.append({})
        for instr in ctx.getChildren():
            if isinstance(instr, TerminalNodeImpl):  # ← ignora ';' y otros tokens
                continue
            if self.retorno is not None:  # ← solo debería cortar si estamos en una función
                break
            self.visit(instr)
        self.scopes.pop()



    def _verificar_tipo(self, tipo, valor):
        if tipo == "int": return isinstance(valor, int)
        elif tipo == "float": return isinstance(valor, float)
        elif tipo == "bool": return isinstance(valor, bool)
        elif tipo == "string": return isinstance(valor, str)
        return False
    
    def _insertar_variable(self, nombre, tipo, valor):
        if nombre in self.scopes[-1]:
            print(f"❌ Error: Variable '{nombre}' ya fue declarada en este bloque.")
            self.hayErrores = True
            return
        self.scopes[-1][nombre] = {'tipo': tipo, 'valor': valor}
    
    def _buscar_variable(self, nombre):
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre]
        print(f"❌ Error: Variable '{nombre}' no declarada.")
        self.hayErrores = True
        return None

    def _valor_default(self, tipo):
        if tipo == "int": return 0
        if tipo == "float": return 0.0
        if tipo == "bool": return False
        if tipo == "string": return ""
        return None


    def _asignar_variable(self, nombre, valor):
        for scope in reversed(self.scopes):
            if nombre in scope:
                tipo = scope[nombre]['tipo']
                if not self._verificar_tipo(tipo, valor):
                    print(f"❌ Error de tipo: No se puede asignar '{valor}' a '{nombre}' de tipo '{tipo}'")
                    self.hayErrores = True
                    return
                scope[nombre]['valor'] = valor
                return
        print(f"❌ Error: Variable '{nombre}' no declarada.")        
        self.hayErrores = True

