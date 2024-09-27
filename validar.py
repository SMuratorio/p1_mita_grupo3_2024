import re

#Matriz usuarios

def validar_email(mail):
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(patron, mail) is not None

def obtener_email():
    while True:  # Bucle infinito hasta recibir un correo válido
        mail = input("Ingrese su correo electrónico: ").strip()
        if validar_email(mail):
            return mail  # Retorna el correo si es válido
        else:
            print("Correo no válido. Intente nuevamente.")


def validar_dni(dni):
    patron = r'^\d{2}\.\d{3}\.\d{3}$'  # Expresión regular para el formato XX.XXX.XXX
    return re.match(patron, dni) is not None

def obtener_dni():
    while True:  # Bucle infinito hasta recibir un DNI válido
        dni = input("Ingrese el DNI del usuario (con puntos, formato XX.XXX.XXX): ").strip()
        if validar_dni(dni):
            return dni  # Retorna el DNI si es válido
        else:
            print("El DNI ingresado no es válido. Intente nuevamente.")


def obtener_nombre():
    while True:
        nombre = input("Ingrese el nombre del usuario: ").strip().capitalize()
        if validar_strings(nombre):
            return nombre
        else:
            print("Nombre de usuario no válido. ", end="")


def obtener_apellido():
    while True:
        apellido = input("Ingrese el apellido del usuario: ").strip().capitalize()
        if validar_strings(apellido):
            return apellido
        else:
            print("Apellido de usuario no válido. ", end="")


#Matriz peliculas y series

def validar_anio(anio):
    # Expresión regular para validar un año en formato YYYY (de 1900 a 2099)
    patron = r'^(19|20)\d{2}$'
    return re.match(patron, anio) is not None

def obtener_anio():
    while True:  # Bucle infinito hasta recibir un año válido
        anio = input("Ingrese el año de estreno (formato YYYY): ").strip()
        if validar_anio(anio):
            return anio  # Retorna el año si es válido
        else:
            print("Año no válido. Intente nuevamente.")


def validar_tipo(tipo):
    opciones_validas = ["serie", "película", "pelicula"]
    return tipo in opciones_validas

def obtener_tipo():
    while True:  # Bucle infinito hasta recibir una respuesta válida
        tipo = input("Ingrese el tipo (serie/película): ").strip().lower()
        if validar_tipo(tipo):
            return tipo  # Retorna el tipo si es válido
        else:
            print("Entrada no válida. Por favor, ingrese 'serie' o 'película'.")


def es_entero_positivo(entrada):
    """Función auxiliar para verificar si la entrada es un entero positivo."""
    if entrada.isdigit():
        return int(entrada) > 0
    return False

def validar_duracion(tipo):
    while True:
        if tipo in ['película', 'pelicula']:
            entrada = input("Ingrese la duración de la película (en minutos): ").strip()
                    
            if es_entero_positivo(entrada):
                duracion = int(entrada)
                return f"{duracion} minutos"
            else:
                print("Duración no válida. Por favor, ingrese un número entero positivo.")

        elif tipo == 'serie':
            entrada = input("Ingrese la cantidad de temporadas: ").strip()

            if es_entero_positivo(entrada):
                temporadas = int(entrada)
                return f"{temporadas} temporadas"
            else:
                print("Cantidad no válida. Por favor, ingrese un número entero positivo.")

        else:
            print("El tipo ingresado no es válido.")
            return None


def obtener_titulo():
    while True:
        titulo = input("Ingrese el título de la serie/película: ").strip()
        if validar_strings(titulo):
            return titulo  
        else:
            print("Entrada no válida. Inténtelo de nuevo.")

    
def obtener_genero():
    while True:
        genero = input("Ingrese el género: ").strip()
        if validar_strings(genero):
            return genero
        else:
            print("Tipo de género no válido. ", end="")


#Matriz registro vistas

def validar_calificacion(calificacion):
    patron = r'^(?:[1-9]|10)$' # Expresión regular para validar que el número esté entre 1 y 10
    return re.match(patron, calificacion) is not None

def obtener_calificacion():
    while True:  # Bucle infinito hasta recibir una calificación válida
        calificacion = input("Ingrese la calificación (entero entre 1 y 10): ").strip()
        if validar_calificacion(calificacion):
            return int(calificacion)  # Retorna la calificación si es válida
        else:
            print("Calificación no válida. Debe ser un número entero entre 1 y 10. Intente nuevamente.")


def validar_estado(estado):
    estados_validos = ["en curso", "pendiente", "terminada"]    # Lista de estados válidos
    return estado.lower() in estados_validos # Verifica si el estado ingresado está en la lista de estados válidos

def obtener_estado():
    while True:  # Bucle infinito hasta recibir un estado válido
        estado = input("Ingrese el estado (en curso, pendiente, o terminada): ").strip().capitalize()
        if validar_estado(estado):
            return estado  # Retorna el estado si es válido
        else:
            print("Estado no válido. Debe ser 'en curso', 'pendiente' o 'terminada'. Intente nuevamente.")


def obtener_titulo_pelicula(contenindo_peliculas, pelicula_id):
    for pelicula in contenindo_peliculas:
        if pelicula[0] == pelicula_id:
            return pelicula[1]  # El título está en la columna 1
    return None  # No se encontró el ID


def validar_pelicula_id(contenido_peliculas, permitir_vacio=False):
    pelicula_id = input("Nuevo ID de película/serie: ") if permitir_vacio else input("Ingrese el ID de la película/serie: ")

    if permitir_vacio and pelicula_id == "":
        return None

    # Verificar si el ID es un número válido y si la película existe
    while not pelicula_id.isdigit() or obtener_titulo_pelicula(contenido_peliculas, int(pelicula_id)) is None:
        print("Error: " + ("El ID debe ser un número válido." if not pelicula_id.isdigit() else "El ID de la película/serie no existe."))
        pelicula_id = input("Nuevo ID de película/serie: ") if permitir_vacio else input("Ingrese el ID de la película/serie: ")

    return int(pelicula_id)  # Convertir a entero solo después de validar



def obtener_apellido_usuario(contenido_usuarios, usuario_id):
    for usuario in contenido_usuarios:
        if usuario[0] == usuario_id:
            return usuario[2]  # El apellido está en la columna 2
    return None  # No se encontró el ID


def validar_usuario_id(contenido_usuarios, permitir_vacio=False):
    usuario_id = input("Nuevo ID de usuario: ") if permitir_vacio else input("Ingrese el ID del usuario: ")

    # Permitir dejar en blanco si el parámetro permitir_vacio está activado
    if permitir_vacio and usuario_id == "":
        return None

    # Verificar si el ID es un número válido y si el usuario existe
    while not usuario_id.isdigit() or obtener_apellido_usuario(contenido_usuarios, int(usuario_id)) is None:
        print("Error: " + ("El ID debe ser un número válido." if not usuario_id.isdigit() else "El ID del usuario no existe."))
        usuario_id = input("Nuevo ID de usuario: ") if permitir_vacio else input("Ingrese el ID del usuario: ")

    return int(usuario_id)  # Convertimos a entero solo después de validar

#Otros
def validar_continuacion(primera_consulta=True):
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

def validar_strings(strings): #valida apellido, genero y nombre   
    patron = r'^[A-Za-z]+$'
    return re.match(patron, strings) is not None

def manejar_error(mensaje_error, obtener_funcion):
    print(mensaje_error)
    return obtener_funcion()
