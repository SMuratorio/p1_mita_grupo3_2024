import modulo_validar, modulo_matriz
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

matriz_usuarios=modulo_matriz.archivo_a_matriz("usuarios.txt")
dnis_existentes = {usuario[3] for usuario in matriz_usuarios} #comprension de conjuntos
correos_existentes={usuario[4] for usuario in matriz_usuarios}

#-----------------
# Agregar usuario
#----------------
def form_agregar_usuario(matriz_usuarios):
    root = tk.Tk()
    root.title("Agregar Usuario")
    root.geometry("400x400")

    # Etiqueta para el título
    titulo = tk.Label(root, text=f"Agregar Usuario", font=("Arial", 16))
    titulo.pack(pady=10)

    # Campo para Nombre
    tk.Label(root, text="Nombre:", font=("Arial", 12)).pack(pady=5)
    entry_nombre = tk.Entry(root, font=("Arial", 12))
    entry_nombre.pack(pady=5)

    # Campo para Apellido
    tk.Label(root, text="Apellido:", font=("Arial", 12)).pack(pady=5)
    entry_apellido = tk.Entry(root, font=("Arial", 12))
    entry_apellido.pack(pady=5)

    # Campo para DNI
    tk.Label(root, text="DNI:", font=("Arial", 12)).pack(pady=5)
    entry_dni = tk.Entry(root, font=("Arial", 12))
    entry_dni.pack(pady=5)

    # Campo para Mail
    tk.Label(root, text="Correo:", font=("Arial", 12)).pack(pady=5)
    entry_mail = tk.Entry(root, font=("Arial", 12))
    entry_mail.pack(pady=5)

    # Botón para guardar
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: agregar_datos(root, entry_nombre, entry_apellido, entry_dni, entry_mail, matriz_usuarios)
    )
    btn_guardar.pack(pady=20)

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.pack(pady=10)

    root.mainloop()

def agregar_datos(root, entry_nombre, entry_apellido, entry_dni, entry_mail, matriz_usuarios):
    try:
        nombre = entry_nombre.get().capitalize()
        apellido = entry_apellido.get().capitalize()
        dni = entry_dni.get()
        mail = entry_mail.get()
        proximo_id_usuario = len(matriz_usuarios) + 1
        
        #Verificar espacios en blanco
        if not nombre or not apellido or not dni or not mail:
            messagebox.showerror("Error", "Todos los campos son obligatorios. No se puede dejar ninguno en blanco.")
            return
        
        # Validaciones
        if not modulo_validar.validar_strings(nombre):
            messagebox.showerror("Error", "Nombre no válido. Intente nuevamente.")
            return 
        if not modulo_validar.validar_strings(apellido):
            messagebox.showerror("Error", "Apellido no válido. Intente nuevamente.")
            return
        if not modulo_validar.validar_dni(dni):
            messagebox.showerror("Error", "DNI no válido. Asegúrese de que esté en formato XX.XXX.XXX.")
            return
        if not modulo_validar.validar_email(mail):
            messagebox.showerror("Error", "Correo no válido. Intente nuevamente.")
            return

        # Validar unicidad del DNI y correo
        if dni in dnis_existentes:
            messagebox.showerror("Error", "El DNI ingresado ya existe.")
            return
        if mail in correos_existentes:
            messagebox.showerror("Error", "El correo ingresado ya existe.")
            return

        sublista = [proximo_id_usuario, nombre, apellido, dni, mail]
        matriz_usuarios.append(sublista)

        modulo_matriz.guardar_matriz_en_archivo("usuarios.txt", matriz_usuarios)
        messagebox.showinfo("Éxito", f"Usuario {nombre} {apellido} agregado con éxito.")
        root.destroy()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos en todos los campos.")
    except Exception as e:
        messagebox.showerror(f"Ha ocurrido un error inesperado: {e}")

#-------------------
# Actualizar usuario
#-------------------
def form_actualizar_usuario(id_usuario, datos, matriz_usuarios, tree):
    root = tk.Tk()
    root.title("Actualizar Usuario")
    root.geometry("400x400")

    # Etiqueta para el título
    titulo = tk.Label(root, text=f"Actualizar Usuario - ID: {id_usuario}", font=("Arial", 16))
    titulo.pack(pady=10)

    # Campo para Nombre
    tk.Label(root, text="Nombre:", font=("Arial", 12)).pack(pady=5)
    entry_nombre = tk.Entry(root, font=("Arial", 12))
    entry_nombre.insert(0, datos[1])  # Insertar el nombre del usuario seleccionado
    entry_nombre.pack(pady=5)

    # Campo para Apellido
    tk.Label(root, text="Apellido:", font=("Arial", 12)).pack(pady=5)
    entry_apellido = tk.Entry(root, font=("Arial", 12))
    entry_apellido.insert(0, datos[2])  # Insertar el apellido del usuario seleccionado
    entry_apellido.pack(pady=5)

    # Campo para DNI
    tk.Label(root, text="DNI:", font=("Arial", 12)).pack(pady=5)
    entry_dni = tk.Entry(root, font=("Arial", 12))
    entry_dni.insert(0, datos[3])  # Insertar el DNI del usuario seleccionado
    entry_dni.pack(pady=5)

    # Campo para Mail
    tk.Label(root, text="Correo:", font=("Arial", 12)).pack(pady=5)
    entry_mail = tk.Entry(root, font=("Arial", 12))
    entry_mail.insert(0, datos[4])  # Insertar el correo del usuario seleccionado
    entry_mail.pack(pady=5)

    # Botón para guardar
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: actualizar_datos(root, id_usuario, entry_nombre, entry_apellido, entry_dni, entry_mail, matriz_usuarios, tree)
    )
    btn_guardar.pack(pady=20)

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.pack(pady=10)

    root.mainloop()

