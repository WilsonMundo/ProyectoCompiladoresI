📌 ProyectoCompiladoresI

Analizador léxico y sintáctico utilizando ANTLR y Python, capaz de validar la gramática de un lenguaje diseñado.

🚀 Instalación y Configuración

Antes de ejecutar el proyecto, asegurarse de tener Python 3.x y las dependencias necesarias 

Los archivos generados por ANTLR ya están incluidos en el repositorio dentro del directorio parser/, no es necesario correr el comando

si se  desea regenerarlos  (analizador.g4), usar el comando:

antlr4 -Dlanguage=Python3 -visitor -no-listener analizador.g4 -o parser

📚 Explicación del comando:

antlr4 → Ejecuta ANTLR.

-Dlanguage=Python3 → Especifica el lenguaje de salida.

-visitor → Genera clases de visitante (visitor pattern).

-no-listener → No genera clases de listener.

analizador.g4 → Archivo de gramática.

-o parser → Genera los archivos en la carpeta parser/.


## 🖥️ Generación de Código Intermedio (LLVM IR)
El proyecto ahora incluye la capacidad de **generar código intermedio en LLVM IR**. 

Se ha implementado un **visitor** en Python usando `llvmlite`, que toma el árbol sintáctico (AST) generado por ANTLR y lo traduce a **código intermedio LLVM IR**.

### 🚀 ¿Cómo funciona?

1. El código fuente es analizado utilizando ANTLR y el visitor `EvalVisitor`, que realiza las validaciones semánticas y de ejecución.
2. Luego, el código es procesado por un **nuevo visitor** que genera el código intermedio LLVM IR.
3. El código LLVM IR es generado y puede ser utilizado para optimizar o compilar más adelante a código máquina.



✅ Uso del Analizador

Los archivos generados por ANTLR ya están incluidos en el repositorio dentro del directorio parser/, no es necesario correr el comando

si se desea regenerarlos (analizador.g4), usar el comando:

antlr4 -Dlanguage=Python3 -visitor -listener analizador.g4 -o parser

Luego Ejecuta el comando

python3 test.py 
Ejecuta el codigo dentro del archivo codigo.txt 

existe archivos de ejemplo de codigo con para pruebas extencion .txt



📂 Estructura del Proyecto

ProyectoCompiladoresI/

│── parser/                  # Archivos generados por ANTLR (incluidos en el repo)

│── analizador.g4            # Archivo de gramática

│── test.py                  # Archivo principal para ejecutar el analizador

│── EvalVisitor.py           # Implementación de las validaciones y lecturas

│── IRVisitor.py             # Generación de código intermedio en LLVM IR

│── ValidaErrorListener.py   # Manejo de errores en el código fuente

│── SemanticoListener.py     # Análisis semántico avanzado (tipos, funciones, ámbito)

│── Pruebas.txt              # CodigoPruebas

│── CodigoPrubeas.txt        # CodigoPruebas

│── README.md                # Documentación del proyecto


