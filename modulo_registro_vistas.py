import modulo_validar, modulo_menu, modulo_usuarios, modulo_peliculas, modulo_input, modulo_varios

def crear_matriz_registro_vistas(contenido_registro_vistas, matriz_usuarios, matriz_peliculas):
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == "s":
        proximo_id_registro = len(contenido_registro_vistas)+1
        print("\nAgregar registro:")
        usuario_id = modulo_input.obtener_id(matriz_usuarios, "usuarios")
        pelicula_id=int(modulo_input.obtener_id(matriz_peliculas, "pelicula/serie"))
        estado, calificacion = modulo_input.obtener_registro()
        apellido = modulo_usuarios.obtener_usuario(usuario_id, matriz_usuarios)["Apellido"]
        titulo = modulo_peliculas.obtener_pelicula(pelicula_id, matriz_peliculas)["Titulo"]

        print(f"El usuario {usuario_id} ha actualizado el estado de la película/serie '{titulo}' con ID {pelicula_id}.")
    
        fila = [proximo_id_registro, usuario_id, apellido, pelicula_id, titulo, estado, calificacion]
        contenido_registro_vistas.append(fila)
        print("\nRegistro agregado con éxito.")
        opcion_seleccionada = modulo_validar.obtener_opcion(primera_consulta=False)
    
def leer_matriz_registro_vistas(matriz_registro_vistas):
    if not matriz_registro_vistas:
        print("No hay contenido disponible.")
        print()
        return
    
    print("\nContenido registrado:")
    for item in matriz_registro_vistas:
        registro_id,usuario_id,apellido, pelicula_id, titulo, estado, calificacion = item
        print(f"ID del registro: {registro_id}")
        print(f"ID del usuario: {usuario_id}")
        print(f"Apellido: {apellido}")
        print(f"ID Pelicula/serie: {pelicula_id}")
        print(f"Titulo: {titulo}")
        print(f"Estado: {estado}")
        print(f"Calificacion: {calificacion}")
        print("-" * 30)

def actualizar_matriz_registro_vistas(matriz_registro_vistas, matriz_usuarios, matriz_peliculas): 
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == 's':
        id_registro = int(modulo_input.obtener_id(matriz_registro_vistas, "registro"))
        dic_registro_actualizar = obtener_registro(id_registro, matriz_registro_vistas)
        opcion_actualizar = modulo_menu.mostrar_submenu_actualizar(list(dic_registro_actualizar.keys())) #convierte las claves en lista
        # Llamada a la nueva función para validar y actualizar el valor
        dic_registro_actualizar = validar_y_actualizar_registro(opcion_actualizar,dic_registro_actualizar, id_registro, matriz_usuarios, matriz_peliculas)
        actualizar_registro(id_registro, matriz_registro_vistas, dic_registro_actualizar)
        opcion_seleccionada = modulo_validar.obtener_opcion(False)

def obtener_registro(id_registro, matriz_registro_vistas):
    for fila in matriz_registro_vistas:
        if fila[0] == id_registro:
            return {"Usuario ID": fila[1], "Pelicula/Serie ID": fila[3],"Estado": fila[5], "Calificación": fila[6]}
        
def actualizar_registro(id_registro, matriz_registro_vistas, registro_actualizar):
    for fila in matriz_registro_vistas:
        if fila[0] == id_registro:
            fila[1] = registro_actualizar["Usuario ID"] 
            fila[2]= registro_actualizar.get("Apellido", fila[2])  #modifica el apellido solo si se modifico el id
            fila[3] = registro_actualizar["Pelicula/Serie ID"]
            fila[4]= registro_actualizar.get("Titulo", fila[4]) #modifica el titulo solo si se modifico el id
            fila[5] = registro_actualizar["Estado"]
            fila[6] = registro_actualizar["Calificación"]
            return

