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

def guardar_json(data):
    """Guarda el diccionario en un archivo JSON."""
    try:
        with open(archivo_json, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError:
        print("Error al guardar el archivo JSON.")

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
   
    if genero in dic_genero.values():
        claves_a_actualizar = [k for k, v in dic_genero.items() if v == genero]
        if claves_a_actualizar:
            clave_a_actualizar = claves_a_actualizar[0]  # Obtener la primera clave

            nueva_descripcion = input("Ingrese la nueva definición: ").capitalize()

            definiciones = cargar_json()
            definiciones[genero] = nueva_descripcion
            guardar_json(definiciones)
            print(f"Género '{genero}' actualizado.")
    else:
        print(f"Género '{genero}' no encontrado en el diccionario.")

def leer_genero(genero):
    json_data = cargar_json()
    print(f"{genero}: {json_data.get(genero, 'Género no encontrado.')}")

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
