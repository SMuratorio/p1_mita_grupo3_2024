import modulo_validar

def crear_contenido_usuarios(contenido_usuarios, proximo_id_usuarios, nombre, apellido, dni, correo):
    item = [proximo_id_usuarios, nombre, apellido, dni, correo]

    contenido_usuarios.append(item)

    print(f"El usuario {nombre} {apellido} con el DNI '{dni}' creado con ID {proximo_id_usuarios}.")

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

def eliminar_contenido_usuarios(contenido_usuarios):
    while True:
        eliminar_id_usuarios = input("Ingrese el ID del usuario a eliminar: ").strip()

        # Verifica si el ID es un número
        if eliminar_id_usuarios.isdigit():
            eliminar_id_usuarios = int(eliminar_id_usuarios)
            # Verifica si el ID existe en el contenido
            if modulo_validar.si_existe_id_usuario(eliminar_id_usuarios, contenido_usuarios):
                # Proceder a eliminar el contenido con el ID válido
                for item in contenido_usuarios:
                    if item[0] == eliminar_id_usuarios:
                        contenido_usuarios.remove(item)
                        print(f"El usuario con ID {eliminar_id_usuarios} ha sido eliminado.")
                        return  # Sale de la función después de eliminar
            else:
                print(f"ID no encontrado. Por favor, ingrese un ID válido.")
        else:
            print("Por favor, ingrese un número válido.")  # Mensaje si el input no es numérico

def imprimir_matriz_usuarios(usuarios_ordenados, ids_usuarios, encabezado_usuarios):
    """
    Pre: Recibe una matriz ya creada.
    Pos: Muestra por consola los elementos de la matriz.
    """
    # Imprimir el encabezado
    print(" " * 12, end="")  # Espacio para alinear
    for i in encabezado_usuarios: 
        print(f"{i:>25}", end="") 
    print()   

    # Imprimir cada fila 
    for i in range(len(usuarios_ordenados)): 
        print(f"{ids_usuarios[i]:<12}", end="") 
        for j in range(len(usuarios_ordenados[i])): 
            valor = str(usuarios_ordenados[i][j]).capitalize() 
            print(f"{valor:>25}", end="") 
        print()