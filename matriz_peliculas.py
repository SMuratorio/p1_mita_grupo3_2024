import validar

def crear_contenido_peliculas(contenido, proximo_id, titulo, tipo, genero, año, duracion):
    item = [proximo_id, titulo, tipo, genero, año, duracion]

    contenido.append(item)

    print(f"La {tipo} '{titulo}' creada con ID {proximo_id}.")

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
        print(f"Duración: {duracion}")
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

def eliminar_contenido_peliculas(contenido_peliculas):
    while True:
        eliminar_id_peliculas = input("Ingrese el ID de la pelicula/serie a eliminar: ").strip()

        # Verifica si el ID es un número
        if eliminar_id_peliculas.isdigit():
            eliminar_id_peliculas = int(eliminar_id_peliculas)
            # Verifica si el ID existe en el contenido
            if validar.si_existe_id_pelicula(eliminar_id_peliculas, contenido_peliculas):
                # Proceder a eliminar el contenido con el ID válido
                for item in contenido_peliculas:
                    if item[0] == eliminar_id_peliculas:
                        contenido_peliculas.remove(item)
                        print(f"La pelicula con ID {eliminar_id_peliculas} ha sido eliminado.")
                        return  # Sale de la función después de eliminar
            else:
                print(f"ID no encontrado. Por favor, ingrese un ID válido.")
        else:
            print("Por favor, ingrese un número válido.")  # Mensaje si el input no es numérico

def imprimir_matriz_peliculas(peliculas_ordenadas, ids, encabezado):
    """
    Pre: Recibe una matriz ya creada.
    Pos: Muestra por consola los elementos de la matriz.
    """
    # Imprimir el encabezado
    print(" " * 12, end="")  # Espacio para alinear los encabezados
    for i in encabezado:
        print(f"{i:>25}", end="") 
    print()   

    # Imprimir cada fila con el nombre de la pelicula/serie
    for i in range(len(peliculas_ordenadas)):
        print(f"{ids[i]:<12}", end="")
        for j in range(len(peliculas_ordenadas[i])):
            valor = str(peliculas_ordenadas[i][j]).capitalize() #mayuscula
            print(f"{valor:>25}", end="")
        print()
