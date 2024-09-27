import validar

def crear_contenido_usuarios(matriz_usuarios):
    agregar_usuario=validar.validar_continuacion()
    while agregar_usuario=="s":
        proximo_id_usuarios=len(matriz_usuarios)+1
        print("\nAgregar usuario:")
        nombre=validar.obtener_nombre()
        apellido=validar.obtener_apellido()
        dni = validar.obtener_dni()
        correo = validar.obtener_email()

        print(f"El usuario {nombre} {apellido} con el DNI '{dni}' creado con ID {proximo_id_usuarios}.")

        item = [proximo_id_usuarios, nombre, apellido, dni, correo]
        matriz_usuarios.append(item)

        agregar_usuario=validar.validar_continuacion(primera_consulta=False)

def leer_contenido_usuarios(contenido_usuarios):
    if not contenido_usuarios:
        print("No hay contenido disponible.")
        print()
        return
    
    for item in contenido_usuarios:
        proximo_id_usuarios, nombre, apellido, dni, correo = item
        print(f"ID: {proximo_id_usuarios}")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"DNI: {dni}")
        print(f"Correo: {correo}")
        print("-" * 30)

def actualizar_contenido_usuarios(contenido_usuarios):
    actualizar_usuario=validar.validar_continuacion()
  
    while actualizar_usuario == 's':
        actualizar_id_usuario = input("Ingrese el ID del usuario a actualizar: ").strip()
        while not actualizar_id_usuario.isdigit() or not validar.si_existe_id(int(actualizar_id_usuario), contenido_usuarios):
            actualizar_id_usuario = validar.manejar_error("ID no válido. Reintentando...", lambda: input("Ingrese un ID válido: "))
        
        actualizar_id_usuario = int(actualizar_id_usuario)

        for item in contenido_usuarios:
            if item[0] == actualizar_id_usuario:
                print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")
                def validar_dato(dato, funcion_validar, obtener_funcion, actual):
                    return validar.manejar_error(f"{dato} no válido. Reintentando...", obtener_funcion) if dato and not funcion_validar(dato) else dato or actual

                nuevo_nombre = validar_dato(input("Nuevo nombre: ").strip().capitalize(), validar.validar_strings, validar.obtener_nombre, item[1])
                nuevo_apellido = validar_dato(input("Nuevo apellido: ").strip().capitalize(), validar.validar_strings, validar.obtener_apellido, item[2])
                nuevo_dni = validar_dato(input("Nuevo DNI: ").strip(), validar.validar_dni, validar.obtener_dni, item[3])
                nuevo_correo = validar_dato(input("Nuevo correo: ").strip(), validar.validar_email, validar.obtener_email, item[4])

                item[1], item[2], item[3], item[4] = nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_correo
                print(f"{nuevo_nombre} {nuevo_apellido} con ID {actualizar_id_usuario} ha sido actualizado.")
                actualizar_usuario = validar.validar_continuacion(primera_consulta=False)
                
                return

def eliminar_contenido_usuarios(contenido_usuarios):
    eliminar_usuario = validar.validar_continuacion()
    
    while eliminar_usuario == 's':
        print("\nEliminar contenido:")
        eliminar_id_usuarios = input("Ingrese el ID del usuario a eliminar: ").strip()

        while not eliminar_id_usuarios.isdigit() or not validar.si_existe_id(int(eliminar_id_usuarios), contenido_usuarios):
            if not eliminar_id_usuarios.isdigit():
                print("Por favor, ingrese un número válido.")
            else:
                print("ID no encontrado. Por favor, ingrese un ID válido.")
            eliminar_id_usuarios = input("Ingrese el ID del usuario a eliminar: ").strip()
        
        eliminar_id_usuarios = int(eliminar_id_usuarios)
        
        # Eliminar el usuario
        contenido_usuarios[:] = [item for item in contenido_usuarios if item[0] != eliminar_id_usuarios] 
        #[:] evita la creación de una nueva lista y modifica la lista existente.
        print(f"El usuario con ID {eliminar_id_usuarios} ha sido eliminado.")
        
        eliminar_usuario = validar.validar_continuacion(primera_consulta=False)

def imprimir_matriz_usuarios(contenido_usuarios):
    for i in range(len(contenido_usuarios)):
        contenido_usuarios[i][1] = contenido_usuarios[i][1][:8]  # Recortar el nombre a 8 caracteres
                    
    usuarios_ordenados = sorted(contenido_usuarios, key=lambda x: x[2])# Ordenar la lista por apellido

    ids_usuarios = [item[1] for item in usuarios_ordenados]  # Nombres de los usuarios
    encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Atributos de cada contenido

    # Imprimir el encabezado
    print(" " * 12, end="")  # Espacio para alinear
    for i in encabezado_usuarios: #recorre cada uno de los elementos de la lista 
        print(f"{i:>25}", end="") #mprime i con un mínimo de 25 espacios y alinéalo a la derecha
    print()   

    # Imprimir cada fila 
    for i in range(len(usuarios_ordenados)): #devuelve el número de filas
        print(f"{ids_usuarios[i]:<12}", end="") #imprime el ID del usuario desde ids_usuarios, alineándolo a la izquierda con 12 espacios (:<12), para mantener la alineación con los encabezados.
        for j in range(len(usuarios_ordenados[i])): #recorre las columnas de cada usuario
            valor = str(usuarios_ordenados[i][j]).capitalize() #mayuscula en la 1er letra
            print(f"{valor:>25}", end="") #Imprime cada valor con un ancho de 25 caracteres, alineado a la derecha (:>25)
        print()
