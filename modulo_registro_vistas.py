import modulo_validar, modulo_matriz
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

matriz_usuarios=modulo_matriz.archivo_a_matriz("usuarios.txt")
matriz_peliculas=modulo_matriz.archivo_a_matriz("peliculas.txt")
matriz_registro_vistas=modulo_matriz.archivo_a_matriz("registros.txt")

#-----------------
# Agregar registro
#-----------------
def form_agregar_registro(matriz_registro_vistas, matriz_usuarios, matriz_peliculas):
    root = tk.Tk()
    root.title("Agregar Registro")
    root.geometry("400x400")

    # Función para habilitar el campo "Calificación" si el estado es "terminada"
    def verificar_estado(event):
        if entry_estado.get().lower() == "terminada":
            entry_calificacion.config(state="normal")  # Habilitar el campo "Calificación"
        else:
            entry_calificacion.config(state="disabled")  # Deshabilitar el campo "Calificación"

    # Etiqueta para el título
    titulo = tk.Label(root, text="Agregar Registro", font=("Arial", 16))
    titulo.pack(pady=10)

    # Campo para ID Usuario
    tk.Label(root, text="ID Usuario:", font=("Arial", 12)).pack(pady=5)
    entry_usuario_id = tk.Entry(root, font=("Arial", 12))
    entry_usuario_id.pack(pady=5)

    # Campo para ID Película/Serie
    tk.Label(root, text="ID Película/Serie:", font=("Arial", 12)).pack(pady=5)
    entry_pelicula_id = tk.Entry(root, font=("Arial", 12))
    entry_pelicula_id.pack(pady=5)

    # Campo para Estado
    tk.Label(root, text="Estado:", font=("Arial", 12)).pack(pady=5)
    entry_estado = tk.Entry(root, font=("Arial", 12))
    entry_estado.pack(pady=5)
    entry_estado.bind("<KeyRelease>", verificar_estado)  # Verificar el estado en cada pulsación de tecla

    # Campo para Calificación
    tk.Label(root, text="Calificación:", font=("Arial", 12)).pack(pady=5)
    entry_calificacion = tk.Entry(root, font=("Arial", 12), state="disabled")  # Inicialmente deshabilitado
    entry_calificacion.pack(pady=5)

    # Botón para guardar
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: agregar_datos(root, entry_usuario_id, entry_pelicula_id, entry_estado, entry_calificacion, matriz_registro_vistas, matriz_usuarios, matriz_peliculas)
    )
    btn_guardar.pack(pady=20)

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.pack(pady=10)

    root.mainloop()

def agregar_datos(root, entry_usuario_id, entry_pelicula_id, entry_estado, entry_calificacion, matriz_registro_vistas, matriz_usuarios, matriz_peliculas):
    try:
        # Obtener los valores de los campos
        usuario_id = int(entry_usuario_id.get())
        pelicula_id = int(entry_pelicula_id.get())
        estado = entry_estado.get().capitalize()
        calificacion = entry_calificacion.get() if estado == "terminada" else "0"

        # Validar que los campos no estén vacíos
        if not estado or not entry_usuario_id.get() or not entry_pelicula_id.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios. No se puede dejar ninguno en blanco.")
            return

        # Validar que los IDs sean válidos
        if usuario_id not in [usuario[0] for usuario in matriz_usuarios]:
            messagebox.showerror("Error", "ID de usuario no válido.")
            return

        if pelicula_id not in [pelicula[0] for pelicula in matriz_peliculas]:
            messagebox.showerror("Error", "ID de película/serie no válido.")
            return

        if not modulo_validar.validar_estado(estado):
            messagebox.showerror("Error", "Estado no válido. Los estados válidos son: 'en curso', 'pendiente' o 'terminada'.")
            return

        # Validar calificación si el estado es "terminada"
        if estado == "terminada" and (not modulo_validar.validar_calificacion(calificacion)):
            messagebox.showerror("Error", "Calificación no válida. Debe ser un número entre 1 y 10.")
            return

        # Buscar el apellido del usuario usando el ID
        apellido_usuario = next((usuario[1] for usuario in matriz_usuarios if usuario[0] == usuario_id), None)
        if not apellido_usuario:
            messagebox.showerror("Error", "No se encontró el apellido del usuario.")
            return

        # Buscar el título de la película usando el ID
        titulo_pelicula = next((pelicula[1] for pelicula in matriz_peliculas if pelicula[0] == pelicula_id), None)
        if not titulo_pelicula:
            messagebox.showerror("Error", "No se encontró el título de la película/serie.")
            return

        # Guardar el registro
        matriz_registro_vistas.append([len(matriz_registro_vistas) + 1, usuario_id,apellido_usuario,pelicula_id ,titulo_pelicula ,estado, calificacion])
        modulo_matriz.guardar_matriz_en_archivo("registros.txt", matriz_registro_vistas)
        messagebox.showinfo("Éxito", "Registro agregado correctamente.")
        root.destroy()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos en todos los campos.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {e}")

