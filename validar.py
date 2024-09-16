import re

#Matriz usuarios

def validar_email(mail, permitir_blanco=False):
    if permitir_blanco and mail == "":
        return True  # Si se permite blanco y el correo está vacío, es válido (no se actualiza)
    
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(patron, mail) is not None

def obtener_email(permitir_blanco=False):
    while True:  # Bucle infinito hasta recibir un correo válido
        mail = input("Ingrese su correo electrónico: ").strip()
        if validar_email(mail, permitir_blanco):
            return mail  # Retorna el correo si es válido
        else:
            print("Correo no válido. Intente nuevamente.")


def validar_dni(dni, permitir_blanco=False):
    if permitir_blanco and dni == "":
        return True  # Si se permite blanco y el DNI está vacío, es válido (no se actualiza)
    
    patron = r'^\d{2}\.\d{3}\.\d{3}$'  # Expresión regular para el formato XX.XXX.XXX
    return re.match(patron, dni) is not None

def obtener_dni(permitir_blanco=False):
    while True:  # Bucle infinito hasta recibir un DNI válido
        dni = input("Ingrese el DNI del usuario (con puntos, formato XX.XXX.XXX): ").strip()
        if validar_dni(dni, permitir_blanco):
            return dni  # Retorna el DNI si es válido
        else:
            print("El DNI ingresado no es válido. Intente nuevamente.")


def validar_nombre(nombre, permitir_blanco=False):    
    if permitir_blanco and nombre == "":
        return True 
    patron = r'[A-Za-z]'
    return re.match(patron, nombre) is not None
    
def obtener_nombre(permitir_blanco=False):
    while True:
        nombre = input("Ingrese el nombre del usuario: ").strip().capitalize()
        if validar_genero(nombre, permitir_blanco):
            return nombre
        else:
            print("Nombre de usuario no válido. ", end="")


def validar_apellido(apellido, permitir_blanco=False):    
    if permitir_blanco and apellido == "":
        return True 
    patron = r'[A-Za-z]'
    return re.match(patron, apellido) is not None
    
def obtener_apellido(permitir_blanco=False):
    while True:
        apellido = input("Ingrese el apellido del usuario: ").strip().capitalize()
        if validar_genero(apellido, permitir_blanco):
            return apellido
        else:
            print("Apellido de usuario no válido. ", end="")


def si_existe_id_usuario(id_usuario, contenido_usuario):
    for usuario in contenido_usuario:
        if usuario[0] == id_usuario:  # Se asume que el ID está en la primera posición de cada fila
            return True
    return False


#Matriz peliculas y series

def validar_año(año, permitir_blanco=False):
    if permitir_blanco and año == "":
        return True  # Si se permite blanco y el año está vacío, es válido (no se actualiza)
    
    # Expresión regular para validar un año en formato YYYY (de 1900 a 2099)
    patron = r'^(19|20)\d{2}$'
    return re.match(patron, año) is not None

def obtener_año(permitir_blanco=False):
    while True:  # Bucle infinito hasta recibir un año válido
        año = input("Ingrese el año de estreno (formato YYYY): ").strip()
        if validar_año(año, permitir_blanco):
            return año  # Retorna el año si es válido
        else:
            print("Año no válido. Intente nuevamente.")


def validar_tipo(tipo, permitir_blanco=False):
    opciones_validas = ["serie", "película", "pelicula"]
    
    if permitir_blanco and tipo == "":
        return True  # Si se permite blanco y el tipo está vacío, es válido (no se actualiza)
    
    return tipo in opciones_validas

def obtener_tipo(permitir_blanco=False):
    while True:  # Bucle infinito hasta recibir una respuesta válida
        tipo = input("Ingrese el tipo (serie/película): ").strip().lower()
        if validar_tipo(tipo, permitir_blanco):
            return tipo  # Retorna el tipo si es válido
        else:
            print("Entrada no válida. Por favor, ingrese 'serie' o 'película'.")


def es_entero_positivo(entrada):
    """Función auxiliar para verificar si la entrada es un entero positivo."""
    if entrada.isdigit():
        return int(entrada) > 0
    return False

def validar_duracion(tipo, permitir_blanco=False):
    while True:
        if tipo in ['película', 'pelicula']:
            entrada = input("Ingrese la duración de la película (en minutos): ").strip()
            
            if entrada == "":
                if permitir_blanco:
                    return None  # O cualquier otro valor que prefieras para representar una entrada en blanco
                else:
                    print("No puede dejar el campo en blanco.")
                    
            elif es_entero_positivo(entrada):
                duracion = int(entrada)
                return f"{duracion} minutos"
            else:
                print("Duración no válida. Por favor, ingrese un número entero positivo.")

        elif tipo == 'serie':
            entrada = input("Ingrese la cantidad de temporadas: ").strip()
            
            if entrada == "":
                if permitir_blanco:
                    return None  # O cualquier otro valor que prefieras para representar una entrada en blanco
                else:
                    print("No puede dejar el campo en blanco.")
            elif es_entero_positivo(entrada):
                temporadas = int(entrada)
                return f"{temporadas} temporadas"
            else:
                print("Cantidad no válida. Por favor, ingrese un número entero positivo.")

        else:
            print("El tipo ingresado no es válido.")
            return None


