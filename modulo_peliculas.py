import modulo_validar, modulo_menu, modulo_varios, modulo_input, modulo_genero, modulo_sinopsis, modulo_matriz

matriz_peliculas=modulo_matriz.archivo_a_matriz("peliculas.txt")
titulos_existentes={titulo[1] for titulo in matriz_peliculas}

def crear_matriz_peliculas():
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == "s":
        proximo_id_peliculas = len(matriz_peliculas)+1
        print("\nAgregar pelicula o serie:")
        titulo, tipo, genero, anio, duracion = modulo_input.obtener_pelicula(titulos_existentes)

        sinopsis_formateada=modulo_sinopsis.formatear_sinopsis(titulo)  # Obtener sinopsis formateada
        modulo_sinopsis.guardar_sinopsis_en_archivo(sinopsis_formateada)

        print(f"La {tipo} '{titulo}' creada con ID {proximo_id_peliculas}.")

        sublista = [proximo_id_peliculas, titulo, tipo, genero, anio, duracion]
        matriz_peliculas.append(sublista)
        print("\nPelícula/Serie agregada con éxito.")

        modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
        leer_matriz_peliculas([sublista])

        opcion_seleccionada=modulo_validar.obtener_opcion(primera_consulta=False)

def leer_matriz_peliculas(peliculas):
    print("\nContenido registrado:")
    for fila in peliculas:
        proximo_id, titulo, tipo, genero, año, duracion = fila
        print(f"ID: {proximo_id}")
        print(f"Título: {titulo}")
        print(f"Tipo: {tipo}")
        print(f"Género: {genero}")
        print(f"Año: {año}")
        print(f"Duración: {duracion}")
        print("-" * 30)

def actualizar_matriz_peliculas():
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == 's':
        id_pelicula = int(modulo_input.obtener_id(matriz_peliculas, "pelicula/serie"))
        dic_pelicula_actualizar = obtener_pelicula(id_pelicula, matriz_peliculas)
        opcion_actualizar = modulo_menu.mostrar_submenu_actualizar(list(dic_pelicula_actualizar.keys())) #convierte las claves en lista
        # Llamada a la nueva función para validar y actualizar el valor
        dic_pelicula_actualizar = validar_y_actualizar_pelicula(opcion_actualizar, dic_pelicula_actualizar, id_pelicula, titulos_existentes)
        actualizar_pelicula(id_pelicula, matriz_peliculas, dic_pelicula_actualizar)
        modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
        
        opcion_seleccionada = modulo_validar.obtener_opcion(False)

def obtener_pelicula(id_pelicula, matriz_peliculas):
    for fila in matriz_peliculas:
        if fila[0] == id_pelicula:
            return {"Titulo":fila[1], "Tipo": fila[2], "Genero": fila[3], "Año": fila[4]}

def actualizar_pelicula(id_pelicula, matriz_peliculas, pelicula_actualizar):
    for fila in matriz_peliculas:
        if fila[0] == id_pelicula:
            fila[1] = pelicula_actualizar["Titulo"]
            fila[2] = pelicula_actualizar["Tipo"]
            fila[3] = pelicula_actualizar["Genero"]
            fila[4] = pelicula_actualizar["Año"]
            return

def validar_y_actualizar_pelicula(opcion_actualizar, dic_pelicula_actualizar, id_pelicula, titulos_existentes):
    validadores = {"Titulo": lambda titulo: modulo_validar.validar_titulo(titulo) and modulo_varios.capitalizar_titulo(titulo) not in titulos_existentes, 
                   "Tipo": modulo_validar.validar_tipo,
                   "Genero": lambda genero: True,
                   "Año": modulo_validar.validar_anio}

    titulo_actual = dic_pelicula_actualizar.get("Titulo")  
    valor_actual = dic_pelicula_actualizar.get(opcion_actualizar)   
    
    if opcion_actualizar == "Genero":
        print(f"Va a actualizar el campo 'Genero' cuyo valor actual es: '{valor_actual}'.")
        nuevo_valor= modulo_genero.seleccionar_genero()
        
    else:
        nuevo_valor = modulo_input.obtener_nuevo_valor(opcion_actualizar, dic_pelicula_actualizar, validadores).capitalize()

    if opcion_actualizar == "Tipo":  # Se verifica si se está actualizando el tipo
        if nuevo_valor in ["película", "pelicula"]:
            duracion = modulo_input.obtener_dinamico("Ingrese la duración de la película (en minutos): ","Duración no válida. Por favor, ingrese un número entero positivo.",
                                                      modulo_validar.validar_duracion)
            dic_pelicula_actualizar["Duracion"] = f"{duracion} minutos"  # Actualizar duración para película
        elif nuevo_valor == "serie":
            duracion = modulo_input.obtener_dinamico("Ingrese la cantidad de temporadas: ","Cantidad no válida. Por favor, ingrese un número entero positivo.",
                                                      modulo_validar.validar_duracion)
            dic_pelicula_actualizar["Duracion"] = f"{duracion} temporadas"  # Actualizar duración para serie
    
    if opcion_actualizar == "Titulo":
        titulos_existentes.discard(titulo_actual);titulos_existentes.add(nuevo_valor)
    
    dic_pelicula_actualizar[opcion_actualizar] = nuevo_valor #diccionario que almacena la información de un usuario.
    print(f"{nuevo_valor} con ID {id_pelicula} ha sido actualizado.") #Movi el print aca
    return dic_pelicula_actualizar

def eliminar_matriz_peliculas():
    eliminar_pelicula = modulo_validar.obtener_opcion()
    while eliminar_pelicula == 's':
        print("\nEliminar contenido:")
        id_pelicula = int(modulo_input.obtener_id(matriz_peliculas, "pelicula/serie"))
        # Eliminar el pelicula
        matriz_peliculas[:] = [item for item in matriz_peliculas if item[0] != id_pelicula] 
        #[:] evita la creación de una nueva lista y modifica la lista existente.
        print(f"La pelicula/serie con ID {id_pelicula} ha sido eliminado.")
        modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
        
        eliminar_pelicula = modulo_validar.obtener_opcion(primera_consulta=False)
    
def imprimir_matriz_peliculas(contenido_peliculas):
    for i in range(len(contenido_peliculas)):
        contenido_peliculas[i][1] = contenido_peliculas[i][1][:8]  #Recortar el título a 8 caracteres

    for pelicula in contenido_peliculas:  # Convertir el año a entero si está en formato de cadena
        pelicula[4] = int(pelicula[4])  # Convertir el año de estreno a entero
                            
    matriz_peliculas_ordenadas = sorted(contenido_peliculas, key=lambda x: x[4]) # Ordenar la lista por año de estreno (ascendente)
    encabezado_pelilculas = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido

    ancho_columna=25  
    modulo_varios.imprimir_linea("superior", len(encabezado_pelilculas), ancho_columna)# Imprimir la línea superior del cuadro
    
    print("|" + "|".join([f"{encabezado:<{ancho_columna}}" for encabezado in encabezado_pelilculas]) + "|")  # Imprimir el encabezado
    
    modulo_varios.imprimir_linea("interior", len(encabezado_pelilculas), ancho_columna)    # Imprimir la línea interior del cuadro
    
    for fila in matriz_peliculas_ordenadas:    # Imprimir cada fila de la matriz
        print("|" + "|".join([f"{str(valor).capitalize():<{ancho_columna}}" for valor in fila]) + "|")
    
    modulo_varios.imprimir_linea("inferior", len(encabezado_pelilculas), ancho_columna) # Imprimir la línea inferior del cuadro
