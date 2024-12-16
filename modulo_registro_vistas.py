import modulo_matriz
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#-----------------
# Agregar registro
#-----------------
def form_agregar_registro():
    matriz_usuarios=modulo_matriz.archivo_a_matriz("usuarios.txt")
    matriz_peliculas=modulo_matriz.archivo_a_matriz("peliculas.txt")
    matriz_registro_vistas=modulo_matriz.archivo_a_matriz("registros.txt")

    root = tk.Tk()
    root.title("Agregar Registro")
    root.geometry("400x400")

    # Función para habilitar el campo "Calificación" si el estado es "terminada"
    def verificar_estado(event):
        if combo_estado.get().lower() == "terminada":
            entry_calificacion.config(state="normal")  # Habilitar el campo "Calificación"
        else:
            entry_calificacion.config(state="disabled")  # Deshabilitar el campo "Calificación"

    # Etiqueta para el título
    titulo = tk.Label(root, text="Agregar Registro", font=("Arial", 16))
    titulo.pack(pady=10)

    # Campo para ID Usuario
    tk.Label(root, text="Usuario:", font=("Arial", 12)).pack(pady=5)
    opciones_usuarios = [f"{usuario[1]} {usuario[2]}" for usuario in matriz_usuarios]
    combo_usuario = ttk.Combobox(root, values=opciones_usuarios, font=("Arial", 12), state="readonly")
    combo_usuario.pack(pady=5)

    # Campo para ID Película/Serie
    tk.Label(root, text="Película/Serie:", font=("Arial", 12)).pack(pady=5)
    opciones_peliculas = [pelicula[1] for pelicula in matriz_peliculas]
    combo_pelicula = ttk.Combobox(root, values=opciones_peliculas, font=("Arial", 12), state="readonly")
    combo_pelicula.pack(pady=5)

    # Campo para Estado
    tk.Label(root, text="Estado:", font=("Arial", 12)).pack(pady=5)
    opciones_estado = ["En curso", "Terminada", "Pendiente"]
    combo_estado = ttk.Combobox(root, values=opciones_estado, font=("Arial", 12), state="readonly")
    combo_estado.pack(pady=5)
    combo_estado.bind("<<ComboboxSelected>>", verificar_estado)

    # Campo para Calificación
    tk.Label(root, text="Calificación:", font=("Arial", 12)).pack(pady=5)
    entry_calificacion = tk.Entry(root, font=("Arial", 12), state="disabled")  # Inicialmente deshabilitado
    entry_calificacion.pack(pady=5)

    # Botón para guardar
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: agregar_datos(
            root, combo_usuario, combo_pelicula, combo_estado, entry_calificacion, 
            matriz_registro_vistas, matriz_usuarios, matriz_peliculas
        )
    )
    btn_guardar.pack(pady=20)

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.pack(pady=10)

    root.mainloop()

def agregar_datos(root, combo_usuario, combo_pelicula, combo_estado, entry_calificacion, matriz_registro_vistas, matriz_usuarios, matriz_peliculas):
    try:
        # Obtener los valores seleccionados
        usuario_seleccionado = combo_usuario.get()
        pelicula_seleccionada = combo_pelicula.get()
        estado = combo_estado.get()
        calificacion = entry_calificacion.get() if estado.lower() == "terminada" else "0"

        # Validar selección de usuario y película
        if not usuario_seleccionado or not pelicula_seleccionada or not estado:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Obtener IDs correspondientes
        usuario = next(usuario for usuario in matriz_usuarios if f"{usuario[1]} {usuario[2]}" == usuario_seleccionado)
        pelicula_id = next(pelicula[0] for pelicula in matriz_peliculas if pelicula[1] == pelicula_seleccionada)

        # Validar calificación si el estado es "terminada"
        if estado.lower() == "terminada" and not calificacion.isdigit():
            messagebox.showerror("Error", "Calificación no válida. Debe ser un número.")
            return

        # Guardar el registro
        matriz_registro_vistas.append([len(matriz_registro_vistas) + 1, usuario[0], usuario[2], pelicula_id, pelicula_seleccionada, estado, calificacion])
        modulo_matriz.guardar_matriz_en_archivo("registros.txt", matriz_registro_vistas)
        messagebox.showinfo("Éxito", "Registro agregado correctamente.")
        root.destroy()

    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

