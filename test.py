from antlr4 import *
from parser.analizadorLexer import analizadorLexer
from parser.analizadorParser import analizadorParser
from EvalVisitor import EvalVisitor
from ValidaErrorListener import ValidaErrorListener
from SemanticoListener import SemanticoListener 

def leer_archivo(nombre_archivo):
    """Lee el contenido de un archivo y lo devuelve como una cadena."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'.")
        return None

def analizar_codigo(codigo):
    """Analiza el código fuente usando el analizador léxico y sintáctico."""
    if codigo is None:
        print("❌ Error: No hay código para analizar.")
        return

    input_stream = InputStream(codigo)
    lexer = analizadorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = analizadorParser(token_stream)
    listener = ValidaErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(listener)
    tree = parser.programa()

    
    semantic_listener = SemanticoListener()    
    walker = ParseTreeWalker()
    walker.walk(semantic_listener, tree)

    if semantic_listener.hayErrores:
        semantic_listener.mostrarErrores()
        print("⛔ Se detuvo la ejecución por errores semánticos.")
        return
    
    if listener.hayErrores:
          print("⛔ Se detuvo la ejecución por errores de sintaxis.")
          return
    visitor = EvalVisitor()
    visitor.visit(tree)

    # print("\nResultado de las variables:")
    # for var_name, value in visitor.variables.items():
    #     print(f"{var_name} = {value}")
    
if __name__ == "__main__":
    archivo_codigo = "cod2.txt" 
    #print(f"Leyendo código desde '{archivo_codigo}'...\n")
    
    codigo = leer_archivo(archivo_codigo)
    
    #print("Ejecutando código...\n")
    analizar_codigo(codigo)
