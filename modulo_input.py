import modulo_validar, modulo_varios, modulo_genero
from tkinter import simpledialog, messagebox

def obtener_dinamico_tk(mensaje_input, mensaje_error, validador, capitalizar=True):
    while True:
        dato = simpledialog.askstring("Entrada de datos", mensaje_input)
        if dato:
            dato = dato.strip()
            if capitalizar:
                dato = dato.capitalize()
            if validador(dato):
                return dato
            else:
                messagebox.showerror("Error", mensaje_error)
        else:
            return None  # En caso de que el usuario cierre la ventana de entrada

def obtener_unico_tk(mensaje_input, mensaje_error_unico, mensaje_error_validacion, validar_funcion, existentes):
    while True:
        nuevo_valor = simpledialog.askstring("Entrada de datos", mensaje_input)
        if nuevo_valor:
            nuevo_valor = nuevo_valor.strip()
            if nuevo_valor in existentes:
                messagebox.showerror("Error", mensaje_error_unico)
            elif not validar_funcion(nuevo_valor):
                messagebox.showerror("Error", mensaje_error_validacion)
            else:
                existentes.add(nuevo_valor)
                return nuevo_valor
        else:
            return None

def obtener_usuario_tk(dnis_existentes, correos_existentes):
    nuevo_nombre = obtener_dinamico_tk("Ingrese el nombre del usuario: ", "Nombre de usuario no válido. ", modulo_validar.validar_strings)
    if not nuevo_nombre:
        return None  # Si el usuario cierra la ventana o no ingresa el dato, se sale de la función

    nuevo_apellido = obtener_dinamico_tk("Ingrese el apellido del usuario: ", "Apellido de usuario no válido. ", modulo_validar.validar_strings)
    if not nuevo_apellido:
        return None

    nuevo_dni = obtener_unico_tk("Ingrese el DNI del usuario (con puntos, formato XX.XXX.XXX): ", "El DNI ingresado ya existe. Por favor, ingrese un DNI único.", 
                                 "El DNI ingresado no es válido. Intente nuevamente.", modulo_validar.validar_dni, dnis_existentes)
    if not nuevo_dni:
        return None

    nuevo_mail = obtener_unico_tk("Ingrese el correo electrónico: ", "El correo ya existe. Por favor, ingrese un correo único.", 
                                  "El correo ingresado no es válido. Intente nuevamente.", modulo_validar.validar_email, correos_existentes)
    if not nuevo_mail:
        return None

    return (nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_mail)

def obtener_dinamico(mensaje_input, mensaje_output, funcion_validacion, capitalizar=True):
    while True:
        dato = input(mensaje_input).strip()
        if capitalizar:
            dato=dato.capitalize()
        if funcion_validacion(dato):
            return dato
        else:
            print(mensaje_output) 

def obtener_unico(mensaje_input, mensaje_error_unico, mensaje_error_validacion, validar_funcion, existentes, es_pelicula_serie=False): #para correos y dnis
    while True:
        nuevo_valor = input(mensaje_input).strip()
        
        if es_pelicula_serie:
            nuevo_valor = modulo_varios.capitalizar_titulo(nuevo_valor)

        if nuevo_valor in existentes:
            print(mensaje_error_unico)
        elif not validar_funcion(nuevo_valor):
            print(mensaje_error_validacion)
        else:
            existentes.add(nuevo_valor)
            return nuevo_valor

def obtener_pelicula(titulos_existentes):
    nuevo_titulo = obtener_unico("Ingrese el titulo: ", "El titulo ya existe. Por favor, ingrese un título único.", 
                                 "El titulo ingresado no es válido. Intente nuevamente.", modulo_validar.validar_titulo, titulos_existentes, es_pelicula_serie=True)
    nuevo_tipo = obtener_dinamico("Ingrese el tipo (serie/película): ", "Entrada no válida. Por favor, ingrese 'serie' o 'película'.", 
                                  modulo_validar.validar_tipo, capitalizar=False)
    nuevo_genero =modulo_genero.seleccionar_genero()
    nuevo_anio = obtener_dinamico("Ingrese el año de estreno (formato YYYY): ", "Año no válido. Intente nuevamente.", modulo_validar.validar_anio)
    nueva_duracion = None
    if nuevo_tipo in ['película', 'pelicula']: 
        nueva_duracion = obtener_dinamico("Ingrese la duración de la película (en minutos): ", "Duración no válida. Por favor, ingrese un número entero positivo.", modulo_validar.validar_duracion) + " minutos"
    elif nuevo_tipo == 'serie':
        nueva_duracion = obtener_dinamico("Ingrese la cantidad de temporadas: ", "Cantidad no válida. Por favor, ingrese un número entero positivo.", modulo_validar.validar_duracion) + " temporadas"
    return (nuevo_titulo, nuevo_tipo, nuevo_genero, nuevo_anio, nueva_duracion) #Uso de tupla

def obtener_registro():
    nuevo_estado = obtener_dinamico("Ingrese el estado (en curso, pendiente, o terminada): ", "Estado no válido. Debe ser 'en curso', 'pendiente' o 'terminada'. Intente nuevamente.", modulo_validar.validar_estado)
    nueva_calificacion = obtener_dinamico("Ingrese la calificación (entero entre 1 y 10): ", "Calificación no válida. Debe ser un número entero entre 1 y 10. Intente nuevamente.", modulo_validar. validar_calificacion) if nuevo_estado.lower() == "terminada" else 0
    return (nuevo_estado, nueva_calificacion) #Uso de tupla

def obtener_id_dinamico(mensaje_input, mensaje_output, funcion_validacion, parametros): #para obtener_id ya sea para actualizar o eliminar
    while True:
        dato = input(mensaje_input).strip(). lower()
        if funcion_validacion(dato, parametros):
            return dato
        else:
            print(mensaje_output)

def obtener_id(matriz, tipo_contenido): #Para actualizar o eliminar un determinado ID
    id = obtener_id_dinamico(f"Ingrese el ID de {tipo_contenido}: ", "ID no válido. Reintentando...", modulo_validar.validar_id, {"matriz": matriz})
    return id

def obtener_nuevo_valor(opcion_actualizar, dic_actualizar, validadores): #para actualizar datos de las tres matrices
    nuevo_valor = input(f"Ingrese el nuevo {opcion_actualizar}, valor anterior {dic_actualizar[opcion_actualizar]}: ")
    while not validadores[opcion_actualizar](nuevo_valor): #se accede a validadores a la opcion que se quiere actualizar con el nuevo valor
        nuevo_valor = input(f"Dato no válido o {opcion_actualizar} existente. Ingrese un nuevo {opcion_actualizar}: ")
    return nuevo_valor
    