#--------------------
# Actualizar registro
#--------------------
def form_actualizar_registro(id_registro, datos, tree):
    matriz_usuarios=modulo_matriz.archivo_a_matriz("usuarios.txt")
    matriz_peliculas=modulo_matriz.archivo_a_matriz("peliculas.txt")
    matriz_registro_vistas=modulo_matriz.archivo_a_matriz("registros.txt")

    root = tk.Tk()
    root.title("Actualizar Registro de Vista")
    root.geometry("400x400") 

    # Etiqueta para el título
    titulo = tk.Label(root, text=f"Actualizar Registro de Vista - ID: {id_registro}", font=("Arial", 16))
    titulo.pack(pady=10)

    def verificar_estado(event):
        if combo_estado.get().lower() == "terminada":
            entry_calificacion.config(state="normal")  # Habilitar el campo "Calificación"
        else:
            entry_calificacion.config(state="disabled")  # Deshabilitar el campo "Calificación"

    # Campo para ID de Usuario
    tk.Label(root, text="Usuario:", font=("Arial", 12)).pack(pady=5)
    opciones_usuarios = [f"{usuario[1]} {usuario[2]}" for usuario in matriz_usuarios]
    combo_usuario = ttk.Combobox(root, values=opciones_usuarios, font=("Arial", 12), state="readonly")
    combo_usuario.set(next(f"{usuario[1]} {usuario[2]}" for usuario in matriz_usuarios if usuario[0] == int(datos[1])))
    combo_usuario.pack(pady=5)

    # Campo para ID de Película/Serie
    tk.Label(root, text="Película/Serie:", font=("Arial", 12)).pack(pady=5)
    opciones_peliculas = [pelicula[1] for pelicula in matriz_peliculas]
    combo_pelicula = ttk.Combobox(root, values=opciones_peliculas, font=("Arial", 12), state="readonly")
    combo_pelicula.set(next(pelicula[1] for pelicula in matriz_peliculas if pelicula[0] == int(datos[3])))
    combo_pelicula.pack(pady=5)

    # Campo para Estado
    tk.Label(root, text="Estado:", font=("Arial", 12)).pack(pady=5)
    opciones_estado = ["En curso", "Terminada", "Pendiente"]
    combo_estado = ttk.Combobox(root, values=opciones_estado, font=("Arial", 12), state="readonly")
    combo_estado.set(datos[5])
    combo_estado.pack(pady=5)
    combo_estado.bind("<<ComboboxSelected>>", verificar_estado)

    # Campo para Calificación
    tk.Label(root, text="Calificación:", font=("Arial", 12)).pack(pady=5)
    entry_calificacion = tk.Entry(root, font=("Arial", 12))
    entry_calificacion.insert(0, datos[6])  # Insertar la calificación
    entry_calificacion.pack(pady=5)
    if datos[5].lower() != "terminada":
        entry_calificacion.config(state="disabled")  # Deshabilitar si no está terminada

    # Botón para guardar
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: actualizar_registro(
            root, id_registro, combo_usuario, combo_pelicula, combo_estado, entry_calificacion, 
            matriz_registro_vistas, tree, matriz_usuarios, matriz_peliculas
        )
    )
    btn_guardar.pack(pady=20)

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.pack(pady=10)

    root.mainloop()

def actualizar_registro(root, id_registro, combo_usuario, combo_pelicula, combo_estado, entry_calificacion, matriz_registro_vistas, tree, matriz_usuarios, matriz_peliculas):
    try:
        # Obtener los valores seleccionados
        usuario_seleccionado = combo_usuario.get()
        pelicula_seleccionada = combo_pelicula.get()
        estado = combo_estado.get()
        calificacion = entry_calificacion.get() if estado.lower() == "terminada" else "0"

        # Validar selección de usuario y película
        if not usuario_seleccionado or not pelicula_seleccionada or not estado:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Obtener IDs correspondientes
        usuario = next(usuario for usuario in matriz_usuarios if f"{usuario[1]} {usuario[2]}" == usuario_seleccionado)
        pelicula_id = next(pelicula[0] for pelicula in matriz_peliculas if pelicula[1] == pelicula_seleccionada)

        # Validar calificación si el estado es "terminada"
        if estado.lower() == "terminada" and not calificacion.isdigit():
            messagebox.showerror("Error", "Calificación no válida. Debe ser un número.")
            return

        # Buscar y actualizar el registro
        for registro in matriz_registro_vistas:
            if registro[0] == id_registro:
                registro[1] = usuario[0]
                registro[2] = usuario[2]
                registro[3] = pelicula_id
                registro[4] = pelicula_seleccionada
                registro[5] = estado
                registro[6] = calificacion
                break

        # Guardar los cambios en el archivo
        modulo_matriz.guardar_matriz_en_archivo("registros.txt", matriz_registro_vistas)
        refrescar_grilla(tree, matriz_registro_vistas)
        messagebox.showinfo("Éxito", "Registro actualizado correctamente.")
        root.destroy()

    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

def refrescar_grilla(tree, matriz_registro_vistas):
    for item in tree.get_children():
        tree.delete(item)
  
    matriz_registros_ordenados = sorted(matriz_registro_vistas, key=lambda x:str(x[2]))

    for registro in matriz_registros_ordenados:
        tree.insert("", tk.END, values=registro)

#-----------------
# Generar reporte
#-----------------
def imprimir_matriz_registro_vistas_tk(modo="normal"):
    matriz_registro_vistas=modulo_matriz.archivo_a_matriz("registros.txt")

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
    matriz_registros_ordenados = sorted(matriz_registro_vistas, key=lambda x: str(x[2]))

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
                form_actualizar_registro(id_registro, seleccion, tree)
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
