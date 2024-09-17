import menu, matriz_peliculas, matriz_usuarios, matriz_registro_vistas, validar

def _main_():
    proximo_id_peliculas, proximo_id_usuarios = 5, 5

    contenido_usuarios = [
    [1, "Juan", "Pérez","12.345.678", "juan.perez@gmail.com"],
    [2, "Ana", "García","23.456.789", "ana.garcia@yahoo.com"],
    [3, "Luis", "Martínez","34.567.890", "luis.martinez@hotmail.com"],
    [4, "Laura", "López","45.678.901", "laura.lopez@gmail.com"]]
    contenido_peliculas =[
    [1, "El Señor de los Anillos","Película", "Fantasía", 2001,"178 minutos"],
    [2, "Breaking Bad", "Serie",  "Drama", 2008 , "5 temporadas"], 
    [3, "Matrix", "Película", "Ciencia Ficción", 1999, "136 minutos"],
    [4, "Stranger Things", "Serie", "Terror", 2016, "4 temporadas"] ]
    contenido_registro_vistas=[
    [2, 'García', 3, 'Matrix', 'terminada', 9],
    [4, 'López', 1, 'El Señor de los Anillos', 'en curso', 0]]

    salir=True
    while salir:
        menu.mostrar_menu()
        opcion = input("Seleccione una opción del menú principal: ")

        if opcion == '1':  # Menú de Usuarios
            submenu_activo = True  # Bandera para controlar el bucle del submenú de usuarios
            while submenu_activo:
                menu.mostrar_submenu(opcion)
                subopcion_usuarios = input("Seleccione una opción del submenú de Usuarios: ").strip().lower()

                if subopcion_usuarios=='a':  # Agregar Usuario
                    seguir = "0"
                    while seguir != "-1":
                        nombre=validar.obtener_nombre()
                        apellido=validar.obtener_apellido()
                        dni = validar.obtener_dni()
                        correo = validar.obtener_email()

                        matriz_usuarios.crear_contenido_usuarios(contenido_usuarios, proximo_id_usuarios, nombre, apellido, dni, correo)
                        proximo_id_usuarios += 1

                        seguir = (input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
                        
                        while seguir!="-1" and seguir!="0":
                            print("Ingreso no valido, vuelva a intentar")
                            seguir=(input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))

                    print("\nUsuario agregado con éxito.")
                    print("\nContenido registrado:")
                    matriz_usuarios.leer_contenido_usuarios(contenido_usuarios)
                    
                elif subopcion_usuarios == 'b':  # Listar Usuarios
                    print("\nContenido registrado:")
                    usuarios_ordenados = sorted(contenido_usuarios, key=lambda x: x[2]) # Ordenar la lista por apellido

                    encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Atributos de cada contenido
                    usuarios = [dict(zip(encabezado_usuarios, fila)) for fila in usuarios_ordenados] #La combierte a diccionario
                    for usuario in usuarios: # Imprimir los diccionarios
                        print(usuario)
                    print()

                elif subopcion_usuarios== 'c':  # Actualizar Usuario
                    actualizar_opcion_usuarios = validar.validar_actualizacion()

                    while actualizar_opcion_usuarios == 's':
                        print("\nActualizar contenido:")

                        # Solicitar el ID del usuario a cambiar
                        nuevo_id_usuarios = input("Ingrese el ID del usuario a cambiar: ")

                        # Validar que el ID sea numérico y que exista en el contenido
                        while not nuevo_id_usuarios.isdigit() or not validar.si_existe_id_usuario(int(nuevo_id_usuarios), contenido_usuarios):
                            if not nuevo_id_usuarios.isdigit():
                                print("Por favor, ingrese un número válido.")  # Mensaje si el input no es numérico
                            else:
                                print("ID no encontrado. Por favor, ingrese un ID válido.")  # Mensaje si el ID no está en la matriz
                            nuevo_id_usuarios = input("Ingrese el ID del usuario a cambiar: ")

                        # Convertir a entero después de la validación
                        nuevo_id_usuarios = int(nuevo_id_usuarios)

                        print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

                        nuevo_nombre_str = input("Nuevo nombre (deje en blanco para no cambiar): ").strip().capitalize()
                        if nuevo_nombre_str:
                            if validar.validar_nombre(nuevo_nombre_str):
                                nuevo_nombre = nuevo_nombre_str
                            else:
                                print("El nuevo nombre ingresado no es válido. Intente nuevamente.")
                                nuevo_nombre = validar.obtener_nombre()  # Solicita un nuevo nombre si el ingresado no es válido
                        else:
                            nuevo_nombre = None  # Si el campo está en blanco, no se actualiza el nombre
                        
                        nuevo_apellido_str = input("Nuevo apellido (deje en blanco para no cambiar): ").strip().capitalize()
                        if nuevo_apellido_str:
                            if validar.validar_apellido(nuevo_apellido_str):
                                nuevo_apellido = nuevo_apellido_str
                            else:
                                print("El nuevo apellido ingresado no es válido. Intente nuevamente.")
                                nuevo_apellido = validar.obtener_apellido()  # Solicita un nuevo apellido si el ingresado no es válido
                        else:
                            nuevo_apellido = None  # Si el campo está en blanco, no se actualiza el apellido
                        
                        nuevo_dni_str = input("Nuevo DNI (deje en blanco para no cambiar): ").strip()
                        if nuevo_dni_str:
                            if validar.validar_dni(nuevo_dni_str):
                                nuevo_dni = nuevo_dni_str
                            else:
                                print("El nuevo DNI ingresado no es válido.")
                                nuevo_dni = validar.obtener_dni() 
                        else:
                            nuevo_dni = None  # Si el campo está en blanco, no se actualiza el DNI

                        nuevo_correo_str = input("Nuevo correo (deje en blanco para no cambiar): ")
                        if nuevo_correo_str:
                            if validar.validar_email(nuevo_correo_str):
                                nuevo_correo = nuevo_correo_str
                            else:
                                print("El nuevo correo ingresado no es válido.")
                                nuevo_correo = validar.obtener_email() 
                        else:
                            nuevo_correo = None  # Si el campo está en blanco, no se actualiza el correo

                        matriz_usuarios.actualizar_contenido_usuarios(contenido_usuarios, nuevo_id_usuarios,nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_correo)

                        print("\nContenido actualizado:")
                        matriz_usuarios.leer_contenido_usuarios(contenido_usuarios)

                        actualizar_opcion_usuarios = validar.validar_actualizacion(primera_consulta=False)

                elif subopcion_usuarios == 'd':  # Eliminar Usuario
                    eliminar_opcion_usuarios = validar.validar_eliminacion(contenido_usuarios)

                    while eliminar_opcion_usuarios == 's':
                        print("\nEliminar contenido:")

                        matriz_usuarios.eliminar_contenido_usuarios(contenido_usuarios)

                        print("\nContenido después de la eliminación:")
                        matriz_usuarios.leer_contenido_usuarios(contenido_usuarios)

                        eliminar_opcion_usuarios = validar.validar_eliminacion(primera_consulta=False)

                        print("\nProceso finalizado.")
                    
                elif subopcion_usuarios == 'e': #Generar reporte
                    for i in range(len(contenido_usuarios)):
                        contenido_usuarios[i][1] = contenido_usuarios[i][1][:8]  # Recortar el nombre a 8 caracteres
                    
                    usuarios_ordenados = sorted(contenido_usuarios, key=lambda x: x[2])# Ordenar la lista por apellido

                    # Imprimir matriz
                    ids_usuarios = [item[1] for item in usuarios_ordenados]  # Nombres de los usuarios
                    encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Atributos de cada contenido

                    matriz_usuarios.imprimir_matriz_usuarios(usuarios_ordenados, ids_usuarios, encabezado_usuarios)
                    print()
                
                elif subopcion_usuarios == 'f': # Volver al menú principal
                    submenu_activo = False  # Salir del submenú volviendo al menú principal
                
                else:
                    print("\nOpción no válida, intente nuevamente.")

        elif opcion == '2': #Menu de peliculas/series
            submenu_activo = True  # Bandera para controlar el bucle del submenú
            while submenu_activo:
                menu.mostrar_submenu(opcion)
                subopcion_peliculas = input("Seleccione una opción del submenú de Películas/Series: ").strip().lower()

                if subopcion_peliculas == 'a': #Agregar peliculas
                    continuar = "0"
                    while continuar!="-1":
                        titulo=validar.obtener_titulo()
                        tipo = validar.obtener_tipo()
                        genero=validar.obtener_genero()
                        año = validar.obtener_año()
                        duracion = validar.validar_duracion(tipo)

                        matriz_peliculas.crear_contenido_peliculas(contenido_peliculas, proximo_id_peliculas, titulo, tipo, genero, año, duracion)
                        proximo_id_peliculas += 1

                        continuar = (input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
                    
                        while continuar!="-1" and continuar!="0":
                            print("Ingreso no valido, vuelva a intentar")
                            continuar=(input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))

                    print("\nPelícula/Serie agregada con éxito.")
                    print("\nContenido registrado:")
                    matriz_peliculas.leer_contenido_peliculas(contenido_peliculas)

                elif subopcion_peliculas == 'b':#listar películas/series
                    print("\nContenido registrado:")
                    # Convertir el año a entero si está en formato de cadena
                    for pelicula in contenido_peliculas:
                        pelicula[4] = int(pelicula[4])  # Convertir el año de estreno a entero

                    # Ordenar la lista por año de estreno (ascendente)
                    peliculas_ordenadas = sorted(contenido_peliculas, key=lambda x: x[4])

                    #imprimir matriz
                    encabezado = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido
                    peliculas = [dict(zip(encabezado, fila)) for fila in peliculas_ordenadas]
                    # Imprimir los diccionarios
                    for pelis in peliculas:
                        print(pelis)
                    print()
                    
                elif subopcion_peliculas == 'c': #actualizar
                    # Código para actualizar películas/series
                    actualizar_opcion_peliculas = validar.validar_actualizacion()

                    while actualizar_opcion_peliculas == 's':
                        print("\nActualizar contenido:")
                        
                        # Solicitar el ID de la película/serie a cambiar
                        nuevo_id_peliculas = input("Ingrese el ID de la película/serie a cambiar: ")

                        # Validar que el ID sea numérico y que exista en el contenido
                        while not nuevo_id_peliculas.isdigit() or not validar.si_existe_id_pelicula(int(nuevo_id_peliculas), contenido_peliculas):
                            if not nuevo_id_peliculas.isdigit(): #isdigit() verifica que todos los caracteres sena nros
                                print("Por favor, ingrese un número válido.")  # Mensaje si el input no es numérico
                            else:
                                print(f"El ID {nuevo_id_peliculas} no existe. Ingrese un ID válido.")  # Mensaje si el ID no está en la matriz
                            nuevo_id_peliculas = input("Ingrese el ID de la película/serie a cambiar: ")

                        # Convertir a entero después de la validación
                        nuevo_id_peliculas = int(nuevo_id_peliculas)

                        print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

                        nuevo_titulo = input("Nuevo título (deje en blanco para no cambiar): ")

                        nuevo_tipo_str = input("Nuevo tipo (deje en blanco para no cambiar): ").strip().lower()
                        # Para la actualización del tipo (se permite dejar el campo en blanco)
                        if nuevo_tipo_str:
                            if validar.validar_tipo(nuevo_tipo_str):
                                nuevo_tipo = nuevo_tipo_str
                            else:
                                print("El nuevo tipo ingresado no es válido. Intente nuevamente.")
                                nuevo_tipo = validar.obtener_tipo()  # Solicita un nuevo tipo si el ingresado no es válido
                        else:
                            nuevo_tipo = None  # Si el campo está en blanco, no se actualiza el tipo
                        
                        nuevo_genero_str = input("Nuevo género (deje en blanco para no cambiar): ")
                        if nuevo_genero_str:
                            if validar.validar_genero(nuevo_genero_str):
                                nuevo_genero = nuevo_genero_str
                            else:
                                print("El nuevo genero ingresado no es válido. Intente nuevamente.")
                                nuevo_genero = validar.obtener_genero()  # Solicita un nuevo genero si el ingresado no es válido
                        else:
                            nuevo_genero = None  # Si el campo está en blanco, no se actualiza el genero

                        nuevo_año_str = input("Nuevo año (deje en blanco para no cambiar): ")
                        if nuevo_año_str:
                            if validar.validar_año(nuevo_año_str):
                                nuevo_año = nuevo_año_str
                            else:
                                print("El nuevo año ingresado no es válido.")
                                nuevo_año =  validar.obtener_año() 
                        else:
                            nuevo_año = None  # Si el campo está en blanco, no se actualiza el año
                        
                        nuevo_duracion = validar.validar_duracion(nuevo_tipo)
                        
                        matriz_peliculas.actualizar_contenido_peliculas(contenido_peliculas, nuevo_id_peliculas,nuevo_titulo, nuevo_tipo, nuevo_genero, nuevo_año, nuevo_duracion)

                        print("\nContenido actualizado:")
                        matriz_peliculas.leer_contenido_peliculas(contenido_peliculas)
                        
                        actualizar_opcion_peliculas = validar.validar_actualizacion(primera_consulta=False)

                elif subopcion_peliculas == 'd': #eliminar
                    # Código para eliminar películas/series
                    eliminar_opcion_peliculas = validar.validar_eliminacion()
                    while eliminar_opcion_peliculas == 's':
                        print("\nEliminar contenido:")
                        
                        matriz_peliculas.eliminar_contenido_peliculas(contenido_peliculas)

                        print("\nContenido después de la eliminación:")
                        matriz_peliculas.leer_contenido_peliculas(contenido_peliculas)
                        
                        eliminar_opcion_peliculas = validar.validar_eliminacion(primera_consulta=False)

                elif subopcion_peliculas == 'e': #Mostrar reporte
                    for i in range(len(contenido_peliculas)):
                        contenido_peliculas[i][1] = contenido_peliculas[i][1][:8]  #Recortar el título a 8 caracteres

                    for pelicula in contenido_peliculas:  # Convertir el año a entero si está en formato de cadena
                        pelicula[4] = int(pelicula[4])  # Convertir el año de estreno a entero
                            
                    peliculas_ordenadas = sorted(contenido_peliculas, key=lambda x: x[4]) # Ordenar la lista por año de estreno (ascendente)

                    #imprimir matriz
                    ids_peliculas=[item[1] for item in peliculas_ordenadas]  # Nombres de las películas/series
                    encabezado = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido

                    matriz_peliculas.imprimir_matriz_peliculas(peliculas_ordenadas, ids_peliculas, encabezado)
                    print()
                
                elif subopcion_peliculas == 'f':# Volver al menú principal
                    submenu_activo = False  # Bandera para salir del bucle del submenú
             
                else:
                    print("Opción no válida, intente nuevamente.")

        elif opcion=='3': #Menu registro vistas
            submenu_activo = True  # Bandera para controlar el bucle del submenú
            while submenu_activo:
                menu.mostrar_submenu(opcion)
                subopcion_registro = input("Seleccione una opción del submenú de Registro: ").strip().lower()

                if subopcion_registro == 'a':  # Agregar Registro de Vista
                    combinacion = "0"
                    while combinacion != "-1":
                        usuario_id = validar.validar_usuario_id(contenido_usuarios)
                        pelicula_id = validar.validar_pelicula_id(contenido_peliculas)
                        estado = validar.obtener_estado()
                        if estado == "terminada":
                            estado = "Terminada"
                            calificacion = validar.obtener_calificacion()
                        else:
                            calificacion = 0  # Dejar calificación en 0 si no se desea ingresar

                        matriz_registro_vistas.crear_contenido_registro_vistas(contenido_registro_vistas, usuario_id, pelicula_id, estado, calificacion, contenido_peliculas, contenido_usuarios)

                        combinacion = (input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
                        
                        while combinacion!="-1" and combinacion!="0":
                            print("Ingreso no valido, vuelva a intentar")
                            combinacion=(input("Si desea continuar ingresando contenido ingrese 0, si desea finalizar el proceso, indique -1: "))
                        
                        print("\nRegistro agregado con éxito.")
                        print("\nContenido registrado:")
                        matriz_registro_vistas.leer_contenido_registro_vistas(contenido_registro_vistas)
                        
                elif subopcion_registro == 'b':  # Listar Registros de Vista
                    print("\nContenido registrado:")
                    registros_ordenados = sorted(contenido_registro_vistas, key=lambda x: x[1])# Ordenar la lista por apellido

                    # Imprimir matriz
                    encabezado_registros = ["ID usuario", "Apellido", "ID P/S", "Titulo", "Estado", "Clasificacion"]
                    registros = [dict(zip(encabezado_registros, fila)) for fila in registros_ordenados]
                    
                    for vistas in registros: # Imprimir los diccionarios
                        print(vistas)
                    print()

                elif subopcion_registro == 'c':  # Actualizar Registro de Vista
                    actualizar_opcion_registro_vistas = validar.validar_actualizacion()

                    while actualizar_opcion_registro_vistas == 's':
                        print("\nActualizar contenido:")
                        
                        # Solicitar el ID de usuario para cambiar
                        nuevo_id_registro = input("Ingrese el ID del usuario del registro a cambiar: ")

                        # Validar que el ID sea numérico y que exista en contenido_registro_vistas
                        while not nuevo_id_registro.isdigit() or not validar.si_existe_id_usuario(int(nuevo_id_registro), contenido_registro_vistas):
                            if not nuevo_id_registro.isdigit():
                                print("Por favor, ingrese un número válido.")  # Mensaje si el input no es numérico
                            else:
                                print("ID no encontrado. Por favor, ingrese un ID válido.")  # Mensaje si el ID no está en la matriz
                            nuevo_id_registro = input("Ingrese el ID del usuario del registro a cambiar: ")

                        # Convertir a entero después de la validación
                        nuevo_id_registro = int(nuevo_id_registro)

                        print("Ingrese los nuevos datos (deje en blanco si no desea cambiar un campo).")

                        nuevo_id_pelicula = (input("Nuevo ID de película/serie (deje en blanco para no cambiar): "))
                        # Si el usuario ingresa un valor (no está en blanco)
                        if nuevo_id_pelicula:
                            # Validar que el ID sea numérico y que exista en el contenido
                            while not nuevo_id_pelicula.isdigit() or not validar.si_existe_id_pelicula(int(nuevo_id_pelicula), contenido_peliculas):
                                if not nuevo_id_pelicula.isdigit():
                                    print("Por favor, ingrese un número válido.")  # Mensaje si el input no es numérico
                                else:
                                    print("ID no encontrado. Por favor, ingrese un ID válido.")  # Mensaje si el ID no está en la matriz
                                
                                nuevo_id_pelicula = input("Nuevo ID de película/serie (deje en blanco para no cambiar): ")

                            # Convertir a entero después de la validación
                            nuevo_id_pelicula = int(nuevo_id_pelicula)
                        else:
                            nuevo_id_pelicula = None  # Indicar que no se desea cambiar el ID

                        nuevo_estado_str = input("Nuevo estado (deje en blanco para no cambiar): ").strip().lower()
                        if nuevo_estado_str:
                            if validar.validar_estado(nuevo_estado_str):
                                nuevo_estado = nuevo_estado_str
                                if nuevo_estado == "terminada":
                                    nuevo_calificacion = validar.obtener_calificacion()
                                else:
                                    nuevo_calificacion = None
                            else:
                                print("El nuevo estado ingresado no es válido. Intente nuevamente.")
                                nuevo_estado = validar.obtener_estado()
                                if nuevo_estado == "terminada":
                                    nuevo_calificacion = validar.obtener_calificacion()
                                else:
                                    nuevo_calificacion = None
                        else:
                            nuevo_estado = None
                            nuevo_calificacion = None

                        matriz_registro_vistas.actualizar_contenido_registro_vistas(contenido_registro_vistas, nuevo_id_registro, nuevo_id_pelicula, estado=nuevo_estado, calificacion=nuevo_calificacion)

                        print("\nContenido actualizado:")
                        matriz_registro_vistas.leer_contenido_registro_vistas(contenido_registro_vistas)

                        actualizar_opcion_registro_vistas = validar.validar_actualizacion(primera_consulta=False)

                elif subopcion_registro == 'd':  # Eliminar Registro de Vista
                    eliminar_opcion_registro_vistas = validar.validar_eliminacion()

                    while eliminar_opcion_registro_vistas == 's':
                        print("\nEliminar contenido:")

                        matriz_registro_vistas.eliminar_contenido_registro_vistas(contenido_registro_vistas)

                        print("\nContenido después de la eliminación:")
                        matriz_registro_vistas.leer_contenido_registro_vistas(contenido_registro_vistas)

                        eliminar_opcion_registro_vistas = validar.validar_eliminacion(primera_consulta=False)

                        print("\nProceso finalizado.")

                elif subopcion_registro == 'e':  # Generar Reporte
                    for i in range(len(contenido_registro_vistas)):
                        contenido_registro_vistas[i][3] = contenido_registro_vistas[i][3][:8]# Recortar los títulos a un máximo de 8 caracteres
                    
                    registros_ordenados = sorted(contenido_registro_vistas, key=lambda x: x[1]) # Ordenar la matriz por apellido

                    # Imprimir matriz
                    ids_registro = [item[1] for item in registros_ordenados]  # Apellidos de los usuarios
                    encabezado_registros = ["ID usuario", "Apellido", "ID P/S", "Titulo", "Estado", "Clasificacion"]

                    matriz_registro_vistas.imprimir_matriz_registro_vistas(registros_ordenados, ids_registro, encabezado_registros)
                    print()
                
                elif subopcion_registro == 'f':# Volver al menú principal
                    submenu_activo = False  # Salir del submenú volviendo al menú principal

                else:
                    print("Opción no válida, intente nuevamente.")
        
        elif opcion == '4':  # Salir del programa
            print("\nSaliendo del programa")
            salir=False

if __name__ == "__main__":
    _main_()