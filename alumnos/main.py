from alumnos import registrar_alumno, listar_alumnos, buscar_alumno, modificar_alumno, eliminar_alumno 
from estadisticas import cantidad_alumnos, promedio_notas, nota_mayor, evaluacion_alumnos
from archivos import guardar_archivo, leer_archivo
def imprimir_menu(alumnos):
    salir = False
    while not salir:
        opcion = input("======= GESTIÓN DE ALUMNOS =======\n" \
        "1. Registrar alumno\n" \
        "2. Listar alumnos\n" \
        "3. Buscar alumno\n" \
        "4. Modificar alumno\n" \
        "5. Eliminar alumno\n" \
        "6. Ver estadisticas\n" \
        "7. Salir\n" \
        "\n" \
        "Seleccione una opcion: ")

        salir = ejecutar_menu(opcion, alumnos)

def ejecutar_menu(opcion, alumnos):
    match(opcion):
        case "1":
            registrar_alumno(alumnos)
            guardar_archivo(alumnos)
        case "2":
            listar_alumnos(alumnos)
        case "3":
            buscar_alumno(alumnos)
        case "4":
            modificar_alumno(alumnos)
            guardar_archivo(alumnos)
        case "5":
            eliminar_alumno(alumnos)
            guardar_archivo(alumnos)
        case "6":
            if len(alumnos) > 0:
                cantidad_alumnos(alumnos)
                promedio_notas(alumnos)
                nota_mayor(alumnos)
                evaluacion_alumnos(alumnos)
            else:
                print("No hay alumnos cargados.")
                return False
        case "7":
            
            return True
        case _:
            print("Opcion invalida. Ingresar nuevamente")
            return False

def main():
    alumnos = leer_archivo()

    imprimir_menu(alumnos)

    
    
if __name__ == "__main__":
    main()
