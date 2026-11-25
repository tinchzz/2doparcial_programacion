# No se debe permitir:
# DNI duplicados. validaciones.py
# Edades negativas. validaciones.py
# Notas fuera del rango 0-10. validaciones.py
# Cada alumno posee: DNI, Nombre, Apellido, Edad, Nota final 
def validar_dni(dni, alumnos):
    if dni.isdigit():
        if 6 <= len(dni) <= 8:
            if dni in alumnos:
                return False
            return True
        return False
    return False

def validar_nota(nota):
    nota = float(nota)
    if 0 <= nota <= 10:
        return True
    return False

def validar_edad(edad):
    if edad.isdigit():
        edad = int(edad)
        if 0 <= edad <= 100:
            return True
        return False
    return False
