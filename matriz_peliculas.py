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



