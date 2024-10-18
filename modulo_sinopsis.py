import modulo_input, modulo_validar, modulo_peliculas

def leer_sinopsis(archivo, matriz_peliculas):
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == 's':
        try:
            id_pelicula = modulo_input.obtener_id(matriz_peliculas, "película/serie")  # Obtener ID
            titulo = modulo_peliculas.obtener_pelicula(int(id_pelicula), matriz_peliculas)["Titulo"]
            with open(archivo, "r", encoding="UTF-8") as file:
                sinopsis_encontrada = False
                linea = file.readline()  # Leer la primera línea
                while linea:  # Mientras haya líneas en el archivo
                    if linea.startswith(titulo):  # Buscar por título en la línea actual
                        print(f"Sinopsis de '{titulo}':\n")
                        print(linea)  # Imprimir la sinopsis
                        sinopsis_encontrada = True
                        # Leer las siguientes líneas hasta encontrar un bloque en blanco
                        while linea and linea != "\n":
                            linea = file.readline()
                            print(linea, end='')  # Imprimir la sinopsis línea por línea
                        break  # Salir del bucle una vez encontrada la sinopsis
                    linea = file.readline()  # Leer la siguiente línea

                if not sinopsis_encontrada:
                    print(f"No se encontró la sinopsis para '{titulo}' en el archivo.") #se supone que esto nunca va a pasar porque al agregar pelicula/serie
                                                                                        #te va a obligar a agregar sinopsis asi que dsp sacarlo.
        except FileNotFoundError:
            print("El archivo de sinopsis no existe.")
        except OSError:
            print("Hubo un error al abrir el archivo.")
        opcion_seleccionada = modulo_validar.obtener_opcion(False)