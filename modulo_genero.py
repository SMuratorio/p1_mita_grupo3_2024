import json, modulo_validar, modulo_menu
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

archivo_json = 'definiciones_generos.json'

def cargar_json():
    """Carga el archivo JSON y maneja errores."""
    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo JSON no fue encontrado. Se utilizará un diccionario vacío.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Se utilizará un diccionario vacío.")
        return {}
    except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
   
def guardar_json(datos):
    try:
        with open(archivo_json, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar el archivo JSON: {e}")

def agregar_genero(nuevo_genero, definicion):
    datos = cargar_json()

    if nuevo_genero in datos.values():
        messagebox.showerror("Error", f"El género '{nuevo_genero}' ya existe.")
        return False

    if not definicion.strip():
        messagebox.showerror("Error", "La definición no puede estar vacía.")
        return False

    datos[nuevo_genero] = definicion
    guardar_json(datos)
    messagebox.showinfo("Éxito", f"Género '{nuevo_genero}' agregado")
    return True

def eliminar_genero(key_genero):
    datos = cargar_json()

    if key_genero not in datos:
        messagebox.showerror("Error", f"No se encontró un género con clave '{key_genero}'.")
        return False

    datos.pop(key_genero)
    guardar_json(datos)
    messagebox.showinfo("Éxito", f"Género con clave '{key_genero}' eliminado.")
    return True

def imprimir_generos_tk():
    root = tk.Tk()
    root.title("Matriz de Géneros")
    root.geometry("600x500")  # Dimensiones ajustadas

    # Configuración del Treeview
    tree = ttk.Treeview(root, columns=("ID", "Género", "Definición"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Género", text="Género")
    tree.heading("Definición", text="Definición")
    tree.column("ID", width=50, anchor=tk.CENTER)
    tree.column("Género", width=150, anchor="w")
    tree.column("Definición", width=300, anchor="w")
    tree.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    # Cargar datos desde el archivo JSON
    def cargar_treeview():
        """Cargar datos del archivo JSON en el Treeview."""
        for row in tree.get_children():
            tree.delete(row)
        generos = cargar_json()
        for index, (key, value) in enumerate(generos.items(), start=1):
            tree.insert("", tk.END, values=(index, key, value))

    cargar_treeview()

    # Contenedor para los campos de entrada
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    # Campo Género
    tk.Label(input_frame, text="Género:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_genero = tk.Entry(input_frame, font=("Arial", 12))
    entry_genero.grid(row=0, column=1, padx=5, pady=5)

    # Campo Definición (TextArea)
    tk.Label(input_frame, text="Definición:", font=("Arial", 12)).grid(row=1, column=0, sticky="ne", padx=5, pady=5)
    text_definicion = tk.Text(input_frame, font=("Arial", 12), height=5, width=30, wrap="word")
    text_definicion.grid(row=1, column=1, padx=5, pady=5)

    def obtener_seleccion():
        """Obtener la clave y el valor de la selección en el Treeview."""
        item_seleccionado = tree.selection()
        if not item_seleccionado:
            return None, None
        valores = tree.item(item_seleccionado, "values")
        key_genero = valores[1]  # La clave del género (columna "Género")
        definicion = valores[2]  # La definición actual
        return key_genero, definicion

    # Función para manejar la selección en el Treeview
    def manejar_seleccion(event):
        """Rellena los campos con los valores seleccionados en el Treeview."""
        key_genero, definicion = obtener_seleccion()
        if key_genero and definicion:
            entry_genero.delete(0, tk.END)
            entry_genero.insert(0, key_genero)
            text_definicion.delete("1.0", tk.END)
            text_definicion.insert("1.0", definicion)

    # Asociar el evento de selección en el Treeview
    tree.bind("<<TreeviewSelect>>", manejar_seleccion)

    # Función para agregar un género
    def agregar_genero_action():
        nuevo_genero = entry_genero.get().strip()
        definicion = text_definicion.get("1.0", tk.END).strip()

        if not modulo_validar.validar_strings(nuevo_genero):
            messagebox.showerror("Error", "Genero invalido intente nuevamente.")
            entry_genero.delete(0, tk.END)
            return

        if not nuevo_genero or not definicion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if agregar_genero(nuevo_genero, definicion):  # `None` porque no hay una clave para un nuevo género
            cargar_treeview()
            entry_genero.delete(0, tk.END)
            text_definicion.delete("1.0", tk.END)

    # Función para eliminar un género
    def eliminar_genero_action():
        key_genero, _ = obtener_seleccion()
        if not key_genero:
            messagebox.showerror("Error", "Debe seleccionar un género para eliminar.")
            return

        if eliminar_genero(key_genero):
            cargar_treeview()
            entry_genero.delete(0, tk.END)
            text_definicion.delete("1.0", tk.END)

    # Contenedor para los botones
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Botones para acciones CRUD
    tk.Button(button_frame, text="Enviar", font=("Arial", 12), command=agregar_genero_action).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Eliminar", font=("Arial", 12), command=eliminar_genero_action).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Cerrar", font=("Arial", 12), command=root.destroy).grid(row=0, column=2, padx=5)

    root.mainloop()
