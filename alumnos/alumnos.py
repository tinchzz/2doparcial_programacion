# 1. Cargar alumnos
# Crear una función que permita registrar alumnos. alumnos.py
# No se debe permitir:
# DNI duplicados. validaciones.py
# Edades negativas. validaciones.py
# Notas fuera del rango 0-10. validaciones.py
# Cada alumno posee: DNI, Nombre, Apellido, Edad, Nota final 
from validaciones import validar_dni, validar_edad, validar_nota
def pedir_dni(alumnos):
    validez = False

    while not validez:
        dni = input("DNI: ")
        if validar_dni(dni, alumnos) == True:
            validez = True
        else:
            print("DNI inválido o ya registrado. Ingresar nuevamente")
    return dni

def pedir_edad():
    validez = False

    while not validez:
        edad = input("Edad: ")
        if validar_edad(edad) == True:
            edad = int(edad)
            validez = True
        else:
            print("Edad no valida. Ingresar nuevamente")
    return edad

def pedir_nota():
    validez = False

    while not validez:
        nota = input("Nota final: ")
        if validar_nota(nota) == True:
            nota = float(nota)
            validez = True
        else:
            print("Nota no valida. Ingresar nuevamente")
    return nota

def registrar_alumno(alumnos):
    print("=== CARGAR NUEVO ALUMNO ===")
 
    dni = pedir_dni(alumnos)
    nombre = input("Nombre: ")
    apellido = input("Apellido: ") 
    edad = pedir_edad()
    nota = pedir_nota()

    alumnos[dni] = {"nombre": nombre, "apellido": apellido, "edad": edad, "nota": nota}

def listar_alumnos(alumnos):
    for dni, datos in alumnos.items():
        mostrar_alumno(dni,datos)

def mostrar_alumno(dni, datos):
    print(f"DNI: {dni}\n"
          f"Nombre: {datos["nombre"]}\n"
          f"Apellido: {datos["apellido"]}\n"
          f"Edad: {datos["edad"]}")
    if datos["nota"] == int(datos["nota"]):
        print(f"Nota final: {int(datos["nota"])}\n")
    else:
        print(f"Nota final: {datos["nota"]}\n")

def buscar_alumno(alumnos):
    dni_alumno = input("Ingresar DNI del alumno: ")
    if dni_alumno in alumnos:
        mostrar_alumno(dni_alumno,alumnos[dni_alumno])
    else:
        print("El DNI ingresado no está en el sistema.")

def modificar_alumno(alumnos):
    dni_alumno = input("Ingresar DNI del alumno: ")
    if dni_alumno in alumnos:
        mostrar_alumno(dni_alumno,alumnos[dni_alumno])
        opcion = input("¿Que queres modificar?\n" \
        "1. Nombre\n" \
        "2. Apellido\n" \
        "3. Edad\n" \
        "4. Nota\n"
        "0. Cancelar\n" \
        "\n" \
        "Seleccionar una opcion: ")
        match(opcion):
            case "1":
                nuevo_nombre = input("Ingresar nuevo nombre: ")
                alumnos[dni_alumno]["nombre"] = nuevo_nombre
            case "2":
                nuevo_apellido = input("Ingresar nuevo apellido: ")
                alumnos[dni_alumno]["apellido"] = nuevo_apellido
            case "3":
                nueva_edad = pedir_edad()
                alumnos[dni_alumno]["edad"] = nueva_edad
            case "4":
                nueva_nota = pedir_nota()
                alumnos[dni_alumno]["nota"] = nueva_nota
            case "0":
                return
            case _:
                print("Valor incorrecto. Ingresar nuevamente")
    else:
        print("El DNI ingresado no está en el sistema.")


def eliminar_alumno(alumnos):
    dni_alumno = input("Ingresar DNI del alumno: ")
    if dni_alumno in alumnos:
        validez = False
        while not validez:
            opcion = input(f"Va a eliminar al DNI {dni_alumno} - {alumnos[dni_alumno]["nombre"]} {alumnos[dni_alumno]["apellido"]}. ¿Esta seguro?\n"
                    "1. Si\n" \
                    "2. No\n" \
                    "\n" \
                    "Seleccionar opcion: ")
            match(opcion):
                case "1":
                    del alumnos[dni_alumno]
                    print("Alumno eliminado correctamente")
                    validez = True
                case "2":
                    validez = True
                    print("Ningún alumno fue eliminado")
                case _:
                    print("Valor incorrecto. Ingresar nuevamente")
                    validez = False
    else:
        print("El DNI ingresado no está en el sistema.")