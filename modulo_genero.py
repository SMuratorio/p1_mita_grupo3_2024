import json, modulo_validar, modulo_menu

dic_genero = {
    0: "Otro",
    1: "Fantasía", 
    2: "Drama",
    3: "Ciencia ficción",
    4: "Terror",
    5: "Acción",
    6: "Histórico",
    7: "Crimen",
    8: "Comedia",
    9: "Misterio",
    10: "Animación"}

archivo_json = 'definiciones_generos.json'

def cargar_json():
    """Carga el archivo JSON y maneja errores."""
    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo JSON no fue encontrado. Se utilizará un diccionario vacío.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Se utilizará un diccionario vacío.")
        return {}
    except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

def seleccionar_genero():
    opcion=modulo_validar.obtener_opcion()
    while opcion=='s':
        json_data = cargar_json()  # Cargar descripciones desde JSON
        print("Seleccione un género:")
        for clave, genero in dic_genero.items(): #clave: nro de cada genero 
            descripcion = json_data.get(genero, "Descripción no disponible.")  # Obtener la descripción
            print(f"{clave}: {genero} - {descripcion}")  # Mostrar género con descripción

        seleccion = input("Ingrese el número del género: ")

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if seleccion == 0:
                modulo_menu.submenu_genero()
            elif seleccion in dic_genero:
                opcion='n'
            else:
                print("Selección no válida. Intente de nuevo.")
        else:
            print("Entrada no válida. Debe ser un número.")
    return genero
    
def agregar_genero():
    nuevo_genero = input("Ingrese el nuevo género: ").strip().capitalize()
    
    if nuevo_genero in dic_genero.values():
        print("Este género ya existe en el diccionario.")
        return  # Salimos si el género ya existe

    if modulo_validar.validar_genero(nuevo_genero):
        nueva_clave = max(dic_genero.keys()) + 1
        dic_genero[nueva_clave] = nuevo_genero
        
        definicion = ""
        while not definicion:
            definicion = input("Ingrese la definición del nuevo género: ").strip().capitalize()
            if not definicion:
                print("La definición no puede estar vacía. Por favor, ingrese una definición válida.")

        definiciones = cargar_json()
        definiciones[nuevo_genero] = definicion
        guardar_json(definiciones)
        print(f"Género '{nuevo_genero}' agregado con clave {nueva_clave}.")
    else:
        print("El género ingresado no es válido.")

def actualizar_genero():
    genero = input("Ingrese el nombre del género a actualizar: ").capitalize()
   
     # Buscar la clave asociada al género
    clave_a_actualizar = None
    for clave, valor in dic_genero.items():
        if valor == genero:
            clave_a_actualizar = clave
            # dejamos que el ciclo continúe, pero ya tenemos la clave

    if clave_a_actualizar is not None:  # Verificar si el género existe
        nueva_descripcion = ""
        while not nueva_descripcion.strip():  # Validar que no esté vacío o solo espacios
            nueva_descripcion = input("Ingrese la nueva definición: ").capitalize()
            if not nueva_descripcion.strip():
                print("La definición no puede estar vacía. Intente nuevamente.")
        
        definiciones = cargar_json()
        definiciones[genero] = nueva_descripcion
        guardar_json(definiciones)
        print(f"Género '{genero}' actualizado.")
    else:
        print(f"Género '{genero}' no encontrado en el diccionario.")

def eliminar_genero():
    genero = input("Ingrese el nombre del género a eliminar: ").capitalize()
    
    if genero in dic_genero.values():
        for clave, valor in dic_genero.items(): # Encontrar la clave del género a eliminar
            if valor == genero:
                dic_genero.pop(clave)  # Elimina del diccionario
                
                json_data = cargar_json() # Cargar las definiciones desde el archivo JSON
                
                if genero in json_data:
                    json_data.pop(genero)  # Elimina directamente la entrada del JSON
                    guardar_json(json_data)  # Guarda los cambios en el archivo JSON
                    print(f"Género '{genero}' eliminado.")
                else:
                    print(f"Género '{genero}' no encontrado en el archivo JSON.")
                return  # Salir de la función después de eliminar
    else:
        print(f"Género '{genero}' no existe en el diccionario.")

def guardar_json(data):
    """Guarda el diccionario en un archivo JSON."""
