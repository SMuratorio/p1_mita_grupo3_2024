import modulo_validar

def obtener_dinamico(mensaje_input, mensaje_output, funcion_validacion):
    while True:
        dato = input(mensaje_input).strip(). lower()
        if funcion_validacion(dato):
            return dato
        else:
            print(mensaje_output)

def obtener_usuario():
    nuevo_nombre = obtener_dinamico("Ingrese el nombre del usuario: ", "Nombre de usuario no válido. ", modulo_validar.validar_strings)
    nuevo_apellido = obtener_dinamico("Ingrese el apellido del usuario: ", "Apellido de usuario no válido. ", modulo_validar.validar_strings)
    nuevo_dni = obtener_dinamico("Ingrese el DNI del usuario (con puntos, formato XX.XXX.XXX): ", "El DNI ingresado no es válido. Intente nuevamente.",  modulo_validar.validar_dni)
    nuevo_mail = obtener_dinamico("Ingrese su correo electrónico: ", "Correo no válido. Intente nuevamente.", modulo_validar.validar_email)
    return (nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_mail) #Uso de tupla

def obtener_pelicula():
    nuevo_titulo = obtener_dinamico("Ingrese el título de la serie/película: ", "Entrada no válida. Inténtelo de nuevo.", modulo_validar.validar_strings)
    nuevo_tipo = obtener_dinamico("Ingrese el tipo (serie/película): ", "Entrada no válida. Por favor, ingrese 'serie' o 'película'.", modulo_validar.validar_tipo)
    nuevo_genero = obtener_dinamico("Ingrese el género: ", "Tipo de género no válido. ", modulo_validar.validar_strings)
    nuevo_anio = obtener_dinamico("Ingrese el año de estreno (formato YYYY): ", "Año no válido. Intente nuevamente.", modulo_validar.validar_anio)
    nueva_duracion = None
    if nuevo_tipo in ['película', 'pelicula']: 
        nueva_duracion = obtener_dinamico("Ingrese la duración de la película (en minutos): ", "Duración no válida. Por favor, ingrese un número entero positivo.", modulo_validar.es_entero_positivo) + " minutos"
    elif nuevo_tipo == 'serie':
        nueva_duracion = obtener_dinamico("Ingrese la cantidad de temporadas: ", "Cantidad no válida. Por favor, ingrese un número entero positivo.", modulo_validar.es_entero_positivo) + " temporadas"
    return (nuevo_titulo, nuevo_tipo, nuevo_genero, nuevo_anio, nueva_duracion) #Uso de tupla

def obtener_registro():
    nuevo_estado = obtener_dinamico("Ingrese el estado (en curso, pendiente, o terminada): ", "Estado no válido. Debe ser 'en curso', 'pendiente' o 'terminada'. Intente nuevamente.", modulo_validar.validar_estado)
    nueva_calificacion = obtener_dinamico("Ingrese la calificación (entero entre 1 y 10): ", "Calificación no válida. Debe ser un número entero entre 1 y 10. Intente nuevamente.", modulo_validar. validar_calificacion) if nuevo_estado.lower() == "terminada" else 0
    return (nuevo_estado, nueva_calificacion) #Uso de tupla
    