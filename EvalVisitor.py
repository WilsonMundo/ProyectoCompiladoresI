from parser.analizadorVisitor import analizadorVisitor

class EvalVisitor(analizadorVisitor):

    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        """Valida y ejecuta todas las instrucciones del programa."""
        for child in ctx.getChildren():
            self.visit(child)

    def visitForLoop(self, ctx):
        """Ejecuta un ciclo for con validaciones."""
        self.visit(ctx.asignacion(0))  # Inicialización
    
        while True:
            resultado_condicion = self.visit(ctx.condicion())
    
            if resultado_condicion is None:
                print("❌ Error: Condición inválida en el for.")
                return
    
            if not resultado_condicion:
                break
            
            self.visit(ctx.bloque())
            self.visit(ctx.asignacion(1))  # Incremento


    def visitWhileLoop(self, ctx):
        """Ejecuta un ciclo while con validaciones."""
        while True:
            resultado_condicion = self.visit(ctx.condicion())

            if resultado_condicion is None:
                print("❌ Error: Condición inválida en el while.")
                return

            if not resultado_condicion:
                break

            self.visit(ctx.bloque())


    def visitIfElse(self, ctx):
        """Ejecuta y valida un if-else."""
        resultado_condicion = self.visit(ctx.condicion())

        if resultado_condicion is None:
            print("❌ Error: Condición inválida en el if.")
            return

        if resultado_condicion:  
            self.visit(ctx.bloque(0))
        elif ctx.bloque(1) is not None:  
            self.visit(ctx.bloque(1))


    def visitAccion(self, ctx):
        """Ejecuta mostrar() con soporte para múltiples valores en una sola línea."""
        partes = []
    
        for child in ctx.getChildren():
            text = child.getText()
    
            if text in ["mostrar", "(", ")", ","]:
                continue  # Ignoramos tokens PRINT, paréntesis y comas
            
            if text.startswith('"') and text.endswith('"'):  # Si es una cadena (STRING)
                partes.append(text[1:-1])  # Quitamos comillas
            
            elif text.isnumeric():  # Si es un número
                partes.append(text)
            
            elif text.isidentifier():  # Si es una variable (ID)
                if text in self.variables:
                    partes.append(str(self.variables[text]))  # Convertimos a string el valor
                else:
                    print(f"❌ Error: Variable '{text}' no definida.")
                    return
            
            else:  # Si es una expresión, la evaluamos
                partes.append(str(self.visit(child)))
    
        print(" ".join(partes))  # ✅ Imprimimos todo junto en una línea
    
    def visitAsignacion(self, ctx):
        """Valida y ejecuta asignaciones."""
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())

        if value is None:
            print(f"❌ Error: No se pudo asignar valor a '{var_name}'")
            return

        self.variables[var_name] = value
        return value

    def visitSuma(self, ctx):
        """Valida y ejecuta sumas."""
        var_name = ctx.ID().getText()
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))

        if left is None or right is None:
            print(f"❌ Error: Suma inválida en la variable '{var_name}'")
            return

        self.variables[var_name] = left + right
        return left + right

    def visitExpresion(self, ctx):
        """Evalúa expresiones numéricas respetando la prioridad de operadores correctamente."""
        if ctx.NUM():
            return float(ctx.NUM().getText())

        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.variables:
                print(f"❌ Error: Variable '{var_name}' no definida.")
                return None
            return self.variables[var_name]

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            return self.visit(ctx.getChild(1))  #  Evalúa contenido dentro de paréntesis

        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))  # Evaluamos el operando izquierdo
            op = ctx.getChild(1).getText()  # Obtenemos el operador
            right = self.visit(ctx.getChild(2))  # Evaluamos el operando derecho

            if left is None or right is None:
                print(f"❌ Error: Expresión inválida '{ctx.getText()}'")
                return None

            #print(f"🧐 Evaluando: {left} {op} {right}")  # 👀 Depuración

            # Evaluación según prioridad de operadores
            if op == '*':
                return left * right
            elif op == '/':
                if right == 0:
                    print("⚠️ Advertencia: División por cero")
                    return None
                return left / right
            elif op == '%':  
                if right == 0:
                    print("⚠️ Advertencia: Módulo por cero")
                    return None
                return left % right
            elif op == '+':
                return left + right
            elif op == '-':
                return left - right

        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))  # Si es un solo valor, devuélvelo directamente

        print(f"❌ Error: Expresión inválida '{ctx.getText()}'")
        return None




    def visitCondicion(self, ctx):
       """Evalúa condiciones y devuelve un booleano."""
       left = self.visit(ctx.expresion(0))
       right = self.visit(ctx.expresion(1))
       operador = ctx.getChild(1).getText()

       if left is None or right is None:
           print(f"❌ Error: Condición inválida '{ctx.getText()}'")
           return None

       if operador == '<':
           return left < right
       elif operador == '>':
           return left > right
       elif operador == '<=':
           return left <= right
       elif operador == '>=':
           return left >= right
       elif operador == '==':
           return left == right
       elif operador == '!=':
           return left != right

       print(f"❌ Error: Operador desconocido en condición '{ctx.getText()}'")
       return None


    def visitBloque(self, ctx):
        """Ejecuta instrucciones dentro del bloque."""
        for instr in ctx.getChildren():
            self.visit(instr)
