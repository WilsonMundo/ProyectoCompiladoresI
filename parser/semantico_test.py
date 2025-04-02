from antlr4 import *
from parser.analizadorLexer import analizadorLexer
from parser.analizadorParser import analizadorParser
from parser.analizadorListener import analizadorListener
from SemanticoListener import SemanticoListener

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {nombre_archivo}")
        return None

def analizar_semantica(codigo):
    input_stream = InputStream(codigo)
    lexer = analizadorLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = analizadorParser(tokens)
    tree = parser.programa()

    listener = SemanticoListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    if listener.hayErrores():
        listener.mostrarErrores()
        print("⛔ Ejecución detenida por errores semánticos.")
    else:
        print("✅ Análisis semántico exitoso. No se encontraron errores.")

if __name__ == "__main__":
    codigo = leer_archivo("codigo.txt")
    if codigo:
        analizar_semantica(codigo)
