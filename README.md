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

✅ Uso del Analizador

Ejecuta el comando

python3 test.py 
Ejecuta el codigo dentro del archivo codigo.txt

existe archivos de ejemplo de codigo con para pruebas extencion .txt

📂 Estructura del Proyecto

ProyectoCompiladoresI/
│── parser/                 # Archivos generados por ANTLR (incluidos en el repo)
│── analizador.g4           # Archivo de gramática
│── test.py                 # Archivo principal para ejecutar el analizador
│── EvalVisitor.py          # Validaciones y lecturas del archivo Eval  estructura del lenguaje
│── README.md               # Documentación del proyecto


