import validar, menu

def crear_matriz_usuarios(matriz_usuarios):
    opcion_seleccionada = validar.obtener_opcion()

    while opcion_seleccionada == "s":
        print("\nAgregar usuario:")
        nombre = validar.obtener_nombre()
        apellido = validar.obtener_apellido()
        dni = validar.obtener_dni()
        correo = validar.obtener_email()
        proximo_id_usuario = len(matriz_usuarios)+1

        print(f"El usuario {nombre} {apellido} con el DNI '{dni}' creado con ID {proximo_id_usuario}.")

        sublista = [proximo_id_usuario, nombre, apellido, dni, correo] #Empaquetado
        matriz_usuarios.append(sublista)
        print("\nUsuario agregado con éxito.")

        opcion_seleccionada = validar.obtener_opcion(primera_consulta=False)
        
def leer_matriz_usuarios(matriz_usuarios):
    if not matriz_usuarios:
        print("No hay contenido disponible.")
        print()
        return
    
    print("\nContenido registrado:")
    for fila in matriz_usuarios:
        proximo_id_usuario, nombre, apellido, dni, correo = fila #Desempaquetado
        print(f"ID: {proximo_id_usuario}")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"DNI: {dni}")
        print(f"Correo: {correo}")
        print("-" * 30)

def actualizar_matriz_usuarios(matriz_usuarios):
    opcion_seleccionada = validar.obtener_opcion()
  
    while opcion_seleccionada == 's':
        id_usuario = input("Ingrese el ID del usuario a actualizar: ").strip()
        while not id_usuario.isdigit() or not validar.si_existe_id(int(id_usuario), matriz_usuarios):
            id_usuario = validar.manejar_error("ID no válido. Reintentando...", lambda: input("Ingrese un ID válido: "))
        
        id_usuario = int(id_usuario)

        dic_usuario_actualizar = obtener_usuario(id_usuario, matriz_usuarios)
        opcion_actualizar = menu.mostrar_submenu_actualizar(list(dic_usuario_actualizar.keys()))
        nuevo_valor = input(f"Ingrese el nuevo {opcion_actualizar}, valor anterior {dic_usuario_actualizar[opcion_actualizar]}: ")
        dic_usuario_actualizar[opcion_actualizar] = nuevo_valor
        actualizar_usuario(id_usuario, matriz_usuarios, dic_usuario_actualizar)
        print(f"{nuevo_valor} con ID {id_usuario} ha sido actualizado.")
        opcion_seleccionada = validar.obtener_opcion(False)

def obtener_usuario(id_usuario, matriz_usuarios):
    for fila in matriz_usuarios:
        if fila[0] == id_usuario:
            return {"Nombre":fila[1], "Apellido": fila[2], "D.N.I": fila[3], "Correo": fila[4]}

def actualizar_usuario(id_usuario, matriz_usuarios, usuario_actualizar):
    for fila in matriz_usuarios:
        if fila[0] == id_usuario:
            fila[1] = usuario_actualizar["Nombre"]
            fila[2] = usuario_actualizar["Apellido"]
            fila[3] = usuario_actualizar["D.N.I"]
            fila[4] = usuario_actualizar["Correo"]
            return

def eliminar_matriz_usuarios(matriz_usuarios):
    opcion_seleccionada = validar.obtener_opcion()
    
    while opcion_seleccionada == 's':
        print("\nEliminar contenido:")
        id_usuario = input("Ingrese el ID del usuario a eliminar: ").strip()

        while not id_usuario.isdigit() or not validar.si_existe_id(int(id_usuario), matriz_usuarios):
            if not id_usuario.isdigit():
                print("Por favor, ingrese un número válido.")
            else:
                print("ID no encontrado. Por favor, ingrese un ID válido.")
            id_usuario = input("Ingrese el ID del usuario a eliminar: ").strip()
        
        id_usuario = int(id_usuario)
        
        # Eliminar el usuario
        matriz_usuarios[:] = [fila for fila in matriz_usuarios if fila[0] != id_usuario] 
        #[:] evita la creación de una nueva lista y modifica la lista existente.
        print(f"El usuario con ID {id_usuario} ha sido eliminado.")
        
        opcion_seleccionada = validar.obtener_opcion(primera_consulta=False)

def imprimir_matriz_usuarios(matriz_usuarios):
    len_matriz_usuarios=len(matriz_usuarios)
    for encabezado in range(len_matriz_usuarios):
        matriz_usuarios[encabezado][1] = matriz_usuarios[encabezado][1][:8]  # Recortar el nombre a 8 caracteres
                    
    matriz_usuarios_ordenados = sorted(matriz_usuarios, key=lambda fila: fila[2])# Ordenar la lista por apellido
    encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Atributos de cada contenido

    # Imprimir el encabezado
    for encabezado in encabezado_usuarios: #recorre cada uno de los elementos de la lista 
        print(f"{encabezado:<25}", end="") #mprime i con un mínimo de 25 espacios y alinéalo a la derecha
    print()   

    # Imprimir cada fila 
    for encabezado in range(len_matriz_usuarios): #devuelve el número de filas
        for j in range(len(matriz_usuarios_ordenados[encabezado])): #recorre las columnas de cada usuario
            valor = str(matriz_usuarios_ordenados[encabezado][j]).capitalize() #mayuscula en la 1er letra
            print(f"{valor:<25}", end="") #Imprime cada valor con un ancho de 25 caracteres, alineado a la derecha (:>25)
        print()
        
    print()

def listar_matriz_usuarios(matriz_usuarios):
    print("\nContenido registrado:")
    matriz_usuarios_ordenados = sorted(matriz_usuarios, key=lambda fila: fila[2]) # Ordenar la lista por apellido
    encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Empaquetado
    matriz_dic_usuarios = [dict(zip(encabezado_usuarios, fila)) for fila in matriz_usuarios_ordenados] #La combierte a diccionario
    for fila in matriz_dic_usuarios: # Imprimir los diccionarios
        print(fila)
    print()
