#Matriz registro vistas
import validar

def crear_matriz_registro_vistas(contenido_registro_vistas, contenido_usuarios, contenido_peliculas):
    agregar_registro=validar.validar_continuacion()
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

        agregar_registro=validar.validar_continuacion(primera_consulta=False)
    
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

def actualizar_matriz_registro_vistas(contenido_registro_vistas, contenido_usuarios, contenido_peliculas): 
    actualizar_registro_vistas = validar.validar_continuacion()
    while actualizar_registro_vistas == 's':
        actualizar_id_registro = input("Ingrese el ID del registro a actualizar: ").strip()
        while not actualizar_id_registro.isdigit() or not validar.si_existe_id(int(actualizar_id_registro), contenido_registro_vistas):
            actualizar_id_registro = validar.manejar_error("ID no válido. Reintentando...", lambda: input("Ingrese un ID válido: "))
        
        actualizar_id_registro = int(actualizar_id_registro)
        for item in contenido_registro_vistas:
            if item[0] == actualizar_id_registro:
                print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")
                def validar_dato(dato, funcion_validar, obtener_funcion, actual):
                    return validar.manejar_error(f"{dato} no válido. Reintentando...", obtener_funcion) if dato and not funcion_validar(dato) else dato or actual
                
                
                nuevo_id_usuario = validar.validar_usuario_id(contenido_usuarios, permitir_vacio=True)
                if nuevo_id_usuario is not None:  # Asegúrate de que no sea None antes de asignar
                    nuevo_apellido=validar.obtener_apellido_usuario(contenido_usuarios, nuevo_id_usuario)  
                    item[1], item[2]=nuevo_id_usuario, nuevo_apellido # Actualiza item[1] con el nuevo ID de usuario y el item[2] con nuevo apellido
                else:
                    nuevo_id_usuario,nuevo_apellido = item[1], item[2]

                nuevo_id_pelicula = validar.validar_pelicula_id(contenido_peliculas, permitir_vacio=True)
                if nuevo_id_pelicula is not None:  # Asegúrate de que no sea None antes de asignar
                    nuevo_titulo=validar.obtener_titulo_pelicula(contenido_peliculas, nuevo_id_pelicula)
                    item[3], item[4] = nuevo_id_pelicula, nuevo_titulo 
                else:
                    nuevo_id_pelicula,nuevo_titulo=item[3],item[4]

                nuevo_estado = validar_dato(input("Nuevo estado: ").strip(). lower(), validar.validar_estado, validar.obtener_estado, item[5])

                # Si el estado fue actualizado, se requiere gestionar la calificación
                nuevo_calificacion=item[6]
                if nuevo_estado != item[5]:  # Solo si hay un cambio en el estado
                    if nuevo_estado == "terminada":
                        calificacion_input = input("Ingrese la calificación: ").strip()
                        nuevo_calificacion = validar_dato(calificacion_input, validar.validar_calificacion, validar.obtener_calificacion, item[6])
                    elif nuevo_estado in ["en curso", "pendiente"]:
                        nuevo_calificacion = 0  # Reinicia la calificación
                

                item[1], item[2], item[3], item[4], item[5], item[6]= nuevo_id_usuario,nuevo_apellido, nuevo_id_pelicula,nuevo_titulo, nuevo_estado, nuevo_calificacion
                print(f"ID {actualizar_id_registro} ha sido actualizado")
                actualizar_registro_vistas = validar.validar_continuacion(primera_consulta=False)
                
                return         

def eliminar_matriz_registro_vistas(contenido_registro_vistas):
    eliminar_registro = validar.validar_continuacion()
    
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
        
        eliminar_registro= validar.validar_continuacion(primera_consulta=False)

def imprimir_matriz_registro_vistas(contenido_registro_vistas):
    for i in range(len(contenido_registro_vistas)):
        contenido_registro_vistas[i][4] = contenido_registro_vistas[i][4][:8]# Recortar los títulos a un máximo de 8 caracteres
                    
    registros_ordenados = sorted(contenido_registro_vistas, key=lambda x: x[1]) # Ordenar la matriz por apellido

    ids_registro = [item[2] for item in registros_ordenados]  # Apellidos de los usuarios
    encabezado_registros = ["ID registro","ID usuario", "Apellido", "ID P/S", "Titulo", "Estado", "Clasificacion"]

    # Imprimir el encabezado
    print(" " * 12, end="")  # Espacio para alinear con los nombres
    for i in encabezado_registros:
        print(f"{i:>20}", end="") 
    print()   

    # Imprimir cada fila con el nombre de la pelicula/serie
    for i in range(len(registros_ordenados)):
        print(f"{ids_registro[i]:<12}", end="")
        for j in range(len(registros_ordenados[i])):
            valor = str(registros_ordenados[i][j]).capitalize() #mayuscula
            print(f"{valor:>20}", end="")
        print()
    print()

def listar_matriz_registro_vistas(matriz_registro_vistas):
    registros_ordenados = sorted(matriz_registro_vistas, key=lambda x: x[2])# Ordenar la lista por apellido
    # Imprimir matriz
    encabezado_registros = ["ID registro","ID usuario", "Apellido", "ID P/S", "Titulo", "Estado", "Clasificacion"]
    registros = [dict(zip(encabezado_registros, fila)) for fila in registros_ordenados]
    
    for vistas in registros: # Imprimir los diccionarios
        print(vistas)
    print()
