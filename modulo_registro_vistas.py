import validar, menu

def crear_matriz_registro_vistas(contenido_registro_vistas, contenido_usuarios, contenido_peliculas):
    agregar_registro=validar.obtener_opcion()
    while agregar_registro=="s":
        proximo_id_registro=len(contenido_registro_vistas)+1
        print("\nAgregar registro:")
        usuario_id = validar.validar_usuario_id(contenido_usuarios)
        pelicula_id = validar.validar_pelicula_id(contenido_peliculas)
        estado = validar.obtener_estado()
        calificacion = validar.obtener_calificacion() if estado == "Terminada" else 0
        
        apellido = validar.obtener_apellido_usuario(contenido_usuarios, usuario_id)
        titulo = validar.obtener_titulo_pelicula(contenido_peliculas, pelicula_id)

        print(f"El usuario {usuario_id} ha actualizado el estado de la película/serie '{titulo}' con ID {pelicula_id}.")
    
        item = [proximo_id_registro, usuario_id, apellido, pelicula_id, titulo, estado, calificacion]
        contenido_registro_vistas.append(item)

        agregar_registro=validar.obtener_opcion(primera_consulta=False)
    
def leer_matriz_registro_vistas(contenido_registro_vistas):
    if not contenido_registro_vistas:
        print("No hay contenido disponible.")
        print()
        return
    
    for item in contenido_registro_vistas:
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
    opcion_seleccionada = validar.obtener_opcion()
    while opcion_seleccionada == 's':
        id_registro = input("Ingrese el ID del registro a actualizar: ").strip()
        while not id_registro.isdigit() or not validar.si_existe_id(int(id_registro), matriz_registro_vistas):
            id_registro = validar.manejar_error("ID no válido. Reintentando...", lambda: input("Ingrese un ID válido: "))
        
        id_registro = int(id_registro)

        dic_registro_actualizar = obtener_registro(id_registro, matriz_registro_vistas)
        opcion_actualizar = menu.mostrar_submenu_actualizar(list(dic_registro_actualizar.keys()))
        nuevo_valor = input(f"Ingrese nuevo/a {opcion_actualizar}, valor anterior {dic_registro_actualizar[opcion_actualizar]}: ")
        dic_registro_actualizar[opcion_actualizar] = nuevo_valor
        actualizar_registro(id_registro, matriz_registro_vistas, dic_registro_actualizar)
        print(f"{nuevo_valor} con ID {id_registro} ha sido actualizado.")
        opcion_seleccionada = validar.obtener_opcion(False)

def obtener_registro(id_registro, matriz_registro_vistas):
    for fila in matriz_registro_vistas:
        if fila[0] == id_registro:
            return {"Estado": fila[5], "Calificación": fila[6]}
        
def actualizar_registro(id_registro, matriz_registro_vistas, registro_actualizar):
    for fila in matriz_registro_vistas:
        if fila[0] == id_registro:
            fila[5] = registro_actualizar["Estado"]
            fila[6] = registro_actualizar["Calificación"]
            return

def eliminar_matriz_registro_vistas(contenido_registro_vistas):
    eliminar_registro = validar.obtener_opcion()
    
    while eliminar_registro == 's':
        print("\nEliminar contenido:")
        eliminar_id_registro = input("Ingrese el ID del registro a eliminar: ").strip()

        while not eliminar_id_registro.isdigit() or not validar.si_existe_id(int(eliminar_id_registro), contenido_registro_vistas):
            if not eliminar_id_registro.isdigit():
                print("Por favor, ingrese un número válido.")
            else:
                print("ID no encontrado. Por favor, ingrese un ID válido.")
            eliminar_id_registro = input("Ingrese el ID del registro a eliminar: ").strip()
        
        eliminar_id_registro = int(eliminar_id_registro)
        
        # Eliminar el registro
        contenido_registro_vistas[:] = [item for item in contenido_registro_vistas if item[0] != eliminar_id_registro] #[:] evita la creación de una nueva lista y modifica la lista existente.
        print(f"El registro con ID {eliminar_id_registro} ha sido eliminado.")
        
        eliminar_registro= validar.obtener_opcion(primera_consulta=False)

def imprimir_matriz_registro_vistas(contenido_registro_vistas):
    for i in range(len(contenido_registro_vistas)):
        contenido_registro_vistas[i][4] = contenido_registro_vistas[i][4][:8]# Recortar los títulos a un máximo de 8 caracteres
                    
    registros_ordenados = sorted(contenido_registro_vistas, key=lambda x: x[1]) # Ordenar la matriz por apellido
    encabezado_registros = ["ID registro","ID usuario", "Apellido", "ID P/S", "Titulo", "Estado", "Calificacion"]

    # Imprimir el encabezado
    for i in encabezado_registros:
        print(f"{i:<20}", end="") 
    print()   

    # Imprimir cada fila con el nombre de la pelicula/serie
    for i in range(len(registros_ordenados)):
        for j in range(len(registros_ordenados[i])):
            valor = str(registros_ordenados[i][j]).capitalize() #mayuscula
            print(f"{valor:<20}", end="")
        print()
    print()

def listar_matriz_registro_vistas(matriz_registro_vistas):
    registros_ordenados = sorted(matriz_registro_vistas, key=lambda x: x[2])# Ordenar la lista por apellido
    # Imprimir matriz
    encabezado_registros = ["ID registro","ID usuario", "Apellido", "ID P/S", "Titulo", "Estado", "Calificacion"]
    registros = [dict(zip(encabezado_registros, fila)) for fila in registros_ordenados]
    
    for vistas in registros: # Imprimir los diccionarios
        print(vistas)
    print()