def actualizar_datos(root, id_usuario, entry_nombre, entry_apellido, entry_dni, entry_mail, matriz_usuarios, tree):
    nombre = entry_nombre.get().capitalize()
    apellido = entry_apellido.get().capitalize()
    dni = entry_dni.get()
    mail = entry_mail.get()

    if not (nombre and apellido and dni and mail):
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
        return
    
    if not modulo_validar.validar_strings(nombre):
        messagebox.showerror("Error", "Nombre no válido. Intente nuevamente.")
        return
    if not modulo_validar.validar_strings(apellido):
        messagebox.showerror("Error", "Apellido no válido. Intente nuevamente.")
        return

    datos_actuales = next((usuario for usuario in matriz_usuarios if usuario[0] == id_usuario), None)
    if not datos_actuales:
        messagebox.showerror("Error", "Usuario no encontrado en la matriz.")
        return

    # Validar DNI solo si se modificó
    if dni and dni != datos_actuales[3]:
        if not modulo_validar.validar_dni(dni):
            messagebox.showerror("Error", "DNI no válido. Asegúrese de que esté en formato XX.XXX.XXX.")
            return
        if dni in dnis_existentes:
            messagebox.showerror("Error", "El DNI ingresado ya existe.")
            return

    # Validar correo solo si se modificó
    if mail and mail != datos_actuales[4]:
        if not modulo_validar.validar_email(mail):
            messagebox.showerror("Error", "Correo no válido. Intente nuevamente.")
            return
        if mail in correos_existentes:
            messagebox.showerror("Error", "El correo ingresado ya existe.")
            return
        
    for usuario in matriz_usuarios:
        if usuario[0] == id_usuario:
            usuario[1] = nombre
            usuario[2] = apellido
            usuario[3] = dni
            usuario[4] = mail
            break

    modulo_matriz.guardar_matriz_en_archivo("usuarios.txt", matriz_usuarios)
    
    refrescar_grilla(tree, matriz_usuarios)
    
    messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
    root.destroy()

def refrescar_grilla(tree, matriz_usuarios):
    for item in tree.get_children():
        tree.delete(item)
    
    matriz_usuarios_ordenados = sorted(matriz_usuarios, key=lambda fila: fila[2])
    # Insertar los datos en el Treeview
    for usuario in matriz_usuarios_ordenados:
        # Recortar el nombre a 8 caracteres
        usuario[1] = usuario[1][:8]
        tree.insert("", tk.END, values=(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
    
#-----------------
# Generar reporte
#----------------
def imprimir_matriz_usuarios_tk(matriz_usuarios, modo="normal"):
    root = tk.Tk()
    root.title("Matriz de Usuarios")

    tree = ttk.Treeview(root, columns=("ID", "Nombre", "Apellido", "DNI", "Correo"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("DNI", text="DNI")
    tree.heading("Correo", text="Correo")
    tree.column("ID", width=50, anchor=tk.CENTER)
    tree.column("Nombre", width=150, anchor="w")
    tree.column("Apellido", width=150, anchor="w")
    tree.column("DNI", width=100, anchor=tk.CENTER)
    tree.column("Correo", width=200, anchor="w")

    # Ordenar la matriz por apellido
    matriz_usuarios_ordenados = sorted(matriz_usuarios, key=lambda fila: fila[2])

    # Insertar los datos en el Treeview
    for usuario in matriz_usuarios_ordenados:
        # Recortar el nombre a 8 caracteres
        usuario[1] = usuario[1][:8]
        tree.insert("", tk.END, values=(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
    
    tree.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    # Solo mostrar los botones si el modo es "normal"
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
                id_usuario = int(seleccion[0])  # Obtener el ID como entero
                form_actualizar_usuario(id_usuario, seleccion, matriz_usuarios_ordenados, tree)
            else:
                messagebox.showwarning("Sin selección", "Por favor, seleccione un usuario.")

        def eliminar_seleccion():#(funcion que elimina usuario)
            seleccion = obtener_seleccion(tree)
            if seleccion:
                # Filtrar los registros que no coinciden con el ID seleccionado
                matriz_usuarios[:] = [registro for registro in matriz_usuarios if registro[0] != seleccion[0]]
                
                # Eliminar el registro de la vista (Treeview)
                tree.delete(tree.selection()[0])
                
                messagebox.showinfo("Éxito", "Registro eliminado.")
            else:
                messagebox.showwarning("Sin selección", "Por favor, seleccione un registro para eliminar.")

        btn_seleccion = tk.Button(root, text="Actualizar", command=actualizar_seleccion)
        btn_seleccion.pack(pady=10)

        btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_seleccion)
        btn_eliminar.pack(pady=10)

    boton_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
    boton_cerrar.pack(pady=20)

    root.mainloop()
