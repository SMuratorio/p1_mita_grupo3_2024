def archivo_a_matriz(nombre_archivo):
    matriz = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                fila = linea.strip().split(";")
                # Convertir el primer elemento (ID) a entero si es posible
                if fila and fila[0].isdigit():
                    fila[0] = int(fila[0])
                matriz.append(fila)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except IOError:
        print("Error al leer el archivo.")
    
    return matriz

def guardar_matriz_en_archivo(nombre_archivo, matriz, delimitador=";"):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for fila in matriz:
                linea = delimitador.join(str(elemento) for elemento in fila)
                archivo.write(linea + "\n")
    except IOError:
        print("Error al escribir en el archivo.")