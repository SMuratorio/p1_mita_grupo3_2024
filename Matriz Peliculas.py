#Matriz Peliculas

def crear_contenido_peliculas(contenido, proximo_id, titulo, tipo, genero, año, duracion):
    item = [proximo_id, titulo, tipo, genero, año, duracion]

    contenido.append(item)

    print(f"La {tipo} '{titulo}' creada con ID {proximo_id}.")

    return contenido

def leer_contenido_peliculas(contenido):
    if not contenido:
        print("No hay contenido disponible.")
        return
    
    for item in contenido:
        proximo_id, titulo, tipo, genero, año, duracion = item
        print(f"ID: {proximo_id}")
        print(f"Título: {titulo}")
        print(f"Tipo: {tipo}")
        print(f"Género: {genero}")
        print(f"Año: {año}")
        print(f"Duración: {duracion} minutos")
        print("-" * 30)

def actualizar_contenido_peliculas(contenido, item_id, titulo=None, tipo=None, genero=None, año=None, duracion=None):
    for item in contenido:
        if item[0] == item_id:
            item[1] = titulo if titulo is not None and titulo != '' else item[1]
            item[2] = tipo if tipo is not None and tipo != '' else item[2]
            item[3] = genero if genero is not None and genero != '' else item[3]
            item[4] = año if año is not None else item[4]
            item[5] = duracion if duracion is not None and duracion != '' else item[5]
            print(f"{item[2]} con ID {item_id} actualizada.")
            return
    print(f"No se encontró el contenido con ID {item_id}.")

def eliminar_contenido_peliculas(contenido, item_id):
    for item in contenido:
        if item[0] == item_id:
            contenido.remove(item)
            print(f"El {item[2]} con ID {item_id} ha sido eliminado.")
            return
    print(f"No se encontró el contenido con ID {item_id}.")

def crear_matriz_peliculas(n, m):
    """
    pre: recibe n y m. Donde n: filas y m:columnas
    pos: devuelve una matriz de NxM creada con ceros
    
    """
    """return [[0]*m for fil in range (n)]"""
    return [[0]*m for _ in range(n)]

def llenar_matriz_peliculas(m, peliculas_ordenadas):
    """
    Pre: Recibe una matriz ya creada y una lista 'contenido' que contiene otras listas.
    Pos: Llena la matriz con los valores de la lista 'contenido'.
    """
    for i in range(len(peliculas_ordenadas)):
        for j in range(len(peliculas_ordenadas[i])):
            m[i][j] = peliculas_ordenadas[i][j]

def imprimir_matriz_peliculas(matriz, ids, encabezado):
    """
    Pre: Recibe una matriz ya creada.
    Pos: Muestra por consola los elementos de la matriz.
    """
    # Imprimir el encabezado
    print(" " * 12, end="")  # Espacio para alinear con los nombres
    for i in encabezado:
        print(f"{i:>15}", end="") 
    print()   

    # Imprimir cada fila con el nombre de la pelicula/serie
    for i in range(len(matriz)):
        print(f"{ids[i]:<12}", end="")
        for j in range(len(matriz[i])):
            valor = str(matriz[i][j]).capitalize() #mayuscula
            print(f"{valor:>15}", end="")
        print()


contenido = []
proximo_id_peliculas = 1
b=1
continuar = 0

while continuar == 0:
    titulo = input("Ingrese el nombre de la película/serie: ")
    tipo = input("Indique si es una serie o película: ")
    genero = input("Indique el género: ")
    año = int(input("Indique su año de estreno: "))
    duracion = input("Indique la duración: ")

    conte = crear_contenido_peliculas(contenido, proximo_id_peliculas, titulo, tipo, genero, año, duracion)
    proximo_id_peliculas+=1
    
    continuar = int(input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
    
    if continuar == -1:
        continuar = -1


# PROGRAMA PRINCIPAL
print("\nContenido registrado:")
leer_contenido_peliculas(contenido)

# Preguntar si se desea actualizar contenido
actualizar_opcion_peliculas = input("\n¿Desea actualizar contenido? (s/n): ").lower()

while actualizar_opcion_peliculas == 's':
    print("\nActualizar contenido:")

    nuevo_id_peliculas = int(input("Ingrese el ID de la película/serie a cambiar: "))
    print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

    nuevo_titulo = input("Nuevo título (deje en blanco para no cambiar): ")
    nuevo_tipo = input("Nuevo tipo (deje en blanco para no cambiar): ")
    nuevo_genero = input("Nuevo género (deje en blanco para no cambiar): ")
    nuevo_año_str = input("Nuevo año (deje en blanco para no cambiar): ")
    nuevo_duracion = input("Nueva duración (deje en blanco para no cambiar): ")

    # Convertir nuevo año a entero si no está vacío
    nuevo_año = int(nuevo_año_str) if nuevo_año_str else None

    actualizar_contenido_peliculas(contenido, nuevo_id_peliculas, titulo=nuevo_titulo, tipo=nuevo_tipo, genero=nuevo_genero, año=nuevo_año, duracion=nuevo_duracion)

    print("\nContenido actualizado:")
    leer_contenido_peliculas(contenido)
    
    # Preguntar si se desea seguir actualizando
    actualizar_opcion_peliculas = input("\n¿Desea seguir actualizando contenido? (s/n): ").lower()

# Preguntar si se desea eliminar contenido
eliminar_opcion_peliculas = input("\n¿Desea eliminar contenido? (s/n): ").lower()

while eliminar_opcion_peliculas == 's':
    print("\nEliminar contenido:")

    eliminar_id_peliculas = int(input("Ingrese el ID de la película/serie a eliminar: "))
    eliminar_contenido_peliculas(contenido, eliminar_id_peliculas)

    print("\nContenido después de la eliminación:")
    leer_contenido_peliculas(contenido)
    
    # Preguntar si se desea seguir eliminando
    eliminar_opcion_peliculas = input("\n¿Desea seguir eliminando contenido? (s/n): ").lower()

print("\nProceso finalizado.")

#Recortar los títulos a un máximo de 8 caracteres
for i in range(len(contenido)):
    contenido[i][1] = contenido[i][1][:8]  #Recortar el título a 8 caracteres

# Ordenar la lista por año de estreno (ascendente)
peliculas_ordenadas = sorted(contenido, key=lambda x: x[4])

#crear matriz
matriz = crear_matriz_peliculas (len(contenido),6)

#llenar matriz
llenar_matriz_peliculas(matriz, peliculas_ordenadas)

#imprimir matriz
ids_peliculas=[item[1] for item in peliculas_ordenadas]  # Nombres de las películas/series
encabezado = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido

imprimir_matriz_peliculas(matriz, ids_peliculas, encabezado)