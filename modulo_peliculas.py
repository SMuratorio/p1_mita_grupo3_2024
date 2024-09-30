import validar

def crear_matriz_peliculas(matriz_peliculas):
    agregar_pelicula=validar.obtener_opcion()
    while agregar_pelicula=="s":
        proximo_id_peliculas=len(matriz_peliculas)+1
        print("\nAgregar pelicula o serie:")
        titulo=validar.obtener_titulo()
        tipo = validar.obtener_tipo()
        genero=validar.obtener_genero()
        anio = validar.obtener_anio()
        duracion = validar.validar_duracion(tipo)

        print(f"La {tipo} '{titulo}' creada con ID {proximo_id_peliculas}.")

        item = [proximo_id_peliculas, titulo, tipo, genero, anio, duracion]
        matriz_peliculas.append(item)

        agregar_pelicula=validar.obtener_opcion(primera_consulta=False)

def leer_matriz_peliculas(contenido):
    if not contenido:
        print("No hay contenido disponible.")
        print()
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

def actualizar_matriz_peliculas(contenido_peliculas):
    actualizar_pelicula=validar.obtener_opcion()
  
    while actualizar_pelicula == 's':
        actualizar_id_pelicula = input("Ingrese el ID de la pelicula a actualizar: ").strip()
        while not actualizar_id_pelicula.isdigit() or not validar.si_existe_id(int(actualizar_id_pelicula), contenido_peliculas):
            actualizar_id_pelicula = validar.manejar_error("ID no válido. Reintentando...", lambda: input("Ingrese un ID válido: "))
        
        actualizar_id_pelicula = int(actualizar_id_pelicula)

        for item in contenido_peliculas:
            if item[0] == actualizar_id_pelicula:
                print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")
                def validar_dato(dato, funcion_validar, obtener_funcion, actual):
                    return validar.manejar_error(f"{dato} no válido. Reintentando...", obtener_funcion) if dato and not funcion_validar(dato) else dato or actual

                nuevo_titulo = validar_dato(input("Nuevo titulo: ").strip().capitalize(), validar.validar_strings, validar.obtener_titulo, item[1])
                nuevo_tipo = validar_dato(input("Nuevo tipo: ").strip(). lower(), validar.validar_tipo, validar.obtener_tipo, item[2])
                nuevo_genero = validar_dato(input("Nuevo genero: ").strip(). capitalize(), validar.validar_strings, validar.obtener_genero, item[3])
                nuevo_anio = validar_dato(input("Nuevo año: ").strip(), validar.validar_anio, validar.obtener_anio, item[4])

                # Validar duración solo si el tipo es válido
                nuevo_duracion = None
                if nuevo_tipo and validar.validar_tipo(nuevo_tipo):
                    nuevo_duracion = validar.validar_duracion(nuevo_tipo)
                else:
                    nuevo_duracion = item[5]  # Mantener la duración existente si no se actualiza el tipo


                item[1], item[2], item[3], item[4], item[5] = nuevo_titulo, nuevo_tipo, nuevo_genero, nuevo_anio, nuevo_duracion
                print(f"{nuevo_titulo} {nuevo_tipo} con ID {actualizar_id_pelicula} ha sido actualizado.")
                actualizar_pelicula = validar.obtener_opcion(primera_consulta=False)
                
                return

def eliminar_matriz_peliculas(contenido_peliculas):
    eliminar_pelicula = validar.obtener_opcion()
    
    while eliminar_pelicula == 's':
        print("\nEliminar contenido:")
        eliminar_id_pelicula = input("Ingrese el ID de la pelicula/serie a eliminar: ").strip()

        while not eliminar_id_pelicula.isdigit() or not validar.si_existe_id(int(eliminar_id_pelicula), contenido_peliculas):
            if not eliminar_id_pelicula.isdigit():
                print("Por favor, ingrese un número válido.")
            else:
                print("ID no encontrado. Por favor, ingrese un ID válido.")
            eliminar_id_pelicula = input("Ingrese el ID de la pelicual/serie a eliminar: ").strip()
        
        eliminar_id_pelicula = int(eliminar_id_pelicula)
        
        # Eliminar el pelicula
        contenido_peliculas[:] = [item for item in contenido_peliculas if item[0] != eliminar_id_pelicula] 
        #[:] evita la creación de una nueva lista y modifica la lista existente.
        print(f"La pelicula/serie con ID {eliminar_id_pelicula} ha sido eliminado.")
        
        eliminar_pelicula = validar.obtener_opcion(primera_consulta=False)
    
def imprimir_matriz_peliculas(contenido_peliculas):
    for i in range(len(contenido_peliculas)):
        contenido_peliculas[i][1] = contenido_peliculas[i][1][:8]  #Recortar el título a 8 caracteres

    for pelicula in contenido_peliculas:  # Convertir el año a entero si está en formato de cadena
        pelicula[4] = int(pelicula[4])  # Convertir el año de estreno a entero
                            
    peliculas_ordenadas = sorted(contenido_peliculas, key=lambda x: x[4]) # Ordenar la lista por año de estreno (ascendente)
    
    ids_peliculas=[item[1] for item in peliculas_ordenadas]  # Nombres de las películas/series
    encabezado = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido

    # Imprimir el encabezado
    print(" " * 12, end="")  # Espacio para alinear los encabezados
    for i in encabezado:
        print(f"{i:>20}", end="") 
    print()   

    # Imprimir cada fila con el nombre de la pelicula/serie
    for i in range(len(peliculas_ordenadas)):
        print(f"{ids_peliculas[i]:<12}", end="")
        for j in range(len(peliculas_ordenadas[i])):
            valor = str(peliculas_ordenadas[i][j]).capitalize() #mayuscula
            print(f"{valor:>20}", end="")
        print()
    print()
    
def listar_matriz_peliculas(matriz_peliculas):
    # Convertir el año a entero si está en formato de cadena
    for pelicula in matriz_peliculas:
        pelicula[4] = int(pelicula[4])  # Convertir el año de estreno a entero

    # Ordenar la lista por año de estreno (ascendente)
    peliculas_ordenadas = sorted(matriz_peliculas, key=lambda x: x[4])

    #imprimir matriz
    encabezado = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido
    peliculas = [dict(zip(encabezado, fila)) for fila in peliculas_ordenadas]
    # Imprimir los diccionarios
    for pelis in peliculas:
        print(pelis)
    print()