#--------------------
# Actualizar registro
#--------------------
def form_actualizar_registro(id_registro, datos, matriz_registro_vistas, tree):
    root = tk.Tk()
    root.title("Actualizar Registro de Vista")
    root.geometry("400x400") 

    # Etiqueta para el título
    titulo = tk.Label(root, text=f"Actualizar Registro de Vista - ID: {id_registro}", font=("Arial", 16))
    titulo.pack(pady=10)

    def verificar_estado(event):
        if entry_estado.get().lower() == "terminada":
            entry_calificacion.config(state="normal")  # Habilitar el campo "Calificación"
        else:
            entry_calificacion.config(state="disabled")  # Deshabilitar el campo "Calificación"

    # Campo para ID de Usuario
    tk.Label(root, text="ID de Usuario:", font=("Arial", 12)).pack(pady=5)
    entry_usuario_id = tk.Entry(root, font=("Arial", 12))
    entry_usuario_id.insert(0, datos[1])  # Insertar el ID de Usuario
    entry_usuario_id.pack(pady=5)

    # Campo para ID de Película/Serie
    tk.Label(root, text="ID de Película/Serie:", font=("Arial", 12)).pack(pady=5)
    entry_pelicula_id = tk.Entry(root, font=("Arial", 12))
    entry_pelicula_id.insert(0, datos[3])  # Insertar el ID de Película/Serie
    entry_pelicula_id.pack(pady=5)

    # Campo para Estado
    tk.Label(root, text="Estado:", font=("Arial", 12)).pack(pady=5)
    entry_estado = tk.Entry(root, font=("Arial", 12))
    entry_estado.pack(pady=5)
    entry_estado.insert(0, datos[5])
    entry_estado.bind("<KeyRelease>", verificar_estado)

    # Campo para Calificación
    tk.Label(root, text="Calificación:", font=("Arial", 12)).pack(pady=5)
    entry_calificacion = tk.Entry(root, font=("Arial", 12))
    entry_calificacion.insert(0, datos[6])  # Insertar la calificación (si existe)
    entry_calificacion.pack(pady=5)
    entry_calificacion.config(state="disabled")  # Deshabilitar al principio

    # Botón para guardar
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: actualizar_registro(root, id_registro,entry_usuario_id, entry_pelicula_id ,entry_estado, entry_calificacion, matriz_registro_vistas, tree)
    )
    btn_guardar.pack(pady=20)

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.pack(pady=10)

    root.mainloop()

def actualizar_registro(root, id_registro, entry_usuario_id, entry_pelicula_id, entry_estado, entry_calificacion, matriz_registro_vistas, tree):
    usuario_id =int(entry_usuario_id.get())  # Obtener el nuevo ID de usuario
    pelicula_id = int(entry_pelicula_id.get())  # Obtener el nuevo ID de película
    estado = entry_estado.get().lower()
    calificacion = entry_calificacion.get()

    if not estado or not pelicula_id or not usuario_id:
        messagebox.showwarning("Campo incompleto", "Por favor, ingrese el estado.")
        return

    if usuario_id not in [usuario[0] for usuario in matriz_usuarios]:
        messagebox.showerror("Error", "ID de usuario no válido.")
        return

    if pelicula_id not in [pelicula[0] for pelicula in matriz_peliculas]:
        messagebox.showerror("Error", "ID de película/serie no válido.")
        return
    
    # Validar el estado
    if not modulo_validar.validar_estado(estado):
        messagebox.showerror("Error", "Estado no válido. Los estados válidos son: 'en curso', 'pendiente' o 'terminada'.")
        return

    # Si el estado es "terminada", validamos la calificación
    if estado == "terminada":
        if not calificacion:
            messagebox.showerror("Error", "Debe ingresar una calificación para el estado 'terminada'.")
            return
        if not modulo_validar.validar_calificacion(calificacion):
            messagebox.showerror("Error", "La calificación debe ser un número entre 1 y 10.")
            return
    else:
        calificacion = 0  # Asignar calificación 0 si no es 'terminada'
    
    apellido_usuario = next((usuario[1] for usuario in matriz_usuarios if usuario[0] == usuario_id), None)
    if not apellido_usuario:
        messagebox.showerror("Error", "No se encontró el apellido del usuario.")
        return

        # Buscar el título de la película usando el ID
    titulo_pelicula = next((pelicula[1] for pelicula in matriz_peliculas if pelicula[0] == pelicula_id), None)
    if not titulo_pelicula:
        messagebox.showerror("Error", "No se encontró el título de la película/serie.")
        return
    
    # Buscar el registro y actualizarlo
    for registro in matriz_registro_vistas:
        if registro[0] == id_registro:
            # Actualizar los valores
            registro[1] = usuario_id  # Actualizar ID de Usuario
            registro[2] = apellido_usuario
            registro[3] = pelicula_id  # Actualizar ID de Película
            registro[4] = titulo_pelicula
            registro[5] = estado  # Actualizar el estado
            registro[6] = calificacion  # Actualizar la calificación
            break

    # Guardar la matriz actualizada en el archivo
    modulo_matriz.guardar_matriz_en_archivo("registros.txt", matriz_registro_vistas)
    refrescar_grilla(tree, matriz_registro_vistas)
    messagebox.showinfo("Éxito", "Registro actualizado correctamente.")
    root.destroy()

