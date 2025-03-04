from parser.analizadorVisitor import analizadorVisitor

class EvalVisitor(analizadorVisitor):

    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        for child in ctx.getChildren():
            self.visit(child)

    def visitCicloPara(self, ctx):
        self.visit(ctx.asignacion(0))  # Inicialización
    
        while True:
            resultado_condicion = self.visit(ctx.condicion())
    
            if resultado_condicion is None:
                print("\u274c Error: Condición inválida en el ciclo para.")
                return
    
            if not resultado_condicion:
                break
            
            self.visit(ctx.bloque())
            self.visit(ctx.asignacion(1))  # Incremento

    def visitCicloMientras(self, ctx):
        while True:
            resultado_condicion = self.visit(ctx.condicion())
            if resultado_condicion is None:
                print("\u274c Error: Condición inválida en el ciclo mientras.")
                return
            if not resultado_condicion:
                break
            self.visit(ctx.bloque())

    def visitCondicional(self, ctx):
        resultado_condicion = self.visit(ctx.condicion())
        if resultado_condicion is None:
            print("\u274c Error: Condición inválida en el condicional.")
            return
        if resultado_condicion:
            self.visit(ctx.bloque(0))
        elif ctx.bloque(1) is not None:
            self.visit(ctx.bloque(1))

    def visitAccion(self, ctx):
        partes = []
        for expr in ctx.getChildren():
            if expr.getText() in ["mostrar", "(", ")", ","]:
                continue  
            if expr.getText().startswith('"') and expr.getText().endswith('"'):
                partes.append(expr.getText()[1:-1])  
            else:
                valor = self.visit(expr)  
                if valor is not None:
                    partes.append(str(valor))
                else:
                    print(f"\u274c Error: No se pudo evaluar '{expr.getText()}'")
                    return
        print(" ".join(partes))
    
    def visitAsignacion(self, ctx):
        nombre_variable = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        if valor is None:
            print(f"\u274c Error: No se pudo asignar valor a '{nombre_variable}'")
            return
        self.variables[nombre_variable] = valor
        return valor

    def visitOperacion(self, ctx):
        nombre_variable = ctx.ID().getText()
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        if izquierda is None or derecha is None:
            print(f"\u274c Error: Operación inválida en la variable '{nombre_variable}'")
            return
        self.variables[nombre_variable] = izquierda + derecha
        return izquierda + derecha

    def visitExpresion(self, ctx):
        if ctx.NUMERO():
            valor = ctx.NUMERO().getText()
            return int(valor) if '.' not in valor else float(valor)
        elif ctx.ID():
            nombre_variable = ctx.ID().getText()
            if nombre_variable not in self.variables:
                print(f"\u274c Error: Variable '{nombre_variable}' no definida.")
                return None
            return self.variables[nombre_variable]
        elif ctx.getChildCount() == 3:
            izquierda = self.visit(ctx.getChild(0))
            operador = ctx.getChild(1).getText()
            derecha = self.visit(ctx.getChild(2))
            if izquierda is None or derecha is None:
                print(f"\u274c Error: Expresión inválida '{ctx.getText()}'")
                return None
            return {
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y if y != 0 else None,
                '%': lambda x, y: x % y if y != 0 else None,
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y
            }.get(operador, lambda x, y: None)(izquierda, derecha)
        return None
    
    def visitCondicion(self, ctx):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        operador = ctx.getChild(1).getText()
        if izquierda is None or derecha is None:
            print(f"\u274c Error: Condición inválida '{ctx.getText()}'")
            return None
        return {
            '<': lambda x, y: x < y,
            '>': lambda x, y: x > y,
            '<=': lambda x, y: x <= y,
            '>=': lambda x, y: x >= y,
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y
        }.get(operador, lambda x, y: None)(izquierda, derecha)
    
    def visitBloque(self, ctx):
        for instruccion in ctx.getChildren():
            self.visit(instruccion)
