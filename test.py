from antlr4 import *
from parser.analizadorLexer   import analizadorLexer
from parser.analizadorParser  import analizadorParser
from EvalVisitor              import EvalVisitor
from ValidaErrorListener      import ValidaErrorListener
from SemanticoListener        import SemanticoListener
from IRVisitor                import IRVisitor
import os

# --------------------------------------------------------------------
# Utilidad I/O
# --------------------------------------------------------------------
def leer_archivo(nombre_archivo: str):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'.")
        return None

# --------------------------------------------------------------------
# Análisis + generación de IR
# --------------------------------------------------------------------
def analizar_codigo(codigo: str, nombre_archivo: str = "codigo.txt") -> str | None:
    """
    Analiza, valida y genera IR LLVM.
    Devuelve la ruta del .ll cuando todo es correcto;
    devuelve None si ocurre cualquier error (léxico, sintáctico o semántico).
    """
    if codigo is None:
        print("❌ Error: No hay código para analizar.")
        return None

    # ---- nombres de salida ----
    nombre_base = os.path.splitext(os.path.basename(nombre_archivo))[0]
    nombre_ll   = f"{nombre_base}.ll"

    # ---- fase léxica + sintáctica ----
    input_stream = InputStream(codigo)
    lexer        = analizadorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser       = analizadorParser(token_stream)

    sintax_listener = ValidaErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(sintax_listener)

    tree = parser.programa()

    # ---- fase semántica ----
    sem_listener = SemanticoListener()
    ParseTreeWalker().walk(sem_listener, tree)

    # ---- mostrar y abortar en caso de errores ----
    if sintax_listener.hayErrores:
        sintax_listener.mostrarErrores()
        print("⛔ Ejecución detenida por errores de sintaxis.\n")
        return None

    if sem_listener.hayErrores:
        sem_listener.mostrarErrores()
        print("⛔ Ejecución detenida por errores semánticos.\n")
        return None

    # ---- sin errores: interpretar (opcional) ----
    visitor = EvalVisitor()
    visitor.visit(tree)

    if visitor.hayErrores:               # ⬅️ NUEVO
        print("⛔ Ejecución detenida por errores de evaluación.\n")
        return None  
    
    # ---- generación de IR ----
    ir_gen = IRVisitor()
    ir_gen.visit(tree)

    with open(nombre_ll, "w", encoding="utf-8") as f:
        f.write(str(ir_gen.module))

    print(f"✅ IR generado en '{nombre_ll}'.")
    return nombre_ll
