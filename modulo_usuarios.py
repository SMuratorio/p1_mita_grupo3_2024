import modulo_validar, modulo_menu, modulo_input, modulo_varios

def crear_matriz_usuarios(matriz_usuarios, dnis_existentes, correos_existentes):
    opcion_seleccionada = modulo_validar.obtener_opcion()

    while opcion_seleccionada == "s":
        print("\nAgregar usuario:")
        nombre, apellido, dni, correo = modulo_input.obtener_usuario(dnis_existentes, correos_existentes)
        proximo_id_usuario = len(matriz_usuarios)+1

        print(f"El usuario {nombre} {apellido} con el DNI '{dni}' creado con ID {proximo_id_usuario}.")

        sublista = [proximo_id_usuario, nombre, apellido, dni, correo] #Empaquetado
        matriz_usuarios.append(sublista)
        print("\nUsuario agregado con éxito.")

        opcion_seleccionada = modulo_validar.obtener_opcion(primera_consulta=False)
        
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

def actualizar_matriz_usuarios(matriz_usuarios, dnis_existentes, correos_existentes):
    opcion_seleccionada = modulo_validar.obtener_opcion()
     
    while opcion_seleccionada == 's':
        id_usuario = int(modulo_input.obtener_id(matriz_usuarios, "usuario"))
        dic_usuario_actualizar = obtener_usuario(id_usuario, matriz_usuarios)
        opcion_actualizar = modulo_menu.mostrar_submenu_actualizar(list(dic_usuario_actualizar.keys())) #convierte las claves en lista
        # Llamada a la nueva función para validar y actualizar el valor
        dic_usuario_actualizar = validar_y_actualizar_usuarios(opcion_actualizar,dic_usuario_actualizar, dnis_existentes, correos_existentes, id_usuario)
        actualizar_usuario(id_usuario, matriz_usuarios, dic_usuario_actualizar)
        opcion_seleccionada = modulo_validar.obtener_opcion(False)

def obtener_usuario(id_usuario, matriz_usuarios):
    for fila in matriz_usuarios:
        if fila[0] == id_usuario:
            return {"Nombre":fila[1], "Apellido": fila[2], "D.N.I": fila[3], "Correo": fila[4]} #Diccionario

def actualizar_usuario(id_usuario, matriz_usuarios, dic_usuario_actualizar):
    for fila in matriz_usuarios:
        if fila[0] == id_usuario:
            fila[1] = dic_usuario_actualizar["Nombre"]
            fila[2] = dic_usuario_actualizar["Apellido"]
            fila[3] = dic_usuario_actualizar["D.N.I"]
            fila[4] = dic_usuario_actualizar["Correo"]
            return

def validar_y_actualizar_usuarios(opcion_actualizar, dic_usuario_actualizar, dnis_existentes, correos_existentes, id_usuario):
    validadores = {"Nombre": modulo_validar.validar_strings, #cada dato con su funcion de validar y verifica q dni y correo no exista en el conjunto
                   "Apellido": modulo_validar.validar_strings,
                   "D.N.I": lambda dni: modulo_validar.validar_dni(dni) and dni not in dnis_existentes,
                   "Correo": lambda email: modulo_validar.validar_email(email) and email not in correos_existentes,}
 
    dni_actual = dic_usuario_actualizar.get("D.N.I")
    correo_actual = dic_usuario_actualizar.get("Correo") #obtiene el valor asociado a esa clave

    nuevo_valor = modulo_input.obtener_nuevo_valor(opcion_actualizar, dic_usuario_actualizar, validadores)

    if opcion_actualizar in ["Nombre", "Apellido"]:
        nuevo_valor = nuevo_valor.capitalize()
    if opcion_actualizar == "D.N.I":
        dnis_existentes.discard(dni_actual);dnis_existentes.add(nuevo_valor)
    elif opcion_actualizar == "Correo":
        correos_existentes.discard(correo_actual);correos_existentes.add(nuevo_valor)

    dic_usuario_actualizar[opcion_actualizar] = nuevo_valor #diccionario que almacena la información de un usuario.
    print(f"{nuevo_valor} con ID {id_usuario} ha sido actualizado.") #Movi el print aca
    return dic_usuario_actualizar

def eliminar_matriz_usuarios(matriz_usuarios):
    opcion_seleccionada = modulo_validar.obtener_opcion()
    
    while opcion_seleccionada == 's':
        print("\nEliminar contenido:")
        id_usuario = int(modulo_input.obtener_id(matriz_usuarios, "usuario"))
        # Eliminar el usuario
        matriz_usuarios[:] = [fila for fila in matriz_usuarios if fila[0] != id_usuario] 
        #[:] evita la creación de una nueva lista y modifica la lista existente.
        print(f"El usuario con ID {id_usuario} ha sido eliminado.")
        
        opcion_seleccionada = modulo_validar.obtener_opcion(primera_consulta=False)

def imprimir_matriz_usuarios(matriz_usuarios):
    len_matriz_usuarios=len(matriz_usuarios)
    for encabezado in range(len_matriz_usuarios):
        matriz_usuarios[encabezado][1] = matriz_usuarios[encabezado][1][:8]  # Recortar el nombre a 8 caracteres
                    
    matriz_usuarios_ordenados = sorted(matriz_usuarios, key=lambda fila: fila[2])# Ordenar la lista por apellido
    encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Atributos de cada contenido

    ancho_columna=30  
    modulo_varios.imprimir_linea("superior", len(encabezado_usuarios), ancho_columna)# Imprimir la línea superior del cuadro
    
    print("|" + "|".join([f"{encabezado:<{ancho_columna}}" for encabezado in encabezado_usuarios]) + "|")  # Imprimir el encabezado
    
    modulo_varios.imprimir_linea("interior", len(encabezado_usuarios), ancho_columna)    # Imprimir la línea interior del cuadro
    
    for fila in matriz_usuarios_ordenados:    # Imprimir cada fila de la matriz
        print("|" + "|".join([f"{str(valor).capitalize():<{ancho_columna}}" for valor in fila]) + "|")
    
    modulo_varios.imprimir_linea("inferior", len(encabezado_usuarios), ancho_columna) # Imprimir la línea inferior del cuadro