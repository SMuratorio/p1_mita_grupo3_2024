import modulo_sinopsis, modulo_validar, modulo_calificaciones, modulo_genero, modulo_usuarios, modulo_matriz, modulo_peliculas, modulo_registro_vistas
import tkinter as tk

mr = modulo_matriz.archivo_a_matriz("registros.txt")
mp = modulo_matriz.archivo_a_matriz("peliculas.txt")
mu = modulo_matriz.archivo_a_matriz("usuarios.txt")

#-----------------
# MENU TKINTER
#-----------------
def mostrar_menu_tkinter():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Aplicación de Seguimiento de Películas y Series Vistas")
    root.geometry("600x300")

    # Etiqueta para el título
    titulo = tk.Label(root, text="Menú Principal", font=("Arial", 16))
    titulo.pack(pady=20)

    # Botón para "Usuarios"
    btn_usuarios = tk.Button(root, text="Usuarios", font=("Arial", 14), width=20, command=lambda: [root.destroy(), mostrar_submenu_usuarios_tkinter()])
    btn_usuarios.pack(pady=5)

    # Botón para "Películas/Series"
    btn_peliculas_series = tk.Button(root, text="Películas/Series", font=("Arial", 14), width=20, command=lambda: [root.destroy(), mostrar_submenu_peliculas_tkinter()])
    btn_peliculas_series.pack(pady=5)

    # Botón para "Registros Vistos"
    btn_registros_vistos = tk.Button(root, text="Registros Vistos", font=("Arial", 14), width=20, command=lambda:  [root.destroy(), mostrar_submenu_registros_tkinter()] )
    btn_registros_vistos.pack(pady=5)

    # Botón para "Salir"
    btn_salir = tk.Button(root, text="Salir", font=("Arial", 14), width=20, command=root.destroy)
    btn_salir.pack(pady=20)

    # Iniciar el bucle de eventos
    root.mainloop()

#-----------------
# SUBMENU TKINTER
#-----------------
def mostrar_submenu_usuarios_tkinter():
    # Crear una ventana para el submenú
    root = tk.Tk()
    root.title("Menú Usuarios")
    root.geometry("600x300")

    # Etiqueta para el título
    titulo = tk.Label(root, text="Menú de Usuarios", font=("Arial", 16))
    titulo.pack(pady=10)

    def volver_menu_principal():
        root.destroy()
        mostrar_menu_tkinter()

    # Botones para las opciones del submenú
    tk.Button(root, text="Agregar Usuario", font=("Arial", 12), command=lambda: modulo_usuarios.form_agregar_usuario(mu)).pack(pady=5)
    tk.Button(root, text="Actualizar/Eliminar Usuario", font=("Arial", 12), command=lambda: modulo_usuarios.imprimir_matriz_usuarios_tk(mu, modo="normal")).pack(pady=5)
    tk.Button(root, text="Generar Reporte", font=("Arial", 12), command=lambda: modulo_usuarios.imprimir_matriz_usuarios_tk(mu, modo="reporte")).pack(pady=5)
    tk.Button(root, text="Volver al Menú Principal", font=("Arial", 12), command=volver_menu_principal).pack(pady=20)

    # Iniciar el bucle de eventos del submenú
    root.mainloop()

def mostrar_submenu_peliculas_tkinter():
    # Crear una ventana para el submenú
    root = tk.Tk()
    root.title("Menú Peliculas y Series")
    root.geometry("600x300")

    # Etiqueta para el título
    titulo = tk.Label(root, text="Menú de Peliculas y Series", font=("Arial", 16))
    titulo.pack(pady=10)

    def volver_menu_principal():
        root.destroy()
        mostrar_menu_tkinter()

    # Botones para las opciones del submenú
    tk.Button(root, text="Agregar Película/Serie", font=("Arial", 12), command=lambda: modulo_peliculas.form_agregar_pelicula(mp)).pack(pady=5)
    tk.Button(root, text="Actualizar/Eliminar Película/Serie", font=("Arial", 12), command=lambda: modulo_peliculas.imprimir_matriz_peliculas_tk(mp, modo="normal")).pack(pady=5)
    tk.Button(root, text="Generar Reporte", font=("Arial", 12), command=lambda: modulo_peliculas.imprimir_matriz_peliculas_tk(mp, modo="reporte")).pack(pady=5)
    tk.Button(root, text="Volver al Menú Principal", font=("Arial", 12), command=volver_menu_principal).pack(pady=20)

    # Iniciar el bucle de eventos del submenú
    root.mainloop()

