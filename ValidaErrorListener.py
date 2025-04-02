from antlr4.error.ErrorListener import ErrorListener
class ValidaErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.hayErrores = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}:{column} → {msg}")
        self.hayErrores = True