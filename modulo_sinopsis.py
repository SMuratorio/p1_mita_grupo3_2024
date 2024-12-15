def buscar_sinopsis(archivo, titulo):
    sinopsis = []
    encontrado = False  # Indica si el título ha sido encontrado

    try:
        with open(archivo, "r", encoding="UTF-8") as file:
            for linea in file:
                if linea.startswith(titulo):  # Cuando encuentra el título
                    encontrado = True
                elif encontrado:
                    if linea == "\n":  # Si encuentra una línea en blanco, termina la sinopsis
                        encontrado = False  # Marcamos que la sinopsis ha terminado
                    else:
                        sinopsis.append(linea.strip())  # Agrega la línea a la sinopsis

        return "\n".join(sinopsis)+"\n" if sinopsis else ""  # Devuelve la sinopsis o None si no se encuentra

    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except OSError:
        print("Hubo un error al abrir el archivo.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

def guardar_sinopsis_en_archivo(sinopsis_formateada):
    try:
        with open("sinopsis.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{sinopsis_formateada}")
    except Exception as e:
        print(f"Error al guardar la sinopsis: {e}")

def formatear_sinopsis(titulo, sinopsis, max_longitud=80):
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

def actualizar_sinopsis(archivo, sinopsis, titulo):
    try:
        nueva_sinopsis_formateada = formatear_sinopsis(titulo, sinopsis)

        with open(archivo, "r", encoding="UTF-8") as file:
            lineas_actualizadas = []
            while (linea := file.readline()):
                if linea.strip().startswith(titulo):  # Verifica si la línea corresponde al título
                    lineas_actualizadas.append(f"{titulo}: {nueva_sinopsis_formateada}\n")
                else:
                    lineas_actualizadas.append(linea)

        with open(archivo, "w", encoding="UTF-8") as file:
            for linea in lineas_actualizadas:
                file.write(linea)

    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except OSError:
        print("Hubo un error al abrir el archivo.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

def eliminar_sinopsis(archivo, titulo, matriz_peliculas):
    try:
        #titulo, id_pelicula = leer_sinopsis(archivo, matriz_peliculas)

        # Abrir el archivo para leer línea por línea
        with open(archivo, "r", encoding="utf-8") as file:
            lineas_filtradas = []
            saltar_lineas = False

            linea = file.readline()
            while linea:
                if linea.strip() == titulo:  # Detecta el inicio de la sinopsis
                    saltar_lineas = True
                elif saltar_lineas and linea.strip() == "":  # Fin de la sinopsis
                    saltar_lineas = False
                elif not saltar_lineas:
                    lineas_filtradas.append(linea)  # Guarda las líneas que no se eliminarán

                linea = file.readline()  # Leer la siguiente línea

        # Sobrescribir el archivo con las sinopsis restantes
        with open(archivo, "w", encoding="utf-8") as file:
            file.writelines(lineas_filtradas)
            print(f"\nLa sinopsis de '{titulo}' ha sido eliminada del archivo.")

    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except KeyError:
        print("El título ingresado no existe en la matriz de películas.")
    except Exception as e:
        print(f"Error al eliminar la sinopsis: {e}")

def eliminar_del_archivo(archivo, titulo): #elimina sinopsis en cuando se elimina de la matriz peliculas
    try:
        # Crear una lista para almacenar las líneas que no se eliminarán
        lineas_filtradas = []
        saltar_lineas = False

        # Leer el archivo línea por línea
        with open(archivo, "r", encoding="utf-8") as file:
            while (linea := file.readline()):
                if linea.strip() == titulo:  # Detecta el inicio de la sinopsis
                    saltar_lineas = True
                elif saltar_lineas and linea.strip() == "":  # Fin de la sinopsis
                    saltar_lineas = False
                elif not saltar_lineas:
                    lineas_filtradas.append(linea)  # Guarda las líneas que no se eliminarán

        # Sobrescribir el archivo con las sinopsis restantes
        with open(archivo, "w", encoding="utf-8") as file:
            file.writelines(lineas_filtradas)

    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except Exception as e:
        print(f"Error al eliminar del archivo: {e}")
