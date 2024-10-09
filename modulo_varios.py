def imprimir_linea(tipo, num_columnas, ancho_columna): #Para imprimir cuadro de la matriz
    if tipo == "superior":
        print("+" + "+".join(["-" * ancho_columna] * num_columnas) + "+")
    elif tipo == "inferior":
        print("+" + "+".join(["-" * ancho_columna] * num_columnas) + "+")
    else:
        print("+" + "+".join(["-" * ancho_columna] * num_columnas) + "+")