def validar_y_actualizar_registro(opcion_actualizar, dic_registro_actualizar, id_registro, matriz_usuarios, matriz_peliculas):
    validadores = {"Usuario ID":  lambda id_usuario: modulo_validar.validar_id_actualizar(id_usuario, {"matriz":matriz_usuarios}),
                   "Pelicula/Serie ID": lambda id_pelicula: modulo_validar.validar_id_actualizar(id_pelicula, {"matriz": matriz_peliculas}),
                   "Estado": modulo_validar.validar_estado,
                   "Calificación": modulo_validar.validar_calificacion}
    
    if opcion_actualizar == "Calificación" and dic_registro_actualizar["Estado"] in ["En curso", "Pendiente"]:
        print("No se puede actualizar la calificación mientras el estado sea 'En curso' o 'Pendiente'.")
        return dic_registro_actualizar  # Salimos de la función sin cambiar la calificación

    nuevo_valor = modulo_input.obtener_nuevo_valor(opcion_actualizar, dic_registro_actualizar, validadores).capitalize()

    if opcion_actualizar == "Estado":# Verificamos el nuevo estado y actualizamos la calificación en consecuencia
        if nuevo_valor in ["En curso", "Pendiente"] or (nuevo_valor == "Terminada" and dic_registro_actualizar["Estado"] in ["En curso", "Pendiente"]):
            dic_registro_actualizar["Calificación"] = "0"  # Reinicia la calificación a 0
    
    elif opcion_actualizar== "Usuario ID":
        apellido = modulo_usuarios.obtener_usuario(int(nuevo_valor), matriz_usuarios)["Apellido"]
        dic_registro_actualizar["Apellido"]=apellido

    elif opcion_actualizar== "Pelicula/Serie ID":
        titulo = modulo_peliculas.obtener_pelicula(int(nuevo_valor), matriz_peliculas)["Titulo"]
        dic_registro_actualizar["Titulo"] = titulo

    dic_registro_actualizar[opcion_actualizar] = nuevo_valor
    print(f"{nuevo_valor} con ID {id_registro} ha sido actualizado.") 
    return dic_registro_actualizar

def eliminar_matriz_registro_vistas(matriz_registro_vistas):
    eliminar_registro = modulo_validar.obtener_opcion()
    
    while eliminar_registro == 's':
        print("\nEliminar contenido:")
        id_registro = int(modulo_input.obtener_id(matriz_registro_vistas, "registro"))
        matriz_registro_vistas[:] = [item for item in matriz_registro_vistas if item[0] != id_registro]
        print(f"El registro con ID {id_registro} ha sido eliminado.")
        
        eliminar_registro= modulo_validar.obtener_opcion(primera_consulta=False)

def imprimir_matriz_registro_vistas(contenido_registro_vistas):
    for i in range(len(contenido_registro_vistas)):
        contenido_registro_vistas[i][4] = contenido_registro_vistas[i][4][:8]# Recortar los títulos a un máximo de 8 caracteres
                    
    matriz_registros_ordenados = sorted(contenido_registro_vistas, key=lambda x: x[2]) # Ordenar la matriz por apellido
    encabezado_registros = ["ID registro","ID usuario", "Apellido", "ID Pelicula/Serie", "Titulo", "Estado", "Calificacion"]

    ancho_columna=20
    modulo_varios.imprimir_linea("superior", len(encabezado_registros), ancho_columna)# Imprimir la línea superior del cuadro
    
    print("|" + "|".join([f"{encabezado:<{ancho_columna}}" for encabezado in encabezado_registros]) + "|")  # Imprimir el encabezado
    
    modulo_varios.imprimir_linea("interior", len(encabezado_registros), ancho_columna)    # Imprimir la línea interior del cuadro
    
    for fila in matriz_registros_ordenados:    # Imprimir cada fila de la matriz
        print("|" + "|".join([f"{str(valor).capitalize():<{ancho_columna}}" for valor in fila]) + "|")
    
    modulo_varios.imprimir_linea("inferior", len(encabezado_registros), ancho_columna) # Imprimir la línea inferior del cuadro
