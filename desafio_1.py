import random

def crear_matriz (n, m):
    """
    pre: recibe n y m. Donde n: filas y m:columnas
    pos: devuelve una matriz de NxM creada con ceros
    
    """
 
    return [[0]*m for fil in range (n)]

def llenar_matriz (m):
    """
    pre: recibe una matriz ya creada.
    pos: llena la matriz con valores aleatorios entre 1 y 10.

    """
    filas = len (m) 
    columnas = len (m [0]) 
    for fil in range (filas): 
        for col in range (columnas): 
            num_aleatorio = random.randint (1, 10)
            m [fil][col] = num_aleatorio 

def imprimir_matriz (matriz, estudiantes, materias):
    """
    pre: recibe una matriz ya creada.
    pos: muestra por consola los elementos de la matriz.
    
    """
     # Imprimir el encabezado de las materias
    print(" " * 12, end="")  # Espacio para alinear con los nombres de los estudiantes
    for materia in materias:
        print(f"{materia:>20}", end="")
    print()

    # Imprimir cada fila con el nombre del estudiante como encabezado
    for i in range(len(matriz)):
        print(f"{estudiantes[i]:<12}", end="")  # Encabezado del estudiante
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:>20}", end="")
        print()

def calcular_promedio_estudiantes(matriz):
    print("Promedio de calificaciones por estudiante:")
    for i in range(len(matriz)): #filas
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        promedio = suma / len(matriz[i])
        print(f"{estudiantes[i]}: {promedio:.2f}")

def calcular_promedio_materias(matriz):
    print("Promedio de calificaciones por materia:")
    for j in range(len(materias)):
        suma = 0
        for i in range(len(matriz)): 
            suma += matriz[i][j] 
        promedio = suma / len(matriz) 
        print(f"{materias[j]}: {promedio:.2f}")


# Programa principal
estudiantes=["Juliana", "Ayelen", "Sofia", "Barbara", "Daiana", "Martina", "Delfina", "Juan", "Mateo", "Emma"]
materias=["Programacion", "Algebra", "Quimica", "Teoria de sistemas", "Sistemas de informacion"]
matriz = crear_matriz (10, 5)
llenar_matriz (matriz)
imprimir_matriz (matriz, estudiantes, materias)

# 4. Calcular y mostrar los promedios
calcular_promedio_estudiantes(matriz)
calcular_promedio_materias(matriz)

