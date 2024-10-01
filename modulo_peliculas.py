import modulo_validar, modulo_menu, modulo_input

def crear_matriz_peliculas(matriz_peliculas):
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == "s":
        proximo_id_peliculas = len(matriz_peliculas)+1
        print("\nAgregar pelicula o serie:")
        titulo, tipo, genero, anio, duracion = modulo_input.obtener_pelicula()

        print(f"La {tipo} '{titulo}' creada con ID {proximo_id_peliculas}.")

        fila = [proximo_id_peliculas, titulo, tipo, genero, anio, duracion]
        matriz_peliculas.append(fila)
        print("\nPelícula/Serie agregada con éxito.")
        opcion_seleccionada=modulo_validar.obtener_opcion(primera_consulta=False)

def leer_matriz_peliculas(matriz_peliculas):
    if not matriz_peliculas:
        print("No hay contenido disponible.")
        print()
        return
    
    print("\nContenido registrado:")
    for fila in matriz_peliculas:
        proximo_id, titulo, tipo, genero, año, duracion = fila
        print(f"ID: {proximo_id}")
        print(f"Título: {titulo}")
        print(f"Tipo: {tipo}")
        print(f"Género: {genero}")
        print(f"Año: {año}")
        print(f"Duración: {duracion}")
        print("-" * 30)

def actualizar_matriz_peliculas(matriz_peliculas):
    opcion_seleccionada=modulo_validar.obtener_opcion()
  
    while opcion_seleccionada == 's':
        id_pelicula = input("Ingrese el ID de la pelicula/serie a actualizar: ").strip()
        while not id_pelicula.isdigit() or not modulo_validar.si_existe_id(int(id_pelicula), matriz_peliculas):
            id_pelicula = modulo_validar.manejar_error("ID no válido. Reintentando...", lambda: input("Ingrese un ID válido: "))
        
        id_pelicula = int(id_pelicula)

        dic_pelicula_actualizar = obtener_pelicula(id_pelicula, matriz_peliculas)
        opcion_actualizar = modulo_menu.mostrar_submenu_actualizar(list(dic_pelicula_actualizar.keys()))
        nuevo_valor = input(f"Ingrese el nuevo {opcion_actualizar}, valor anterior {dic_pelicula_actualizar[opcion_actualizar]} : ")
        dic_pelicula_actualizar[opcion_actualizar] = nuevo_valor
        actualizar_pelicula(id_pelicula, matriz_peliculas, dic_pelicula_actualizar)
        print(f" El {opcion_actualizar}: {nuevo_valor} con ID {id_pelicula} ha sido actualizado.")
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

def eliminar_matriz_peliculas(contenido_peliculas):
    eliminar_pelicula = modulo_validar.obtener_opcion()
    
    while eliminar_pelicula == 's':
        print("\nEliminar contenido:")
        eliminar_id_pelicula = input("Ingrese el ID de la pelicula/serie a eliminar: ").strip()

        while not eliminar_id_pelicula.isdigit() or not modulo_validar.si_existe_id(int(eliminar_id_pelicula), contenido_peliculas):
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
        
        eliminar_pelicula = modulo_validar.obtener_opcion(primera_consulta=False)
    
def imprimir_matriz_peliculas(contenido_peliculas):
    for i in range(len(contenido_peliculas)):
        contenido_peliculas[i][1] = contenido_peliculas[i][1][:8]  #Recortar el título a 8 caracteres

    for pelicula in contenido_peliculas:  # Convertir el año a entero si está en formato de cadena
        pelicula[4] = int(pelicula[4])  # Convertir el año de estreno a entero
                            
    peliculas_ordenadas = sorted(contenido_peliculas, key=lambda x: x[4]) # Ordenar la lista por año de estreno (ascendente)
    encabezado = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido

    # Imprimir el encabezado
    for i in encabezado:
        print(f"{i:<20}", end="") 
    print()   

    # Imprimir cada fila con el nombre de la pelicula/serie
    for i in range(len(peliculas_ordenadas)):
        for j in range(len(peliculas_ordenadas[i])):
            valor = str(peliculas_ordenadas[i][j]).capitalize() #mayuscula
            print(f"{valor:<20}", end="")
        print()
    print()
    
def listar_matriz_peliculas(matriz_peliculas):
    # Convertir el año a entero si está en formato de cadena
    print("\nContenido registrado:")
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