def validar_titulo(titulo, permitir_blanco=False):
    if permitir_blanco:
        return True
    return titulo != ""  

def obtener_titulo(permitir_blanco=False):
    while True:
        titulo = input("Ingrese el título de la serie/película: ").strip().lower()
        if validar_titulo(titulo, permitir_blanco):
            return titulo  
        else:
            print("Entrada no válida. Inténtelo de nuevo.")

   
def validar_genero(genero, permitir_blanco=False):    
    if permitir_blanco and genero == "":
        return True 
    patron = r'[A-Za-z]'
    return re.match(patron, genero) is not None
    
def obtener_genero(permitir_blanco=False):
    while True:
        genero = input("Ingrese el género: ").strip().lower()
        if validar_genero(genero, permitir_blanco):
            return genero
        else:
            print("Tipo de género no válido. ", end="")


def si_existe_id_pelicula(id_pelicula, contenido):
    for pelicula in contenido:
        if pelicula[0] == id_pelicula:  # Asumiendo que el ID está en la primera posición
            return True
    return False


#Matriz registro vistas

def validar_calificacion(calificacion, permitir_blanco=False):
    if permitir_blanco and calificacion == "":
        return True  # Si se permite blanco y la calificación está vacía, es válida (no se actualiza)

    # Expresión regular para validar que el número esté entre 1 y 10
    patron = r'^(?:[1-9]|10)$'
    return re.match(patron, calificacion) is not None

def obtener_calificacion(permitir_blanco=False):
    while True:  # Bucle infinito hasta recibir una calificación válida
        calificacion = input("Ingrese la calificación (entero entre 1 y 10): ").strip()
        if validar_calificacion(calificacion, permitir_blanco):
            return int(calificacion) if calificacion else None  # Retorna la calificación si es válida
        else:
            print("Calificación no válida. Debe ser un número entero entre 1 y 10. Intente nuevamente.")


def validar_estado(estado):
    # Lista de estados válidos
    estados_validos = {"en curso", "pendiente", "terminada"}
    # Verifica si el estado ingresado está en la lista de estados válidos
    return estado.lower() in estados_validos

def obtener_estado():
    while True:  # Bucle infinito hasta recibir un estado válido
        estado = input("Ingrese el estado (en curso, pendiente, o terminada): ").strip().lower()
        if validar_estado(estado):
            return estado  # Retorna el estado si es válido
        else:
            print("Estado no válido. Debe ser 'en curso', 'pendiente' o 'terminada'. Intente nuevamente.")


def obtener_titulo_pelicula(contenindo_peliculas, pelicula_id):
    for pelicula in contenindo_peliculas:
        if pelicula[0] == pelicula_id:
            return pelicula[1]  # El título está en la columna 1
    return None  # No se encontró el ID

def validar_pelicula_id(contenido_peliculas):
    pelicula_id = input("Ingrese el ID de la película/serie: ")  # El ID se ingresa como cadena

    # Verificar si el ID es un número válido y si la película existe
    while not pelicula_id.isdigit() or obtener_titulo_pelicula(contenido_peliculas, int(pelicula_id)) is None:
        if not pelicula_id.isdigit():
            print("Error: El ID debe ser un número válido. Intente nuevamente.")
        else:
            print("Error: El ID de la película/serie no existe. Intente nuevamente.")
        pelicula_id = input("Ingrese el ID de la película/serie: ")

    return int(pelicula_id)  # Convertimos a entero solo después de validar


def obtener_apellido_usuario(contenido_usuarios, usuario_id):
    for usuario in contenido_usuarios:
        if usuario[0] == usuario_id:
            return usuario[2]  # El apellido está en la columna 2
    return None  # No se encontró el ID

def validar_usuario_id(contenido_usuarios):
    usuario_id = input("Ingrese el ID del usuario: ")  # El ID se ingresa como cadena

    # Verificar si el ID es un número válido y si el usuario existe
    while not usuario_id.isdigit() or obtener_apellido_usuario(contenido_usuarios, int(usuario_id)) is None:
        if not usuario_id.isdigit():
            print("Error: El ID debe ser un número válido. Intente nuevamente.")
        else:
            print("Error: El ID del usuario no existe. Intente nuevamente.")
        usuario_id = input("Ingrese el ID del usuario: ")

    return int(usuario_id)  # Convertimos a entero solo después de validar


#Otros
def validar_actualizacion(primera_consulta=True):
    while True:
        if primera_consulta:
            respuesta = input("\n¿Desea actualizar contenido? (s/n): ").strip().lower()
        else:
            respuesta = input("\n¿Desea continuar? (s/n): ").strip().lower()
        
        if respuesta in ['s', 'n']:
            return respuesta
        else:
            print("Entrada no válida. Por favor, ingrese 's' o 'n'.")


def validar_eliminacion(primera_consulta=True):
    while True:
        if primera_consulta:
            respuesta = input("\n¿Desea eliminar contenido? (s/n): ").strip().lower()
        else:
            respuesta = input("\n¿Desea continuar? (s/n): ").strip().lower()
        
        if respuesta in ['s', 'n']:
            return respuesta
        else:
            print("Entrada no válida. Por favor, ingrese 's' o 'n'.")
