# Pregunta elegida: Matrices - Verdaderas: (A, B, F) Falsas: (C, D, E)

def crear_estanteria():
    filas = int(input("Ingresar la cantidad de filas de la estanteria: "))
    columnas = int(input("Ingresar la cantidad de columnas de la estanteria: "))

    estanteria = []

    for i in range(0, filas):
        print(f"Creando {i+1}° fila")
        fila = [] # B. (correcta) Creando filas
        for j in range(0, columnas):
            fila.append(input("Ingresar dato: ")) # B. (correcta) Creando columnas
        estanteria.append(fila) # A. (correcta) Listas anidadas

    return estanteria

def mostrar_estanteria(matriz): # D. (falsa) No se recorren con ciclos. Acá se recorre con for anidados
    for f in range(len(matriz)):
        fila = []
        for c in range(len(matriz[f])):
            fila.append(matriz[f][c])
        print(fila)

def modificar_estanteria(matriz):
    for f in range(len(matriz)):
        print(f"Posiciones disponibles fila {f+1}: ")
        for c in range(len(matriz[f])):
            print(f"Columna {c+1}")

    while not False:
        opcion = int(input("1. Leer \n2. Modificar: "))
        fila = int(input("Numero de fila:"))
        columna = int(input("Numero de columna:"))
        match(opcion):
            case 1:
                print(matriz[fila-1][columna-1]) # F. (correcta) Acceso por fila y columna
                return
            case 2:
                print(matriz[fila-1][columna-1])
                nuevo_valor = input("Ingresar nuevo valor: ")
                matriz[fila-1][columna-1] = nuevo_valor
                mostrar_estanteria(matriz)
                return
            case _:
                print("Opcion incorrecta")


estanteria = crear_estanteria()
print(type(estanteria)) # C. (falsa) Tipo nativo matrix. Python dice que es list
mostrar_estanteria(estanteria)
modificar_estanteria(estanteria)

estanteria_libro = [
    ["990000","Programacion",2026,True],
    ["990001","Matematica",2023,True],
    ["990002","Ingles",2025,False]
]

for f in range(len(estanteria_libro)):
    print(f"Libro {f+1}: ")
    for c in range(len(estanteria_libro[f])):
        print(f"{estanteria_libro[f][c]} - {type(estanteria_libro[f][c])}") # E. (falsa) Mismo tipo obligatorio. La salida muestra str, int y bool en la misma matriz.