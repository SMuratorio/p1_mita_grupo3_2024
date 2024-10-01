import modulo_menu, modulo_peliculas, modulo_usuarios, modulo_registro_vistas

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

    dic_opciones={"1":"usuarios", "2":"peliculas y series", "3":"registros vistas", "4":"salir"} #Uso de diccionarios
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
                        modulo_usuarios.crear_matriz_usuarios(matriz_usuarios)
                        modulo_usuarios.leer_matriz_usuarios(matriz_usuarios)
                        
                    elif subopcion_usuarios == 'b': # Listar Usuarios
                        modulo_usuarios.listar_matriz_usuarios(matriz_usuarios)

                    elif subopcion_usuarios == 'c': # Actualizar Usuario
                        modulo_usuarios.actualizar_matriz_usuarios(matriz_usuarios)
                        modulo_usuarios.leer_matriz_usuarios(matriz_usuarios)

                    elif subopcion_usuarios == 'd': # Eliminar Usuarios
                        modulo_usuarios.eliminar_matriz_usuarios(matriz_usuarios)
                        modulo_usuarios.leer_matriz_usuarios(matriz_usuarios)

                    elif subopcion_usuarios == 'e': # Generar reporte
                        modulo_usuarios.imprimir_matriz_usuarios(matriz_usuarios)
                    
                    elif subopcion_usuarios == 'f': # Volver al menú principal
                        submenu_activo = False  # Salir del submenú volviendo al menú principal

                    else:
                        print("\nOpción no válida, intente nuevamente.")

            elif dic_opciones[opcion] == "peliculas y series": #Menu de peliculas/series
                submenu_activo = True  # Bandera para controlar el bucle del submenú
                while submenu_activo:
                    modulo_menu.mostrar_submenu(opcion)
                    subopcion_peliculas = input("Seleccione una opción del submenú de Películas/Series: ").strip().lower()

                    if subopcion_peliculas == 'a': #Agregar peliculas
                        modulo_peliculas.crear_matriz_peliculas(matriz_peliculas)
                        modulo_peliculas.leer_matriz_peliculas(matriz_peliculas)

                    elif subopcion_peliculas == 'b': #Listar películas/series
                        modulo_peliculas.listar_matriz_peliculas(matriz_peliculas)
                        
                    elif subopcion_peliculas == 'c': #Actualizar
                        modulo_peliculas.actualizar_matriz_peliculas(matriz_peliculas)
                        modulo_peliculas.leer_matriz_peliculas(matriz_peliculas)

                    elif subopcion_peliculas == 'd': #Eliminar
                        modulo_peliculas.eliminar_matriz_peliculas(matriz_peliculas)
                        modulo_peliculas.leer_matriz_peliculas(matriz_peliculas)

                    elif subopcion_peliculas == 'e': #Mostrar reporte
                        modulo_peliculas.imprimir_matriz_peliculas(matriz_peliculas)
                    
                    elif subopcion_peliculas == 'f': #Volver al menú principal
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
                            
                    elif subopcion_registro == 'b':  # Listar Registros de Vista
                        modulo_registro_vistas.listar_matriz_registro_vistas(matriz_registro_vistas)

                    elif subopcion_registro == 'c':  # Actualizar Registro de Vista
                        modulo_registro_vistas.actualizar_matriz_registro_vistas(matriz_registro_vistas, matriz_usuarios, matriz_peliculas)
                        modulo_registro_vistas.leer_matriz_registro_vistas(matriz_registro_vistas)

                    elif subopcion_registro == 'd':  # Eliminar Registro de Vista
                        modulo_registro_vistas.eliminar_matriz_registro_vistas(matriz_registro_vistas)
                        modulo_registro_vistas.leer_matriz_registro_vistas(matriz_registro_vistas)

                    elif subopcion_registro == 'e': # Generar Reporte
                        modulo_registro_vistas.imprimir_matriz_registro_vistas(matriz_registro_vistas)
                    
                    elif subopcion_registro == 'f': # Volver al menú principal
                        submenu_activo = False  # Salir del submenú volviendo al menú principal

                    else:
                        print("Opción no válida, intente nuevamente.")
            
            elif opcion == '4':  # Salir del programa
                print("\nSaliendo del programa")
                salir=False
        else:
            print("\nOpción inválida. Intente nuevamenete")

if __name__ == "__main__":
    _main_()