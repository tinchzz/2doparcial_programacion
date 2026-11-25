# cantidad total alumnos, promedio de notas, alumno con mayor nota, aprobados (≥ 6) y desaprobados (< 6).

def cantidad_alumnos(alumnos):
    print(f"Cantidad de alumnos: {len(alumnos.items())}")

def promedio_notas(alumnos):
    acumulador = 0
    divisor = 0
    for datos in alumnos.values():
        acumulador += datos["nota"]
        divisor+=1
    promedio = acumulador / divisor
    print(f"El promedio de las notas es: {promedio:.2f}")

def nota_mayor(alumnos):
    nota_mayor = 0
    dni_alumno = ""
    nombre_alumno = ""
    for dni, datos in alumnos.items():
        if nota_mayor < datos["nota"]:
            nota_mayor = datos["nota"]
            dni_alumno = dni
            nombre_alumno = datos["nombre"]+" "+datos["apellido"]
    if nota_mayor == int(nota_mayor):
        print(f"La nota mayor es: {int(nota_mayor)} de {nombre_alumno} ({dni_alumno})")
    else:
        print(f"La nota mayor es: {nota_mayor} de {nombre_alumno} ({dni_alumno})")

def evaluacion_alumnos(alumnos):
    aprobados = 0
    desaprobados = 0
    for datos in alumnos.values():
        if datos["nota"] >= 6:
            aprobados += 1
        else:
            desaprobados += 1
    print(f"Cantidad de aprobados: {aprobados}\n"
          f"Cantidad de desaprobados: {desaprobados}")
