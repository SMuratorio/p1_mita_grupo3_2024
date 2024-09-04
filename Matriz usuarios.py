#Matriz usuarios

def crear_contenido_usuarios(contenido_usuarios, proximo_id_usuarios, nombre, apellido, dni, correo):
    item = [proximo_id_usuarios, nombre, apellido, dni, correo]

    contenido_usuarios.append(item)

    print(f"El usuario {nombre} {apellido} con el DNI '{dni}' creado con ID {proximo_id_usuarios}.")

    return contenido_usuarios

def leer_contenido_usuarios(contenido_usuarios):
    if not contenido_usuarios:
        print("No hay contenido disponible.")
        return
    
    for item in contenido_usuarios:
        proximo_id_usuarios, nombre, apellido, dni, correo = item
        print(f"ID: {proximo_id_usuarios}")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"DNI: {dni}")
        print(f"Correo: {correo}")
        print("-" * 30)

def actualizar_contenido_usuarios(contenido_usuarios, item_id_usuarios, nombre=None, apellido=None, dni=None, correo=None):
    for item in contenido_usuarios:
        if item[0] == item_id_usuarios:
            item[1] = nombre if nombre is not None and nombre != '' else item[1]
            item[2] = apellido if apellido is not None and apellido != '' else item[2]
            item[3] = dni if dni is not None and dni != '' else item[3]
            item[4] = correo if correo is not None and correo != '' else item[4]
            print(f"{item[1]}{item[2]} con ID {item_id_usuarios} actualizada.")
            return
    print(f"No se encontró el contenido con ID {item_id_usuarios}.")

def eliminar_contenido_usuarios(contenido_usuarios, item_id_usuarios):
    for item in contenido_usuarios:
        if item[0] == item_id_usuarios:
            contenido_usuarios.remove(item)
            print(f"El {item[2]} con ID {item_id_usuarios} ha sido eliminado.")
            return
    print(f"No se encontró el contenido con ID {item_id_usuarios}.")

def crear_matriz_usuarios(n, m):
    """
    pre: recibe n y m. Donde n: filas y m:columnas
    pos: devuelve una matriz de NxM creada con ceros
    
    """
    """return [[0]*m for fil in range (n)]"""
    return [[0]*m for _ in range(n)]

def llenar_matriz_usuarios(m, usuarios_ordenados):
    """
    Pre: Recibe una matriz ya creada y una lista 'contenido' que contiene otras listas.
    Pos: Llena la matriz con los valores de la lista 'contenido'.
    """
    for i in range(len(usuarios_ordenados)):
        for j in range(len(usuarios_ordenados[i])):
            m[i][j] = usuarios_ordenados[i][j]

def imprimir_matriz_usuarios(matriz, ids_usuarios, encabezado_usuarios):
    """
    Pre: Recibe una matriz ya creada.
    Pos: Muestra por consola los elementos de la matriz.
    """
    # Imprimir el encabezado
    print(" " * 12, end="")  # Espacio para alinear
    for i in encabezado_usuarios:
        print(f"{i:>20}", end="") 
    print()   

    # Imprimir cada fila 
    for i in range(len(matriz)):
        print(f"{ids_usuarios[i]:<12}", end="")
        for j in range(len(matriz[i])):
            valor = str(matriz[i][j]).capitalize() #mayuscula en la 1er letra
            print(f"{valor:>20}", end="")
        print()


contenido_usuarios = []
proximo_id_usuarios = 1
seguir = 0

while seguir == 0:
    nombre = input("Ingrese el nombre del usuario: ")
    apellido=input("Ingrese el apellido del usuario: ")
    dni = input("Ingrese el DNI del usuario: ")
    correo = input("Ingrese su correo electronico: ")
    
    conteni = crear_contenido_usuarios(contenido_usuarios, proximo_id_usuarios, nombre, apellido, dni, correo)
    proximo_id_usuarios+=1
    
    seguir = int(input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
    
    if seguir == -1:
        seguir = -1

# PROGRAMA PRINCIPAL

print("\nContenido registrado:")
leer_contenido_usuarios(contenido_usuarios)

# Preguntar si se desea actualizar contenido
actualizar_opcion_usuarios = input("\n¿Desea actualizar contenido? (s/n): ").lower()

while actualizar_opcion_usuarios == 's':
    print("\nActualizar contenido:")

    nuevo_id_usuarios = int(input("Ingrese el ID del usuario a cambiar: "))
    print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

    nuevo_nombre = input("Nuevo nombre (deje en blanco para no cambiar): ")
    nuevo_apellido = input("Nuevo apellido (deje en blanco para no cambiar): ")
    nuevo_dni_str = (input("Nuevo DNI (deje en blanco para no cambiar): "))
    nuevo_correo = input("Nuevo correo (deje en blanco para no cambiar): ")

    #Convertir nuevo año a entero si no está vacío
    nuevo_dni = int(nuevo_dni_str) if nuevo_dni_str else None

    actualizar_contenido_usuarios(contenido_usuarios, nuevo_id_usuarios, nombre=nuevo_nombre, apellido=nuevo_apellido, dni=nuevo_dni, correo=nuevo_correo)

    print("\nContenido actualizado:")
    leer_contenido_usuarios(contenido_usuarios)
    
    # Preguntar si se desea seguir actualizando
    actualizar_opcion_usuarios = input("\n¿Desea seguir actualizando contenido? (s/n): ").lower()

# Preguntar si se desea eliminar contenido
eliminar_opcion_usuarios = input("\n¿Desea eliminar contenido? (s/n): ").lower()

while eliminar_opcion_usuarios == 's':
    print("\nEliminar contenido:")

    eliminar_id_usuarios = int(input("Ingrese el ID del usuario a eliminar: "))
    eliminar_contenido_usuarios(contenido_usuarios, eliminar_id_usuarios)

    print("\nContenido después de la eliminación:")
    leer_contenido_usuarios(contenido_usuarios)
    
    # Preguntar si se desea seguir eliminando
    eliminar_opcion_usuarios = input("\n¿Desea seguir eliminando contenido? (s/n): ").lower()

print("\nProceso finalizado.")

#Recortar los títulos a un máximo de 8 caracteres
for i in range(len(contenido_usuarios)):
    contenido_usuarios[i][1] = contenido_usuarios[i][1][:8]  #Recortar el nombre a 8 caracteres

#Ordenar la matriz por orden alfabetico en base al nombre
usuarios_ordenados = sorted(contenido_usuarios, key=lambda x: x[1])

#crear matriz
matriz = crear_matriz_usuarios (len(contenido_usuarios),5)

#llenar matriz
llenar_matriz_usuarios(matriz, usuarios_ordenados)

#imprimir matriz
ids_usuarios=[item[1] for item in usuarios_ordenados]  # Nombres de los usuarios
encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Atributos de cada contenido

imprimir_matriz_usuarios(matriz, ids_usuarios, encabezado_usuarios)