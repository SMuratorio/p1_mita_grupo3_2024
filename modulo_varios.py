def imprimir_linea(num_columnas, ancho_columna):
    print("+" + "+".join(["-" * ancho_columna] * num_columnas) + "+")

def capitalizar_titulo(titulo):
     # Capitaliza la primera letra del título y cada palabra que tenga 3 letras o más
    palabras = titulo.split()
    capitalizado = []

    for palabra in palabras:
        if len(palabra) >= 3:
            capitalizado.append(palabra.capitalize())
        else:
            capitalizado.append(palabra)
    
    if capitalizado:# Capitaliza la primera letra del título completo
        capitalizado[0] = capitalizado[0].capitalize()
    return ' '.join(capitalizado)
