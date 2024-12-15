import re, modulo_genero

def validar_strings(strings):  # Valida apellido y nombre
    patron = r'^[A-Za-zÁÉÍÓÚáéíóúÜüÑñ]{3,}$'
    return re.match(patron, strings) is not None

def validar_titulo(titulo):
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü0-9\-\.\,\!¡¿\?\'\s]+$"
    return re.match(patron, titulo) is not None

def validar_email(mail):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+$'
    return re.match(patron, mail) is not None

def validar_dni(dni):
    patron = r'^\d{2}\.\d{3}\.\d{3}$'  # Expresión regular para el formato XX.XXX.XXX
    return re.match(patron, dni) is not None

def validar_anio(anio): #Expresión regular para validar un año en formato YYYY (de 1900 a 2099)
    patron = r'^(19|20)\d{2}$'
    return re.match(patron, anio) is not None

def validar_tipo(tipo):
    opciones_validas = ["serie", "película", "pelicula"]
    return tipo.lower() in opciones_validas

def validar_duracion(entrada): #para validar duracion
    if entrada.isdigit():
        return int(entrada) > 0
    return False

def validar_calificacion(calificacion):
    patron = r'^(?:[1-9]|10)$' # Expresión regular para validar que el número esté entre 1 y 10
    return re.match(patron, calificacion) is not None

def validar_estado(estado):
    estados_validos = ["en curso", "pendiente", "terminada"]    # Lista de estados válidos
    return estado.lower() in estados_validos # Verifica si el estado ingresado está en la lista de estados válidos

def validar_genero(genero):
    """Valida que el género no esté vacío y que no exista ya en el diccionario."""
    return len(genero) > 3 and genero not in modulo_genero.dic_genero and genero.isalpha()
