import menu, matriz_peliculas, matriz_usuarios, matriz_registro_vistas

def _main_():
    proximo_id_peliculas, proximo_id_usuarios,  proximo_id_registro = 5, 5, 3

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
    [1, 4, 'López', 1, 'El Señor de los Anillos', 'en curso', 0],
    [2, 2, 'García', 3, 'Matrix', 'terminada', 9]]

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
                    proximo_id_usuarios=matriz_usuarios.crear_contenido_usuarios(contenido_usuarios, proximo_id_usuarios)

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
                    matriz_usuarios.actualizar_contenido_usuarios(contenido_usuarios)

                    print("\nContenido actualizado:")
                    matriz_usuarios.leer_contenido_usuarios(contenido_usuarios)

                elif subopcion_usuarios == 'd':  # Eliminar Usuarios
                    matriz_usuarios.eliminar_contenido_usuarios(contenido_usuarios)
                    print("\nContenido después de la eliminación:")
                    matriz_usuarios.leer_contenido_usuarios(contenido_usuarios)

                elif subopcion_usuarios == 'e': #Generar reporte
                    matriz_usuarios.imprimir_matriz_usuarios(contenido_usuarios)
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
                    proximo_id_peliculas=matriz_peliculas.crear_contenido_peliculas(contenido_peliculas, proximo_id_peliculas)

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
                    matriz_peliculas.actualizar_contenido_peliculas(contenido_peliculas)

                    print("\nContenido actualizado:")
                    matriz_peliculas.leer_contenido_peliculas(contenido_peliculas)

                elif subopcion_peliculas == 'd': #eliminar
                    matriz_peliculas.eliminar_contenido_peliculas(contenido_peliculas)

                    print("\nContenido después de la eliminación:")
                    matriz_peliculas.leer_contenido_peliculas(contenido_peliculas)

                elif subopcion_peliculas == 'e': #Mostrar reporte
                    matriz_peliculas.imprimir_matriz_peliculas(contenido_peliculas)
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

                if subopcion_registro == 'a':  # Agregar Registro de Vistas
                    proximo_id_registro=matriz_registro_vistas.crear_contenido_registro_vistas(contenido_registro_vistas, contenido_usuarios, contenido_peliculas, proximo_id_registro)

                    print("\nRegistro agregado con éxito.")
                    print("\nContenido registrado:")
                    matriz_registro_vistas.leer_contenido_registro_vistas(contenido_registro_vistas)
                        
                elif subopcion_registro == 'b':  # Listar Registros de Vista
                    print("\nContenido registrado:")
                    registros_ordenados = sorted(contenido_registro_vistas, key=lambda x: x[2])# Ordenar la lista por apellido

                    # Imprimir matriz
                    encabezado_registros = ["ID registro","ID usuario", "Apellido", "ID P/S", "Titulo", "Estado", "Clasificacion"]
                    registros = [dict(zip(encabezado_registros, fila)) for fila in registros_ordenados]
                    
                    for vistas in registros: # Imprimir los diccionarios
                        print(vistas)
                    print()

                elif subopcion_registro == 'c':  # Actualizar Registro de Vista
                    print("\nActualizar contenido:")

                    matriz_registro_vistas.actualizar_contenido_registro_vistas(contenido_registro_vistas, contenido_usuarios, contenido_peliculas)

                    print("\nContenido actualizado:")
                    matriz_registro_vistas.leer_contenido_registro_vistas(contenido_registro_vistas)

                elif subopcion_registro == 'd':  # Eliminar Registro de Vista
                    matriz_registro_vistas.eliminar_contenido_registro_vistas(contenido_registro_vistas)

                    print("\nContenido después de la eliminación:")
                    matriz_registro_vistas.leer_contenido_registro_vistas(contenido_registro_vistas)

                elif subopcion_registro == 'e':  # Generar Reporte
                    matriz_registro_vistas.imprimir_matriz_registro_vistas(contenido_registro_vistas)
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