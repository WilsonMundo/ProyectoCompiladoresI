import subprocess
import time
import os
from test import analizar_codigo, leer_archivo

# --------------------------------------------------------------------
# Utilidades de sistema
# --------------------------------------------------------------------

def ejecutar_comando(cmd: str):
    """Lanza un comando de shell y reporta error si devuelve código ≠ 0."""
    try:
        subprocess.run(cmd, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar: {cmd}\n{e}")

def medir_tiempo(etiqueta: str, funcion, *args):
    """Mide cuánto tarda 'funcion(*args)' y retorna su resultado."""
    print(f"🔄 {etiqueta}...")
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()
    print(f"✅ {etiqueta} completado en {fin - inicio:.2f} segundos.\n")
    return resultado

# --------------------------------------------------------------------
# Fases del back-end
# --------------------------------------------------------------------

def compilar_ll_a_obj(ll_file="codigo.ll", obj_file="codigo.o"):
    if not os.path.exists(ll_file):
        print(f"❌ No se encontró '{ll_file}'. Se omite compilación a objeto.")
        return False
    cmd = (
        f"llc -march=x86-64 -filetype=obj "
        f"-mtriple=x86_64-w64-windows-gnu {ll_file} -o {obj_file}"
    )
    ejecutar_comando(cmd)
    return True

def enlazar_obj_a_bin(obj_file="codigo.o", exe_file="codigo.exe"):
    if not os.path.exists(obj_file):
        print(f"❌ No se encontró '{obj_file}'. No se puede enlazar.")
        return
    cmd = f"x86_64-w64-mingw32-gcc {obj_file} -o {exe_file}"
    ejecutar_comando(cmd)

def optimizar_ll(input_ll="codigo.ll", output_ll="codigoOpt.ll"):
    if not os.path.exists(input_ll):
        print(f"❌ No se encontró '{input_ll}'. No se puede optimizar.")
        return False
    ejecutar_comando(f"opt -O2 {input_ll} -o {output_ll} -S")
    return True

# --------------------------------------------------------------------
# Menú interactivo
# --------------------------------------------------------------------

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

        # ---------------  Opción 1  ----------------------------------
        if opcion == "1":
            archivo_codigo = "codigo.txt"
            codigo = leer_archivo(archivo_codigo)

            ruta_ll = medir_tiempo(
                "Análisis y generación de IR",
                analizar_codigo, codigo, archivo_codigo
            )
            if ruta_ll is None:
                print("🚫 Proceso interrumpido por errores.\n")
                continue

            base = os.path.splitext(archivo_codigo)[0]
            ruta_opt = f"{base}Opt.ll"
            ok_opt = medir_tiempo(
                "Optimización IR",
                optimizar_ll, ruta_ll, ruta_opt
            )
            if not ok_opt:
                continue

            ok_obj = medir_tiempo(
                "Compilación a objeto",
                compilar_ll_a_obj, ruta_opt, f"{base}.o"
            )
            if not ok_obj:
                continue

            medir_tiempo(
                "Enlace a ejecutable",
                enlazar_obj_a_bin, f"{base}.o", f"{base}.exe"
            )

        # ---------------  Opción 2  ----------------------------------
        elif opcion == "2":
            archivo_codigo = "codigo.txt"
            codigo = leer_archivo(archivo_codigo)

            ruta_ll = medir_tiempo(
                "Análisis y generación de IR",
                analizar_codigo, codigo, archivo_codigo
            )
            if ruta_ll is None:
                print("🚫 Proceso interrumpido por errores.\n")
                continue

            base = os.path.splitext(archivo_codigo)[0]
            ok_obj = medir_tiempo(
                "Compilación a objeto",
                compilar_ll_a_obj, ruta_ll, f"{base}.o"
            )
            if not ok_obj:
                continue

            medir_tiempo(
                "Enlace a ejecutable",
                enlazar_obj_a_bin, f"{base}.o", f"{base}.exe"
            )

        # ---------------  Opción 3  ----------------------------------
        elif opcion == "3":
            archivo_codigo = "codigo.txt"
            codigo = leer_archivo(archivo_codigo)
            medir_tiempo(
                "Generación de código intermedio (.ll)",
                analizar_codigo, codigo, archivo_codigo
            )

        # ---------------  Opción 4  ----------------------------------
        elif opcion == "4":
            archivo = input("Nombre del archivo .ll optimizado: ")
            ok_obj = medir_tiempo("Compilación a objeto",
                                  compilar_ll_a_obj, archivo)
            if not ok_obj:
                continue
            medir_tiempo("Enlace a ejecutable", enlazar_obj_a_bin)

        # ---------------  Opción 5  ----------------------------------
        elif opcion == "5":
            obj_file = input("Archivo objeto (.o) a convertir: ")
            exe_file = input("Nombre de salida .exe: ")
            medir_tiempo("Conversión a .exe",
                          enlazar_obj_a_bin, obj_file, exe_file)

        # ---------------  Salir  -------------------------------------
        elif opcion == "6":
            print("👋 Saliendo del compilador.")
            break

        else:
            print("⚠️ Opción inválida. Intenta de nuevo.\n")

# --------------------------------------------------------------------
if __name__ == "__main__":
    mostrar_menu()
