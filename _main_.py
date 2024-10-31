import modulo_menu, modulo_peliculas, modulo_usuarios, modulo_registro_vistas, modulo_sinopsis, modulo_calificaciones

def _main_():
    matriz_usuarios = [
    [1, "Juan", "Pérez", "12.345.678", "juan.perez@gmail.com"],
    [2, "Ana", "García", "23.456.789", "ana.garcia@yahoo.com"],
    [3, "Luis", "Martínez", "34.567.890", "luis.martinez@hotmail.com"],
    [4, "Laura", "López", "45.678.901", "laura.lopez@gmail.com"],
    [5, "Carlos", "Ramírez", "56.789.012", "carlos.ramirez@outlook.com"],
    [6, "María", "Sánchez", "67.890.123", "maria.sanchez@gmail.com"],
    [7, "Pedro", "Gómez", "78.901.234", "pedro.gomez@icloud.com"],
    [8, "Sofía", "Torres", "89.012.345", "sofia.torres@gmail.com"]]

    matriz_peliculas = [
        [1, "El Señor de Los Anillos", "Película", "Fantasía", 2001, "178 minutos"],
        [2, "Breaking Bad", "Serie", "Drama", 2008, "5 temporadas"],
        [3, "Matrix", "Película", "Ciencia ficción", 1999, "136 minutos"],
        [4, "Stranger Things", "Serie", "Terror", 2016, "4 temporadas"],
        [5, "Inception", "Película", "Acción", 2010, "148 minutos"],
        [6, "The Crown", "Serie", "Histórico", 2016, "5 temporadas"],
        [7, "Interstellar", "Película", "Ciencia ficción", 2014, "169 minutos"],
        [8, "La Casa de Papel", "Serie", "Crimen", 2017, "5 temporadas"]]

    matriz_registro_vistas = [
        [1, 4, 'López', 1, 'El Señor de los Anillos', 'En curso', 0],
        [2, 2, 'García', 3, 'Matrix', 'Terminada', 9],
        [3, 5, 'Ramírez', 5, 'Inception', 'Pendiente', 0],
        [4, 6, 'Sánchez', 6, 'The Crown', 'Terminada', 10],
        [5, 1, 'Pérez', 2, 'Breaking Bad', 'Terminada', 10],
        [6, 3, 'Martínez', 4, 'Stranger Things', 'En curso', 0],
        [7, 7, 'Gómez', 7, 'Interstellar', 'Pendiente', 0],
        [8, 8, 'Torres', 8, 'La Casa de Papel', 'Terminada', 8]]

    dic_opciones={"1":"usuarios", "2":"peliculas y series", "3":"registros vistas", "4":"salir"} #Uso de diccionarios
    dnis_existentes = {usuario[3] for usuario in matriz_usuarios} # Conjunto para almacenar DNIs existentes
    correos_existentes={usuario[4] for usuario in matriz_usuarios} #conjunto de correo
    titulos_existentes={titulo[1] for titulo in matriz_peliculas}
    modulo_sinopsis.eliminar_sinopsis_no_existentes("sinopsis.txt", matriz_peliculas)

    salir=True
    while salir:
        modulo_menu.mostrar_menu()
        opcion = input("Seleccione una opción del menú principal: ")
        if opcion in dic_opciones:

            if dic_opciones[opcion] == "usuarios":  # Menú de Usuarios
                submenu_activo = True  # Bandera para controlar el bucle del submenú de usuarios
                while submenu_activo:
                    modulo_menu.mostrar_submenu(opcion)
                    subopcion_usuarios = input("Seleccione una opción del submenú de Usuarios: ").strip().lower()

                    if subopcion_usuarios == 'a': # Agregar Usuario
                        modulo_usuarios.crear_matriz_usuarios(matriz_usuarios, dnis_existentes, correos_existentes)
                        modulo_usuarios.leer_matriz_usuarios(matriz_usuarios)
                        
                    elif subopcion_usuarios == 'b':# Actualizar Usuario
                        modulo_usuarios.imprimir_matriz_usuarios(matriz_usuarios)
                        modulo_usuarios.actualizar_matriz_usuarios(matriz_usuarios, dnis_existentes, correos_existentes)
                        modulo_usuarios.leer_matriz_usuarios(matriz_usuarios)

                    elif subopcion_usuarios == 'c': # Eliminar Usuarios
                        modulo_usuarios.imprimir_matriz_usuarios(matriz_usuarios)
                        modulo_usuarios.eliminar_matriz_usuarios(matriz_usuarios)
                        modulo_usuarios.leer_matriz_usuarios(matriz_usuarios)

                    elif subopcion_usuarios == 'd': # Generar reporte
                        modulo_usuarios.imprimir_matriz_usuarios(matriz_usuarios)
                    
                    elif subopcion_usuarios == 'e': # Volver al menú principal
                        submenu_activo = False  # Salir del submenú volviendo al menú principal

                    else:
                        print("\nOpción no válida, intente nuevamente.")

            elif dic_opciones[opcion] == "peliculas y series": #Menu de peliculas/series
                submenu_activo = True  # Bandera para controlar el bucle del submenú
                while submenu_activo:
                    modulo_menu.mostrar_submenu(opcion)
                    subopcion_peliculas = input("Seleccione una opción del submenú de Películas/Series: ").strip().lower()

                    if subopcion_peliculas == 'a': #Agregar peliculas
                        modulo_peliculas.crear_matriz_peliculas(matriz_peliculas, titulos_existentes)
                        modulo_peliculas.leer_matriz_peliculas(matriz_peliculas)

                    elif subopcion_peliculas == 'b': #Actualizar
                        modulo_peliculas.imprimir_matriz_peliculas(matriz_peliculas)
                        modulo_peliculas.actualizar_matriz_peliculas(matriz_peliculas, titulos_existentes)
                        modulo_peliculas.leer_matriz_peliculas(matriz_peliculas)

                    elif subopcion_peliculas == 'c': #Eliminar
                        modulo_peliculas.imprimir_matriz_peliculas(matriz_peliculas)
                        modulo_peliculas.eliminar_matriz_peliculas(matriz_peliculas)
                        modulo_peliculas.leer_matriz_peliculas(matriz_peliculas)

                    elif subopcion_peliculas == 'd': #Mostrar reporte
                        modulo_peliculas.imprimir_matriz_peliculas(matriz_peliculas)

                    elif subopcion_peliculas == "e":
                        modulo_menu.submenu_sinopsis("sinopsis.txt", matriz_peliculas)
                    
                    elif subopcion_peliculas == 'f': #Volver al menú principal
                        modulo_menu.submenu_calificaciones(matriz_peliculas, matriz_registro_vistas)
                        
                    elif subopcion_peliculas=="g":
                        submenu_activo = False  #Bandera para salir del bucle del submenú

                    else:
                        print("Opción no válida, intente nuevamente.")

            elif dic_opciones[opcion] == "registros vistas": #Menu registro vistas
                submenu_activo = True  # Bandera para controlar el bucle del submenú
                while submenu_activo:
                    modulo_menu.mostrar_submenu(opcion)
                    subopcion_registro = input("Seleccione una opción del submenú de Registro: ").strip().lower()

                    if subopcion_registro == 'a':  # Agregar Registro de Vistas
                        modulo_registro_vistas.crear_matriz_registro_vistas(matriz_registro_vistas, matriz_usuarios, matriz_peliculas)
                        modulo_registro_vistas.leer_matriz_registro_vistas(matriz_registro_vistas)

                    elif subopcion_registro == 'b':  # Actualizar Registro de Vista
                        modulo_registro_vistas.imprimir_matriz_registro_vistas(matriz_registro_vistas)
                        modulo_registro_vistas.actualizar_matriz_registro_vistas(matriz_registro_vistas, matriz_usuarios, matriz_peliculas)
                        modulo_registro_vistas.leer_matriz_registro_vistas(matriz_registro_vistas)

                    elif subopcion_registro == 'c':  # Eliminar Registro de Vista
                        modulo_registro_vistas.imprimir_matriz_registro_vistas(matriz_registro_vistas)
                        modulo_registro_vistas.eliminar_matriz_registro_vistas(matriz_registro_vistas)
                        modulo_registro_vistas.leer_matriz_registro_vistas(matriz_registro_vistas)

                    elif subopcion_registro == 'd': # Generar Reporte
                        modulo_registro_vistas.imprimir_matriz_registro_vistas(matriz_registro_vistas)
                    
                    elif subopcion_registro == 'e': # Volver al menú principal
                        submenu_activo = False  # Salir del submenú volviendo al menú principal

                    else:
                        print("Opción no válida, intente nuevamente.")
            
            elif opcion == '4':  # Salir del programa
                print("\nSaliendo del programa")
                #modulo_sinopsis.eliminar_sinopsis_no_existentes("sinopsis.txt", matriz_peliculas)
                salir=False
        else:
            print("\nOpción inválida. Intente nuevamenete")

if __name__ == "__main__":
    _main_()