def refrescar_grilla(tree, matriz_registro_vistas):
    for item in tree.get_children():
        tree.delete(item)
  
    matriz_registros_ordenados = sorted(matriz_registro_vistas, key=lambda x:str(x[2]))

    for registro in matriz_registros_ordenados:
        tree.insert("", tk.END, values=registro)

#-----------------
# Generar reporte
#-----------------
def imprimir_matriz_registro_vistas_tk(contenido_registro_vistas, modo="normal"):
    root = tk.Tk()
    root.title("Matriz de Registros de Vistas")

    # Crear el Treeview con las columnas necesarias
    tree = ttk.Treeview(root, columns=("ID Registro", "ID Usuario", "Apellido", "ID Película/Serie", "Título", "Estado", "Calificación"), show="headings")
    
    tree.heading("ID Registro", text="ID Registro")
    tree.heading("ID Usuario", text="ID Usuario")
    tree.heading("Apellido", text="Apellido")
    tree.heading("ID Película/Serie", text="ID Película/Serie")
    tree.heading("Título", text="Título")
    tree.heading("Estado", text="Estado")
    tree.heading("Calificación", text="Calificación")

    # Ajustar el ancho de las columnas
    tree.column("ID Registro", width=100, anchor=tk.CENTER)
    tree.column("ID Usuario", width=100, anchor=tk.CENTER)
    tree.column("Apellido", width=150, anchor="w")
    tree.column("ID Película/Serie", width=150, anchor=tk.CENTER)
    tree.column("Título", width=150, anchor="w")
    tree.column("Estado", width=100, anchor="w")
    tree.column("Calificación", width=100, anchor="w")

    # Ordenar la matriz por apellido (índice 2)
    matriz_registros_ordenados = sorted(contenido_registro_vistas, key=lambda x: str(x[2]))

    # Insertar los datos en el Treeview
    for registro in matriz_registros_ordenados:
        tree.insert("", tk.END, values=registro)

    tree.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    # Mostrar los botones solo si el modo es "normal"
    if modo == "normal":
        def obtener_seleccion(tree):
            item_seleccionado = tree.selection()
            if not item_seleccionado:
                return None
            valores = tree.item(item_seleccionado, "values")
            return valores

        def actualizar_seleccion():
            seleccion = obtener_seleccion(tree)
            if seleccion:
                id_registro= int(seleccion[0])  # Obtener el ID como entero
                form_actualizar_registro(id_registro, seleccion, matriz_registro_vistas, tree)
            else:
                messagebox.showwarning("Sin selección", "Por favor, seleccione un usuario.")
        
        def eliminar_seleccion():
            seleccion = obtener_seleccion(tree)
            if seleccion:
                id_seleccionado = int(seleccion[0])
                matriz_registro_vistas[:] = [registro for registro in matriz_registro_vistas if registro[0] != id_seleccionado]
                
                # Eliminar el registro de la vista (Treeview)
                tree.delete(tree.selection()[0])
                modulo_matriz.guardar_matriz_en_archivo("registros.txt", matriz_registro_vistas)
                root.destroy()
                messagebox.showinfo("Éxito", "Registro eliminado.")
            else:
                messagebox.showwarning("Sin selección", "Por favor, seleccione un registro para eliminar.")
        
        # Botón para actualizar el registro seleccionado
        btn_actualizar = tk.Button(root, text="Actualizar", command=actualizar_seleccion)
        btn_actualizar.pack(pady=10)

        # Botón para eliminar el registro seleccionado
        btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_seleccion)
        btn_eliminar.pack(pady=10)

    # Botón para cerrar la ventana
    boton_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
    boton_cerrar.pack(pady=20)

    # Ejecutar la aplicación Tkinter
    root.mainloop()
