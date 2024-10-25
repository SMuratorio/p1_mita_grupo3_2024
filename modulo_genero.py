import json, modulo_validar

dic_genero={
     0: "Otro",
     1:"Fantasía", 
     2:"Drama",
     3:"Ciencia ficción",
     4: "Terror",
     5: "Acción",
     6: "Histórico",
     7: "Crimen"}

def imprimir_generos_con_definicion(dic_genero):
    definiciones = leer_definiciones("genero.txt")  # Leer las definiciones desde el archivo
    print("\nLista de géneros disponibles con definiciones:")
    for clave, genero in dic_genero.items():
        definicion = definiciones.get(genero, "Definición no disponible")
        print(f"{clave}: {genero} - {definicion}")

def leer_definiciones(arch):
    with open(arch, "r", encoding="UTF-8") as file:
        return {clave.strip(): valor.strip() for linea in file if ':' in linea for clave, valor in [linea.split(':', 1)]}
    
def seleccionar_genero(dic, mensaje_input, funcion_validacion):
    while True:
        imprimir_generos_con_definicion(dic)  # Mostrar los géneros actuales
        try:
            opcion = int(input(f"{mensaje_input} (Ingrese 0 para agregar un nuevo género): ").strip()) 
            if opcion == 0: 
                nuevo_genero = input("Ingrese el nuevo género: ").strip().capitalize()
                while not nuevo_genero:  # Validar que el nuevo género no esté vacío
                    nuevo_genero=input("El género no puede estar vacío. Por favor, ingrese un género válido: ").strip().capitalize()
                
                agregar_genero(dic, nuevo_genero)  # Agregar el nuevo género al diccionario

            elif opcion in dic:
                return dic[opcion]  # Retorna el género si la opción existe en el diccionario
            else:
                print(f"No existe un género con el número {opcion}. Por favor, ingrese un número válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def agregar_genero(dic, nuevo_genero): #Agrega un nuevo género al diccionario con una nueva clave, validando el género ingresado.
    if modulo_validar.validar_genero(nuevo_genero):  # Validar el nuevo género
        nueva_clave = max(dic.keys()) + 1  # Obtener la nueva clave incrementando la más alta
        dic[nueva_clave] = nuevo_genero  # Agregar el nuevo género al diccionario
        nueva_definicion = obtener_definicion()
        
        with open("genero.txt", "a", encoding="UTF-8") as archivo:
            archivo.write(f"{nuevo_genero}: {nueva_definicion}\n")
        
        print(f"Género '{nuevo_genero}' agregado con clave {nueva_clave}.")
        guardar_generos_en_json(dic_genero, "genero.txt", "definiciones_generos.json")
    else:
        print("El género ingresado no es válido.")

def obtener_definicion(): #Solicita y valida la definición del nuevo género.
    while True:
        definicion = input("Ingrese la definición del nuevo género: ").strip().capitalize()
        if definicion:
            return definicion
        print("La definición no puede estar vacía. Por favor, ingrese una definición válida.")

def guardar_generos_en_json(dic_genero, archivo_definiciones, archivo_json):#Genera un archivo JSON con los géneros y sus definiciones.
    definiciones = leer_definiciones(archivo_definiciones)
    resultado = {genero: definiciones.get(genero) for genero in dic_genero.values()}
    
    with open(archivo_json, "w", encoding="UTF-8") as archivo:
        json.dump(resultado, archivo, ensure_ascii=False, indent=4)
        