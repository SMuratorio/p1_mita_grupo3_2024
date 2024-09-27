import menu, modulo_peliculas, modulo_usuarios, modulo_registro_vistas

def _main_():

    matriz_usuarios = [
    [1, "Juan", "Pérez","12.345.678", "juan.perez@gmail.com"],
    [2, "Ana", "García","23.456.789", "ana.garcia@yahoo.com"],
    [3, "Luis", "Martínez","34.567.890", "luis.martinez@hotmail.com"],
    [4, "Laura", "López","45.678.901", "laura.lopez@gmail.com"]]
    matriz_peliculas =[
    [1, "El Señor de los Anillos","Película", "Fantasía", 2001,"178 minutos"],
    [2, "Breaking Bad", "Serie",  "Drama", 2008 , "5 temporadas"], 
    [3, "Matrix", "Película", "Ciencia Ficción", 1999, "136 minutos"],
    [4, "Stranger Things", "Serie", "Terror", 2016, "4 temporadas"] ]
    matriz_registro_vistas=[
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
                    modulo_usuarios.crear_contenido_usuarios(matriz_usuarios)

                    print("\nUsuario agregado con éxito.")
                    print("\nContenido registrado:")
                    modulo_usuarios.leer_contenido_usuarios(matriz_usuarios)
                    
                elif subopcion_usuarios == 'b':  # Listar Usuarios
                    print("\nContenido registrado:")
                    usuarios_ordenados = sorted(matriz_usuarios, key=lambda x: x[2]) # Ordenar la lista por apellido

                    encabezado_usuarios = ["ID", "Nombre", "Apellido", "DNI", "Correo"]  # Atributos de cada contenido
                    usuarios = [dict(zip(encabezado_usuarios, fila)) for fila in usuarios_ordenados] #La combierte a diccionario
                    for usuario in usuarios: # Imprimir los diccionarios
                        print(usuario)
                    print()

                elif subopcion_usuarios== 'c':  # Actualizar Usuario
                    modulo_usuarios.actualizar_contenido_usuarios(matriz_usuarios)

                    print("\nContenido actualizado:")
                    modulo_usuarios.leer_contenido_usuarios(matriz_usuarios)

                elif subopcion_usuarios == 'd':  # Eliminar Usuarios
                    modulo_usuarios.eliminar_contenido_usuarios(matriz_usuarios)
                    print("\nContenido después de la eliminación:")
                    modulo_usuarios.leer_contenido_usuarios(matriz_usuarios)

                elif subopcion_usuarios == 'e': #Generar reporte
                    modulo_usuarios.imprimir_matriz_usuarios(matriz_usuarios)
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
                    modulo_peliculas.crear_contenido_peliculas(matriz_peliculas)

                    print("\nPelícula/Serie agregada con éxito.")
                    print("\nContenido registrado:")
                    modulo_peliculas.leer_contenido_peliculas(matriz_peliculas)

                elif subopcion_peliculas == 'b':#listar películas/series
                    print("\nContenido registrado:")
                    # Convertir el año a entero si está en formato de cadena
                    for pelicula in matriz_peliculas:
                        pelicula[4] = int(pelicula[4])  # Convertir el año de estreno a entero

                    # Ordenar la lista por año de estreno (ascendente)
                    peliculas_ordenadas = sorted(matriz_peliculas, key=lambda x: x[4])

                    #imprimir matriz
                    encabezado = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido
                    peliculas = [dict(zip(encabezado, fila)) for fila in peliculas_ordenadas]
                    # Imprimir los diccionarios
                    for pelis in peliculas:
                        print(pelis)
                    print()
                    
                elif subopcion_peliculas == 'c': #actualizar
                    modulo_peliculas.actualizar_contenido_peliculas(matriz_peliculas)

                    print("\nContenido actualizado:")
                    modulo_peliculas.leer_contenido_peliculas(matriz_peliculas)

                elif subopcion_peliculas == 'd': #eliminar
                    modulo_peliculas.eliminar_contenido_peliculas(matriz_peliculas)

                    print("\nContenido después de la eliminación:")
                    modulo_peliculas.leer_contenido_peliculas(matriz_peliculas)

                elif subopcion_peliculas == 'e': #Mostrar reporte
                    modulo_peliculas.imprimir_matriz_peliculas(matriz_peliculas)
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
                    modulo_registro_vistas.crear_contenido_registro_vistas(matriz_registro_vistas, matriz_usuarios, matriz_peliculas)

                    print("\nRegistro agregado con éxito.")
                    print("\nContenido registrado:")
                    modulo_registro_vistas.leer_contenido_registro_vistas(matriz_registro_vistas)
                        
                elif subopcion_registro == 'b':  # Listar Registros de Vista
                    print("\nContenido registrado:")
                    registros_ordenados = sorted(matriz_registro_vistas, key=lambda x: x[2])# Ordenar la lista por apellido

                    # Imprimir matriz
                    encabezado_registros = ["ID registro","ID usuario", "Apellido", "ID P/S", "Titulo", "Estado", "Clasificacion"]
                    registros = [dict(zip(encabezado_registros, fila)) for fila in registros_ordenados]
                    
                    for vistas in registros: # Imprimir los diccionarios
                        print(vistas)
                    print()

                elif subopcion_registro == 'c':  # Actualizar Registro de Vista
                    print("\nActualizar contenido:")

                    modulo_registro_vistas.actualizar_contenido_registro_vistas(matriz_registro_vistas, matriz_usuarios, matriz_peliculas)

                    print("\nContenido actualizado:")
                    modulo_registro_vistas.leer_contenido_registro_vistas(matriz_registro_vistas)

                elif subopcion_registro == 'd':  # Eliminar Registro de Vista
                    modulo_registro_vistas.eliminar_contenido_registro_vistas(matriz_registro_vistas)

                    print("\nContenido después de la eliminación:")
                    modulo_registro_vistas.leer_contenido_registro_vistas(matriz_registro_vistas)

                elif subopcion_registro == 'e':  # Generar Reporte
                    modulo_registro_vistas.imprimir_matriz_registro_vistas(matriz_registro_vistas)
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