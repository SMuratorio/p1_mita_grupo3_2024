import re

def validar_strings(strings): #valida apellido, genero y nombre   
    patron = r'^[A-Za-z]+$'
    return re.match(patron, strings) is not None

def validar_email(mail):
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(patron, mail) is not None

def validar_dni(dni):
    patron = r'^\d{2}\.\d{3}\.\d{3}$'  # Expresión regular para el formato XX.XXX.XXX
    return re.match(patron, dni) is not None

def validar_anio(anio):
    # Expresión regular para validar un año en formato YYYY (de 1900 a 2099)
    patron = r'^(19|20)\d{2}$'
    return re.match(patron, anio) is not None

def validar_tipo(tipo):
    opciones_validas = ["serie", "película", "pelicula"]
    return tipo in opciones_validas

def es_entero_positivo(entrada):
    """Función auxiliar para verificar si la entrada es un entero positivo."""
    if entrada.isdigit():
        return int(entrada) > 0
    return False

def validar_calificacion(calificacion):
    patron = r'^(?:[1-9]|10)$' # Expresión regular para validar que el número esté entre 1 y 10
    return re.match(patron, calificacion) is not None

def validar_estado(estado):
    estados_validos = ["en curso", "pendiente", "terminada"]    # Lista de estados válidos
    return estado.lower() in estados_validos # Verifica si el estado ingresado está en la lista de estados válidos

def validar_pelicula_id(contenido_peliculas, permitir_vacio=False):
    pelicula_id = input("Nuevo ID de película/serie: ") if permitir_vacio else input("Ingrese el ID de la película/serie: ")

    if permitir_vacio and pelicula_id == "":
        return None

    # Verificar si el ID es un número válido y si la película existe
    while not pelicula_id.isdigit() or obtener_titulo_pelicula(contenido_peliculas, int(pelicula_id)) is None:
        print("Error: " + ("El ID debe ser un número válido." if not pelicula_id.isdigit() else "El ID de la película/serie no existe."))
        pelicula_id = input("Nuevo ID de película/serie: ") if permitir_vacio else input("Ingrese el ID de la película/serie: ")

    return int(pelicula_id)  # Convertir a entero solo después de validar

def validar_usuario_id(matriz_usuarios, permitir_vacio=False):
    usuario_id = input("Nuevo ID de usuario: ") if permitir_vacio else input("Ingrese el ID del usuario: ")
    # Permitir dejar en blanco si el parámetro permitir_vacio está activado
    if permitir_vacio and usuario_id == "":
        return None
    # Verificar si el ID es un número válido y si el usuario existe
    while not usuario_id.isdigit() or obtener_apellido_usuario(matriz_usuarios, int(usuario_id)) is None:
        print("Error: " + ("El ID debe ser un número válido." if not usuario_id.isdigit() else "El ID del usuario no existe."))
        usuario_id = input("Nuevo ID de usuario: ") if permitir_vacio else input("Ingrese el ID del usuario: ")

    return int(usuario_id)  # Convertimos a entero solo después de validar

def validar_id_usuario(id_usuario, dic_parametros):
    if str(id_usuario).isdigit():
        matriz_usuarios = dic_parametros["matriz_usuarios"]
        for fila in matriz_usuarios:
            if fila[0] == int(id_usuario):
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

def si_existe_id(id_buscar, contenido): #Verifica si existe id para eliminar/actualizar ya sea series/peliculas, usuarios y registros
    for fila in contenido:
        if fila[0] == id_buscar:  # Asumiendo que el ID está en la primera posición
            return True
    return False

def manejar_error(mensaje_error, obtener_funcion):
    print(mensaje_error)
    return obtener_funcion()

def obtener_titulo_pelicula(contenindo_peliculas, pelicula_id):
    for pelicula in contenindo_peliculas:
        if pelicula[0] == pelicula_id:
            return pelicula[1]  # El título está en la columna 1
    return None  # No se encontró el ID

def obtener_apellido_usuario(contenido_usuarios, usuario_id):
    for usuario in contenido_usuarios:
        if usuario[0] == usuario_id:
            return usuario[2]  # El apellido está en la columna 2
    return None  # No se encontró el ID