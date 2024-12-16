import modulo_calificaciones, modulo_genero, modulo_usuarios, modulo_matriz, modulo_peliculas, modulo_registro_vistas, modulo_sinopsis
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
    root.geometry("700x400")

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
    tk.Button(root, text="Agregar/Actualizar/Eliminar Genero", font=("Arial", 12), command=modulo_genero.imprimir_generos_tk).pack(pady=5)
    tk.Button(root, text="Leer Sinopsis", font=("Arial", 12), command=modulo_sinopsis.leer_sinopsis).pack(pady=5)
    tk.Button(root, text="Ver Calificaciones", font=("Arial", 12), command=mostrar_submenu_calificaciones).pack(pady=5)
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
    tk.Button(root, text="Agregar Registro", font=("Arial", 12), command=lambda: modulo_registro_vistas.form_agregar_registro()).pack(pady=5)
    tk.Button(root, text="Actualizar/Eliminar Registro", font=("Arial", 12), command=lambda: modulo_registro_vistas.imprimir_matriz_registro_vistas_tk(modo="normal")).pack(pady=5)
    tk.Button(root, text="Generar Reporte", font=("Arial", 12), command=lambda: modulo_registro_vistas.imprimir_matriz_registro_vistas_tk(modo="reporte")).pack(pady=5)
    tk.Button(root, text="Volver al Menú Principal", font=("Arial", 12), command=volver_menu_principal).pack(pady=20)

    # Iniciar el bucle de eventos del submenú
    root.mainloop()

def mostrar_submenu_calificaciones():
    # Crear la ventana del submenú
    ventana_calificaciones = tk.Toplevel()
    ventana_calificaciones.title("Menú de Calificaciones")
    ventana_calificaciones.geometry("400x300")

    # Etiqueta de título
    tk.Label(ventana_calificaciones, text="Opciones de Promedios de Calificaciones", font=("Arial", 16)).pack(pady=10)

    # Botones para las opciones
    tk.Button(
        ventana_calificaciones,
        text="Calificaciones por Género",
        font=("Arial", 12),
        command=lambda: modulo_calificaciones.mostrar_promedios(modulo_calificaciones.promedio_por_genero, "Promedios de Calificaciones por Género")
    ).pack(pady=10)

    tk.Button(
        ventana_calificaciones,
        text="Calificaciones por Título",
        font=("Arial", 12),
        command=lambda: modulo_calificaciones.mostrar_promedios(modulo_calificaciones.promedio_peliculas, "Promedios de Calificaciones por Título")
    ).pack(pady=10)

    # Botón para volver al menú principal
    tk.Button(ventana_calificaciones, text="Volver al Menú Principal", font=("Arial", 12), command=ventana_calificaciones.destroy).pack(pady=20)
