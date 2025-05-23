import subprocess
import time
import os
from test import analizar_codigo, leer_archivo


def ejecutar_comando(cmd):
    try:
        subprocess.run(cmd, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar: {cmd}\n{e}")

def medir_tiempo(etiqueta, funcion, *args):
    print(f"🔄 {etiqueta}...")
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()
    print(f"✅ {etiqueta} completado en {fin - inicio:.2f} segundos.\n")
    return resultado

def compilar_ll_a_obj(ll_file="codigo.ll", obj_file="codigo.o"):
    cmd = f"llc -march=x86-64 -filetype=obj -mtriple=x86_64-w64-windows-gnu {ll_file} -o {obj_file}"
    ejecutar_comando(cmd)

def enlazar_obj_a_bin(obj_file="codigo.o", exe_file="codigo.exe"):
    cmd = f"x86_64-w64-mingw32-gcc {obj_file} -o {exe_file}"
    ejecutar_comando(cmd)
def optimizar_ll(input_ll="codigo.ll", output_ll="codigoOpt.ll"):
    ejecutar_comando(f"opt -O2 {input_ll} -o {output_ll} -S")


def mostrar_menu():
    while True:
        print("=== Menú del Compilador ===")
        print("1. Ejecutar flujo completo + optimización")
        print("2. Ejecutar flujo completo sin optimización")
        print("3. Solo generar código intermedio (.ll)")
        print("4. Compilar desde un .ll manualmente optimizado")
        print("5. Convertir binario a .exe")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            archivo_codigo = "codigo.txt"
            codigo = leer_archivo(archivo_codigo)
            medir_tiempo("Análisis y generación de IR", analizar_codigo, codigo, archivo_codigo)

            base = os.path.splitext(archivo_codigo)[0]
            medir_tiempo("Optimización IR", optimizar_ll, f"{base}.ll", f"{base}Opt.ll")
            medir_tiempo("Compilación a objeto", compilar_ll_a_obj, f"{base}Opt.ll", f"{base}.o")
            medir_tiempo("Enlace a ejecutable", enlazar_obj_a_bin, f"{base}.o", f"{base}.exe")
        elif opcion == "2":
            archivo_codigo = "codigo.txt"
            codigo = leer_archivo(archivo_codigo)
            medir_tiempo("Análisis y generación de IR", analizar_codigo, codigo, archivo_codigo)

            base = os.path.splitext(archivo_codigo)[0]
            medir_tiempo("Compilación a objeto", compilar_ll_a_obj, f"{base}.ll", f"{base}.o")
            medir_tiempo("Enlace a ejecutable", enlazar_obj_a_bin, f"{base}.o", f"{base}.exe")
        elif opcion == "3":
            archivo_codigo = "codigo.txt"
            codigo = leer_archivo(archivo_codigo)
            medir_tiempo("Generación de código intermedio", analizar_codigo, codigo, archivo_codigo)
        elif opcion == "4":
            archivo = input("Nombre del archivo .ll optimizado: ")
            medir_tiempo("Compilación a objeto", compilar_ll_a_obj, archivo)
            medir_tiempo("Enlace a ejecutable", enlazar_obj_a_bin)
        elif opcion == "5":
            obj_file = input("Archivo objeto (.o) a convertir: ")
            exe_file = input("Nombre de salida .exe: ")
            medir_tiempo("Conversión a .exe", enlazar_obj_a_bin, obj_file, exe_file)
        elif opcion == "6":
            print("👋 Saliendo del compilador.")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.\n")

if __name__ == "__main__":
    mostrar_menu()
