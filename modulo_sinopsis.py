import modulo_input, modulo_peliculas

def buscar_sinopsis(file, titulo):
    for linea in file:
        if linea.startswith(titulo):
            sinopsis = [linea.strip()]
            for siguiente_linea in file:
                if siguiente_linea == "\n":
                    break
                sinopsis.append(siguiente_linea.strip())
            return "\n".join(sinopsis)
    return None

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