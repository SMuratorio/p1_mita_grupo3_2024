import modulo_menu, modulo_peliculas, modulo_usuarios, modulo_registro_vistas, modulo_matriz

def _main_():
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
                        modulo_usuarios.crear_matriz_usuarios()
                        
                    elif subopcion_usuarios == 'b':# Actualizar Usuario
                        modulo_usuarios.imprimir_matriz_usuarios(modulo_matriz.archivo_a_matriz("usuarios.txt")) 
                        modulo_usuarios.actualizar_matriz_usuarios()

                    elif subopcion_usuarios == 'c': # Eliminar Usuarios
                        modulo_usuarios.imprimir_matriz_usuarios(modulo_matriz.archivo_a_matriz("usuarios.txt")) 
                        modulo_usuarios.eliminar_matriz_usuarios()

                    elif subopcion_usuarios == 'd': # Generar reporte
                        modulo_usuarios.imprimir_matriz_usuarios(modulo_matriz.archivo_a_matriz("usuarios.txt"))
                    
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
                        modulo_peliculas.crear_matriz_peliculas()

                    elif subopcion_peliculas == 'b': #Actualizar
                        modulo_peliculas.imprimir_matriz_peliculas(modulo_matriz.archivo_a_matriz("peliculas.txt")) 
                        modulo_peliculas.actualizar_matriz_peliculas()

                    elif subopcion_peliculas == 'c': #Eliminar
                        modulo_peliculas.imprimir_matriz_peliculas(modulo_matriz.archivo_a_matriz("peliculas.txt")) 
                        modulo_peliculas.eliminar_matriz_peliculas()

                    elif subopcion_peliculas == 'd': #Mostrar reporte
                        modulo_peliculas.imprimir_matriz_peliculas(modulo_matriz.archivo_a_matriz("peliculas.txt"))

                    elif subopcion_peliculas == "e":
                        modulo_menu.submenu_sinopsis("sinopsis.txt", modulo_matriz.archivo_a_matriz("peliculas.txt"))
                    
                    elif subopcion_peliculas == 'f': #Volver al menú principal
                        modulo_menu.submenu_calificaciones()
                        
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
                        modulo_registro_vistas.crear_matriz_registro_vistas()

                    elif subopcion_registro == 'b':  # Actualizar Registro de Vista
                        modulo_registro_vistas.imprimir_matriz_registro_vistas(modulo_matriz.archivo_a_matriz("registros.txt"))
                        modulo_registro_vistas.actualizar_matriz_registro_vistas()

                    elif subopcion_registro == 'c':  # Eliminar Registro de Vista
                        modulo_registro_vistas.imprimir_matriz_registro_vistas(modulo_matriz.archivo_a_matriz("registros.txt"))
                        modulo_registro_vistas.eliminar_matriz_registro_vistas()

                    elif subopcion_registro == 'd': # Generar Reporte
                        modulo_registro_vistas.imprimir_matriz_registro_vistas(modulo_matriz.archivo_a_matriz("registros.txt"))
                    
                    elif subopcion_registro == 'e': # Volver al menú principal
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