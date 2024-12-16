def buscar_sinopsis(archivo, id):
    try:
        with open(archivo, "r", encoding="UTF-8") as file:
            for linea in file:
                # Separar por ';' para obtener el ID, título y sinopsis
                partes = linea.strip().split(";")
                if len(partes) < 3:
                    continue  # Ignorar líneas mal formateadas
                id_actual, titulo, sinopsis = partes[0], partes[1], partes[2]
                if id_actual == str(id):  # Comparar el ID
                    return sinopsis
                
        return "Sinopsis no encontrada."
    except FileNotFoundError:
        return "El archivo no existe."
    except Exception as e:
        return f"Error inesperado: {e}"
    
def guardar_sinopsis_en_archivo(archivo, id_pelicula, titulo, sinopsis):
    try:
        with open(archivo, "a", encoding="utf-8") as file:
            # Escribir en formato ID;Título;Sinopsis
            file.write(f"{id_pelicula};{titulo};{sinopsis}\n")        
    except Exception as e:
        print(f"Error al guardar la sinopsis: {e}")

def actualizar_sinopsis(archivo, nueva_sinopsis, id):
    try:
        lineas_actualizadas = []
        sinopsis_actualizada = False  # Bandera para saber si ya se actualizó la sinopsis

        with open(archivo, "r", encoding="UTF-8") as file:
            lineas = file.readlines()

        for linea in lineas:
            partes = linea.strip().split(";")
            if len(partes) < 3:  # Verificar formato correcto
                lineas_actualizadas.append(linea)  # Mantener líneas mal formateadas
                continue

            id_actual, titulo, sinopsis = partes[0], partes[1], partes[2]
            if id_actual == str(id):  # Si encontramos el ID
                # Reemplazar la sinopsis con la nueva
                lineas_actualizadas.append(f"{id_actual};{titulo};{nueva_sinopsis}\n")
                sinopsis_actualizada = True
            else:
                # Mantener la línea original
                lineas_actualizadas.append(linea)

        if not sinopsis_actualizada:
            print(f"El ID '{id}' no se encontró en el archivo.")
            return

        # Sobrescribir el archivo con las líneas actualizadas
        with open(archivo, "w", encoding="UTF-8") as file:
            file.writelines(lineas_actualizadas)

    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except OSError:
        print("Hubo un error al abrir el archivo.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

def eliminar_del_archivo(archivo, id):
    try:
        # Crear una lista para almacenar las líneas que no se eliminarán
        lineas_filtradas = []

        # Leer el archivo línea por línea
        with open(archivo, "r", encoding="utf-8") as file:
            for linea in file:
                partes = linea.strip().split(";")
                if len(partes) >= 3 and partes[0] == str(id):
                    # Si el ID coincide, saltamos esta línea (no la agregamos)
                    continue
                lineas_filtradas.append(linea)  # Mantener las líneas que no se eliminan

        # Sobrescribir el archivo con las líneas restantes
        with open(archivo, "w", encoding="utf-8") as file:
            file.writelines(lineas_filtradas)

    except FileNotFoundError:
        print("El archivo de sinopsis no existe.")
    except Exception as e:
        print(f"Error al eliminar del archivo: {e}")

