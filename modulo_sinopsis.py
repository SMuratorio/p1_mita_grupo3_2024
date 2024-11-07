import modulo_input, modulo_peliculas

def buscar_sinopsis(file, titulo):
    sinopsis = []
    for linea in file:
        if linea.startswith(titulo):  # Cuando encuentra el título
            sinopsis.append(linea.strip())
            for siguiente_linea in file:
                if siguiente_linea == "\n":  # Cuando encuentra la línea en blanco, termina
                    return "\n".join(sinopsis)  # Devuelve la sinopsis formateada
                sinopsis.append(siguiente_linea.strip())  # Agrega cada línea de sinopsis
    return None  # Retorna None si no encuentra la sinopsis

def leer_sinopsis(archivo, matriz_peliculas):
    try:
        id_pelicula = modulo_input.obtener_id(matriz_peliculas, "película/serie")  # Obtener ID
        titulo = modulo_peliculas.obtener_pelicula(int(id_pelicula), matriz_peliculas)["Titulo"]

        with open(archivo, "r", encoding="UTF-8") as file:
            sinopsis = buscar_sinopsis(file, titulo)

        if sinopsis:
            print(f"Sinopsis de '{titulo}':\n\n{sinopsis}")
        else:
            print(f"No se encontró la sinopsis para '{titulo}' en el archivo.")
            guardar_sinopsis_en_archivo(formatear_sinopsis(titulo))
            print(f"Sinopsis de '{titulo}' guardada correctamente.")
            
    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except OSError:
        print("Hubo un error al abrir el archivo.")
        
    return titulo, id_pelicula

def guardar_sinopsis_en_archivo(sinopsis_formateada):
    try:
        with open("sinopsis.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{sinopsis_formateada}")
    except Exception as e:
        print(f"Error al guardar la sinopsis: {e}")

def formatear_sinopsis(titulo, max_longitud=80):
    sinopsis = ""  # Inicializar la sinopsis como una cadena vacía

    while not sinopsis:  
        sinopsis = input("Ingrese la sinopsis de la película/serie: ").strip().capitalize()  # Eliminar espacios en blanco
        if not sinopsis:  # Verifica si la sinopsis sigue vacía
            print("La sinopsis no puede estar vacía. Por favor, ingrese una sinopsis válida.")

    # Dividir la sinopsis en palabras
    palabras = sinopsis.split()
    lineas = []
    linea_actual = ""
    
    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 > max_longitud:# Si la línea actual más la nueva palabra excede el límite
            lineas.append(linea_actual.strip())  # Agregar la línea actual a la lista
            linea_actual = palabra  # Comenzar una nueva línea
        else:
            linea_actual += " " + palabra  # Agregar la palabra a la línea actual

    lineas.append(linea_actual.strip())  # Agregar la última línea
    
    # Formatear la salida
    sinopsis_formateada = f"{titulo}\n" + "\n".join(lineas) + "\n"
    return sinopsis_formateada

def actualizar_sinopsis(archivo, matriz_peliculas):
    try:
        titulo, id_pelicula = leer_sinopsis(archivo, matriz_peliculas)
        nueva_sinopsis_formateada = formatear_sinopsis(titulo)
        
        with open(archivo, "r", encoding="UTF-8") as file:
            lineas = file.readlines()

        with open(archivo, "w", encoding="UTF-8") as file:
            escribir_lineas_actualizadas(file, lineas, titulo, nueva_sinopsis_formateada)

        print(f"La sinopsis de '{titulo}' ha sido actualizada.")

    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except OSError:
        print("Hubo un error al abrir el archivo.")

def escribir_lineas_actualizadas(file, lineas, titulo, nueva_sinopsis_formateada): #Escribe las líneas en el archivo, actualizando la sinopsis
    i = 0
    while i < len(lineas):
        if lineas[i].startswith(titulo):
            file.write(nueva_sinopsis_formateada)
            i += 1
            # Saltar las líneas de la sinopsis anterior
            while i < len(lineas) and lineas[i] != "\n":
                i += 1
        else:
            file.write(lineas[i])  # Escribir las demás líneas
            i += 1

def eliminar_sinopsis(archivo, matriz_peliculas):
    try:
        titulo, id_pelicula = leer_sinopsis(archivo, matriz_peliculas)
        # Leer el archivo actual y almacenar las líneas que no se eliminarán
        lineas_filtradas = []
        with open(archivo, "r", encoding="utf-8") as file:
            linea = file.readline()
            while linea:
                if linea.strip() == titulo: # Si encontramos el título, saltamos todas las líneas de la sinopsis
                    while linea.strip() != "": # Avanzar hasta la siguiente sinopsis
                        linea = file.readline()
                    # Continuar para leer las siguientes sinopsis (ya saltamos la actual)
                else:# Guardamos la línea si no es la sinopsis que queremos eliminar
                    lineas_filtradas.append(linea)
                    linea = file.readline()

        with open(archivo, "w", encoding="utf-8") as file:# Reescribir el archivo solo con las sinopsis restantes
            file.writelines(lineas_filtradas)
            print(f"\nLa sinopsis de '{titulo}' ha sido eliminada del archivo.")
    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except KeyError:
        print("El título ingresado no existe en la matriz de películas.")
    except Exception as e:
        print(f"Error al eliminar la sinopsis: {e}")

