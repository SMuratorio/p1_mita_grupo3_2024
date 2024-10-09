import re

def validar_strings(strings): #valida apellido, genero y nombre   
    patron = r'^[A-Za-z]{3,}$'
    return re.match(patron, strings) is not None

def validar_titulo(titulo):# Permite letras, números y signos especiales; no hay mínimo de letras
    patron = r'^[A-Za-z0-9\W]*$'  # \W permite todos los caracteres no alfanuméricos
    return re.match(patron, titulo) is not None

def validar_email(mail):
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(patron, mail) is not None

def validar_dni(dni):
    patron = r'^\d{2}\.\d{3}\.\d{3}$'  # Expresión regular para el formato XX.XXX.XXX
    return re.match(patron, dni) is not None

def validar_anio(anio): #Expresión regular para validar un año en formato YYYY (de 1900 a 2099)
    patron = r'^(19|20)\d{2}$'
    return re.match(patron, anio) is not None

def validar_tipo(tipo):
    opciones_validas = ["serie", "película", "pelicula"]
    return tipo in opciones_validas

def es_entero_positivo(entrada): #para validar duracion
    if entrada.isdigit():
        return int(entrada) > 0
    return False

def validar_calificacion(calificacion):
    patron = r'^(?:[1-9]|10)$' # Expresión regular para validar que el número esté entre 1 y 10
    return re.match(patron, calificacion) is not None

def validar_estado(estado):
    estados_validos = ["en curso", "pendiente", "terminada"]    # Lista de estados válidos
    return estado.lower() in estados_validos # Verifica si el estado ingresado está en la lista de estados válidos

def validar_id_actualizar(id, dic_parametros):
    if str(id).isdigit():
        matriz = dic_parametros["matriz"]
        for fila in matriz:
            if fila[0] == int(id):
                return True
    return False

def obtener_opcion(primera_consulta=True):
    while True:
        if primera_consulta:
            respuesta = "s"
        else:
            respuesta = input("\n¿Desea continuar? (s/n): ").strip().lower()
        
        if respuesta in ['s', 'n']:
            return respuesta
        else:
            print("Entrada no válida. Por favor, ingrese 's' o 'n'.")