def mostrar_submenu_registros_tkinter():
    # Crear una ventana para el submenú
    root = tk.Tk()
    root.title("Menú Usuarios")
    root.geometry("600x300")

    # Etiqueta para el título
    titulo = tk.Label(root, text="Menú de Registros Vistas", font=("Arial", 16))
    titulo.pack(pady=10)

    def volver_menu_principal():
        root.destroy()
        mostrar_menu_tkinter()

    
    # Botones para las opciones del submenú
    tk.Button(root, text="Agregar Registro", font=("Arial", 12), command=lambda: modulo_registro_vistas.form_agregar_registro(mr, mu, mp)).pack(pady=5)
    tk.Button(root, text="Actualizar/Eliminar Registro", font=("Arial", 12), command=lambda: modulo_registro_vistas.imprimir_matriz_registro_vistas_tk(mr, modo="normal")).pack(pady=5)
    tk.Button(root, text="Generar Reporte", font=("Arial", 12), command=lambda: modulo_registro_vistas.imprimir_matriz_registro_vistas_tk(mr, modo="reporte")).pack(pady=5)
    tk.Button(root, text="Volver al Menú Principal", font=("Arial", 12), command=volver_menu_principal).pack(pady=20)

    # Iniciar el bucle de eventos del submenú
    root.mainloop()


def submenu_sinopsis(archivo, matriz_peliculas):
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == "s":
        print("\nOpciones de Sinopsis")
        print("1. Leer Sinopsis")
        print("2. Actualizar Sinopsis")
        print("3. Eliminar sinopsis")
        print("0. Regresar al menu principal")

        try:
            opcion_sub = int(input("Seleccione una opción: ").strip())
            if opcion_sub not in range(0, 4):
                raise ValueError  # Lanza una excepción si el número está fuera del rango
            
            if opcion_sub == 1:
                modulo_sinopsis.leer_sinopsis(archivo, matriz_peliculas)
                opcion_seleccionada = modulo_validar.obtener_opcion(primera_consulta=False)
            elif opcion_sub == 2:
                modulo_sinopsis.actualizar_sinopsis(archivo, matriz_peliculas)
                opcion_seleccionada = modulo_validar.obtener_opcion(primera_consulta=False)
            elif opcion_sub == 3:
                modulo_sinopsis.eliminar_sinopsis(archivo, matriz_peliculas)
                opcion_seleccionada = modulo_validar.obtener_opcion(primera_consulta=False)
            elif opcion_sub == 0:
                print("Regresando al menú principal.")
                opcion_seleccionada = "n"
        
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 0 y 3.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
        
def submenu_calificaciones():
    opcion_seleccionada=modulo_validar.obtener_opcion()
    while opcion_seleccionada=="s":
        print("\nOpciones de Promedios de calificaciones")
        print("1. Calificiones por genero")
        print("2. Calificaciones por titulo")
        print("0. Regresar al menu principal")

        try:
            opcion_sub = int(input("Seleccione una opción: ").strip())
            if opcion_sub not in range(0, 3):
                raise ValueError  # Lanza una excepción si el número está fuera del rango
            
            if opcion_sub == 1:
                modulo_calificaciones.imprimir_promedios(modulo_calificaciones.promedio_por_genero, "Promedios de Calificación por Género")
                opcion_seleccionada=modulo_validar.obtener_opcion(primera_consulta=False)
            elif opcion_sub == 2:
                modulo_calificaciones.imprimir_promedios(modulo_calificaciones.promedio_peliculas, "Promedios de Calificación por Película")  
                opcion_seleccionada=modulo_validar.obtener_opcion(primera_consulta=False)
            elif opcion_sub == 0:
                print("Regresando al menú principal.")
                opcion_seleccionada="n"
        
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 0 y 2.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

def submenu_genero():
    opcion_seleccionada=modulo_validar.obtener_opcion()
    while opcion_seleccionada=="s":
        print("\nSubmenú de gestión de géneros")
        print("1: Agregar un nuevo género")
        print("2: Actualizar un género existente")
        print("3: Eliminar un género")
        print("0: Volver al submenú de generos")
        
        try:
            opcion_sub = int(input("Seleccione una opción: ").strip())
            if opcion_sub not in range(0, 3):
                raise ValueError  # Lanza una excepción si el número está fuera del rango      
    
        
            if opcion_sub == 1:
                modulo_genero.agregar_genero(modulo_genero.dic_genero)
            elif opcion_sub == 2:
                modulo_genero.actualizar_genero()
            elif opcion_sub == 3:
                modulo_genero.eliminar_genero()
            elif opcion_sub == 0:
                print("Regresando...")
                opcion_seleccionada="n"
    
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 0 y 3.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
