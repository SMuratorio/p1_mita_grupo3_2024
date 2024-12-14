import modulo_validar, modulo_menu, modulo_input, modulo_varios, modulo_matriz
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox

matriz_usuarios=modulo_matriz.archivo_a_matriz("usuarios.txt")
dnis_existentes = {usuario[3] for usuario in matriz_usuarios} #comprension de conjuntos
correos_existentes={usuario[4] for usuario in matriz_usuarios}

def crear_matriz_usuarios():
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == "s":
        print("\nAgregar usuario:")
        nombre, apellido, dni, correo = modulo_input.obtener_usuario_tk(dnis_existentes, correos_existentes)
        proximo_id_usuario = len(matriz_usuarios)+1

        print(f"El usuario {nombre} {apellido} con el DNI '{dni}' creado con ID {proximo_id_usuario}.")

        sublista = [proximo_id_usuario, nombre, apellido, dni, correo] #Empaquetado
        matriz_usuarios.append(sublista)
        print("\nUsuario agregado con éxito.")

        modulo_matriz.guardar_matriz_en_archivo("usuarios.txt", matriz_usuarios)
        leer_matriz_usuarios([sublista])

        from tkinter import messagebox
        messagebox.showinfo("Éxito", f"Usuario {nombre} {apellido} agregado con éxito.")

        opcion_seleccionada = modulo_validar.obtener_opcion(primera_consulta=False)
        
def leer_matriz_usuarios(usuarios):
    print("\nContenido registrado:")
    for fila in usuarios:
        proximo_id_usuario, nombre, apellido, dni, correo = fila #Desempaquetado
        print(f"ID: {proximo_id_usuario}")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"DNI: {dni}")
        print(f"Correo: {correo}")
        print("-" * 30)

def actualizar_matriz_usuarios():
    # opcion_seleccionada = modulo_validar.obtener_opcion()
    # while opcion_seleccionada == 's':

    id_usuario = int(modulo_input.obtener_id(matriz_usuarios, "usuario"))

    dic_usuario_actualizar = obtener_usuario(id_usuario, matriz_usuarios)
    opcion_actualizar = modulo_menu.mostrar_submenu_actualizar(list(dic_usuario_actualizar.keys())) #convierte las claves en lista
    # Llamada a la nueva función para validar y actualizar el valor
    dic_usuario_actualizar = validar_y_actualizar_usuarios(opcion_actualizar, dic_usuario_actualizar, dnis_existentes, correos_existentes, id_usuario)
    actualizar_usuario(id_usuario, matriz_usuarios, dic_usuario_actualizar)

    modulo_matriz.guardar_matriz_en_archivo("usuarios.txt", matriz_usuarios)
    opcion_seleccionada = modulo_validar.obtener_opcion(False)

def obtener_usuario(id_usuario, matriz_usuarios):
    for fila in matriz_usuarios:
        if fila[0] == id_usuario:
            return {"Nombre":fila[1], "Apellido": fila[2], "D.N.I": fila[3], "Correo": fila[4]} #Diccionario

def validar_y_actualizar_usuarios(opcion_actualizar, dic_usuario_actualizar, dnis_existentes, correos_existentes, id_usuario):
    validadores = {"Nombre": modulo_validar.validar_strings, #cada dato con su funcion de validar y verifica q dni y correo no exista en el conjunto
                   "Apellido": modulo_validar.validar_strings,
                   "D.N.I": lambda dni: modulo_validar.validar_dni(dni) and dni not in dnis_existentes,
                   "Correo": lambda email: modulo_validar.validar_email(email) and email not in correos_existentes,}
 
    dni_actual = dic_usuario_actualizar.get("D.N.I")
    correo_actual = dic_usuario_actualizar.get("Correo") #obtiene el valor asociado a esa clave

    nuevo_valor = modulo_input.obtener_nuevo_valor(opcion_actualizar, dic_usuario_actualizar, validadores)

    if opcion_actualizar in ["Nombre", "Apellido"]:
        nuevo_valor = nuevo_valor.capitalize()
    if opcion_actualizar == "D.N.I":
        dnis_existentes.discard(dni_actual);dnis_existentes.add(nuevo_valor)
    elif opcion_actualizar == "Correo":
        correos_existentes.discard(correo_actual);correos_existentes.add(nuevo_valor)

    dic_usuario_actualizar[opcion_actualizar] = nuevo_valor #diccionario que almacena la información de un usuario.
    print(f"{nuevo_valor} con ID {id_usuario} ha sido actualizado.") #Movi el print aca
    return dic_usuario_actualizar

