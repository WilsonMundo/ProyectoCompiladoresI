from antlr4.error.ErrorListener import ErrorListener

class ValidaErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []            # almacena mensajes

    # ---------------------------------------------------------
    # se llama cada vez que el parser detecta un error léxico-sintáctico
    # ---------------------------------------------------------
    def syntaxError(
        self,
        recognizer,
        offendingSymbol,
        line,
        column,
        msg,
        e,
    ):
        mensaje = f"❌ Error de sintaxis en línea {line}:{column} → {msg}"
        self.errores.append(mensaje)

    # ------------- helpers que usa test.py -------------------
    @property
    def hayErrores(self):
        return bool(self.errores)

    def mostrarErrores(self):
        for m in self.errores:
            print(m)