def actualizar_usuario(id_usuario, matriz_usuarios, dic_usuario_actualizar):
    for fila in matriz_usuarios:
        if fila[0] == id_usuario:
            fila[1] = dic_usuario_actualizar["Nombre"]
            fila[2] = dic_usuario_actualizar["Apellido"]
            fila[3] = dic_usuario_actualizar["D.N.I"]
            fila[4] = dic_usuario_actualizar["Correo"]
            return

def eliminar_matriz_usuarios():
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == 's':
        print("\nEliminar contenido:")
        id_usuario = int(modulo_input.obtener_id(matriz_usuarios, "usuario"))
        # Eliminar el usuario
        matriz_usuarios[:] = [fila for fila in matriz_usuarios if fila[0] != id_usuario] 
        #[:] evita la creación de una nueva lista y modifica la lista existente.
        print(f"El usuario con ID {id_usuario} ha sido eliminado.")

        modulo_matriz.guardar_matriz_en_archivo("usuarios.txt", matriz_usuarios)
        
        opcion_seleccionada = modulo_validar.obtener_opcion(primera_consulta=False)

# Función para mostrar la matriz de usuarios en un Treeview
def imprimir_matriz_usuarios_tk(matriz_usuarios):
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

    for usuario in matriz_usuarios:
        tree.insert("", tk.END, values=usuario)

    tree.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def obtener_seleccion(tree):
        item_seleccionado = tree.selection()
        if not item_seleccionado:
            return None
        valores = tree.item(item_seleccionado, "values")
        return valores

    def mostrar_seleccion():
        seleccion = obtener_seleccion(tree)
        if seleccion:
            id_usuario = int(seleccion[0])  # Obtener el ID como entero
            menu_actualizar_usuario(id_usuario, seleccion, matriz_usuarios)
        else:
            messagebox.showwarning("Sin selección", "Por favor, seleccione un usuario.")

    def eliminar_seleccion():
        seleccion = obtener_seleccion(tree)
        if seleccion:
            id_usuario = int(seleccion[0])
            for usuario in matriz_usuarios:
                if usuario[0] == id_usuario:
                    matriz_usuarios.remove(usuario)
                    break
            tree.delete(tree.selection()[0])
            modulo_matriz.guardar_matriz_en_archivo("usuarios.txt", matriz_usuarios)
            messagebox.showinfo("Éxito", "Usuario eliminado.")
        else:
            messagebox.showwarning("Sin selección", "Por favor, seleccione un usuario para eliminar.")

    btn_seleccion = tk.Button(root, text="Actualizar", command=mostrar_seleccion)
    btn_seleccion.pack(pady=10)

    btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_seleccion)
    btn_eliminar.pack(pady=10)

    boton_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
    boton_cerrar.pack(pady=20)

    root.mainloop()

# --------------------------------
# menu eliminar
# --------------------------------

def eliminar_seleccion():
    print("usuario eliminado")

# --------------------------------
# menu actualizar
# --------------------------------

# Función para mostrar el formulario de actualización con los datos seleccionados
def menu_actualizar_usuario(id_usuario, datos, matriz_usuarios):
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
    tk.Label(root, text="Mail:", font=("Arial", 12)).pack(pady=5)
    entry_mail = tk.Entry(root, font=("Arial", 12))
    entry_mail.insert(0, datos[4])  # Insertar el correo del usuario seleccionado
    entry_mail.pack(pady=5)

    # Botón para guardar
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: guardar_datos(root, id_usuario, entry_nombre, entry_apellido, entry_dni, entry_mail, matriz_usuarios)
    )
    btn_guardar.pack(pady=20)

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.pack(pady=10)

    root.mainloop()

# Función para guardar los datos actualizados
def guardar_datos(root, id_usuario, entry_nombre, entry_apellido, entry_dni, entry_mail, matriz_usuarios):
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()
    mail = entry_mail.get()

    if not (nombre and apellido and dni and mail):
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
        return

    # Actualizar los datos en la matriz
    for usuario in matriz_usuarios:
        if usuario[0] == id_usuario:
            usuario[1] = nombre
            usuario[2] = apellido
            usuario[3] = dni
            usuario[4] = mail
            break

    # Guardar la matriz actualizada en el archivo
    modulo_matriz.guardar_matriz_en_archivo("usuarios.txt", matriz_usuarios)

    messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
    root.destroy()