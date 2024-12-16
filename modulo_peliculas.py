import modulo_genero, modulo_sinopsis, modulo_validar, modulo_matriz
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

matriz_peliculas=modulo_matriz.archivo_a_matriz("peliculas.txt")
titulos_existentes={titulo[1] for titulo in matriz_peliculas}

def capitalizar_titulo(titulo):
     # Capitaliza la primera letra del título y cada palabra que tenga 3 letras o más
    palabras = titulo.split()
    capitalizado = []

    for palabra in palabras:
        if len(palabra) >= 3:
            capitalizado.append(palabra.capitalize())
        else:
            capitalizado.append(palabra)
    
    if capitalizado:# Capitaliza la primera letra del título completo
        capitalizado[0] = capitalizado[0].capitalize()
    return ' '.join(capitalizado)

#-----------------
# Agrerar pelicula
#-----------------
def form_agregar_pelicula(matriz_peliculas):
    root = tk.Tk()
    root.title("Agregar Película")
    root.geometry("600x500")

    # Configurar columnas y filas para centrar el contenido
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(8, weight=1)

    # Etiqueta para el título
    titulo = tk.Label(root, text="Agregar Película", font=("Arial", 16))
    titulo.grid(row=0, column=0, columnspan=2, pady=10)

    # Campos para agregar película
    tk.Label(root, text="Título:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_titulo = tk.Entry(root, font=("Arial", 12))
    entry_titulo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Tipo:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
    tipo_combobox = ttk.Combobox(root, font=("Arial", 12), width=18, state="readonly", values=["Película", "Serie"])
    tipo_combobox.grid(row=2, column=1, padx=10, pady=5)
    tipo_combobox.current(0)  # Selecciona "Película" por defecto

    tk.Label(root, text="Género:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=5, pady=5)

    # Cargar géneros desde el archivo JSON
    generos = list(modulo_genero.cargar_json().keys())
    genero_combobox = ttk.Combobox(root, font=("Arial", 12), width=18, state="readonly", values=generos)
    genero_combobox.grid(row=3, column=1, padx=10, pady=5)
    if generos:  # Si hay géneros disponibles
        genero_combobox.current(0)

    tk.Label(root, text="Año:", font=("Arial", 12)).grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_anio = tk.Entry(root, font=("Arial", 12))
    entry_anio.grid(row=4, column=1, padx=10, pady=5)

    # Dinámico: Label para duración
    duracion_label = tk.Label(root, text="Duración minutos:", font=("Arial", 12))
    duracion_label.grid(row=5, column=0, sticky="e", padx=5, pady=5)

    entry_duracion = tk.Entry(root, font=("Arial", 12))
    entry_duracion.grid(row=5, column=1, padx=10, pady=5)

    # Callback para cambiar el texto del Label según el tipo seleccionado
    def actualizar_label_duracion(event):
        if tipo_combobox.get() == "Película":
            duracion_label.config(text="Duración minutos:")
        elif tipo_combobox.get() == "Serie":
            duracion_label.config(text="Duración temporadas:")

    # Vincular el evento de cambio al combobox
    tipo_combobox.bind("<<ComboboxSelected>>", actualizar_label_duracion)

    # TextArea para Sinopsis
    tk.Label(root, text="Sinopsis:", font=("Arial", 12)).grid(row=6, column=0, sticky="ne", padx=5, pady=5)
    text_sinopsis = tk.Text(root, font=("Arial", 12), height=5, width=20, wrap="word")
    text_sinopsis.grid(row=6, column=1, padx=10, pady=5)

    # Botón para guardar película
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: agregar_datos_pelicula(
            root,
            entry_titulo,
            tipo_combobox,
            genero_combobox,  # Se pasa el Combobox de género en lugar de un campo abierto
            entry_anio,
            entry_duracion,
            text_sinopsis,
            matriz_peliculas
        )
    )
    btn_guardar.grid(row=7, column=0, pady=20, padx=5, sticky="e")

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.grid(row=7, column=1, pady=20, padx=5, sticky="w")

    root.mainloop()

def agregar_datos_pelicula(root, entry_titulo, tipo_combobox, entry_genero, entry_anio, entry_duracion, text_sinopsis, matriz_peliculas):
    try:
        titulo = entry_titulo.get()
        tipo = tipo_combobox.get()  # Obtener el valor seleccionado del Combobox
        genero = entry_genero.get().capitalize()
        anio = entry_anio.get()
        duracion = entry_duracion.get()
        sinopsis = text_sinopsis.get("1.0", "end").strip()  # Obtener el texto del TextArea

        proximo_id_pelicula = len(matriz_peliculas) + 1

        # Verificar espacios en blanco
        if not titulo or not tipo or not genero or not anio or not duracion or not sinopsis:
            messagebox.showerror("Error", "Todos los campos son obligatorios. No se puede dejar ninguno en blanco.")
            return

        # Validaciones
        if not modulo_validar.validar_titulo(titulo):
            messagebox.showerror("Error", "Título no válido. Intente nuevamente.")
            return
        if not modulo_validar.validar_anio(anio):
            messagebox.showerror("Error", "Año no válido. Debe ser un número.")
            return
        if duracion:
            if not modulo_validar.validar_duracion(duracion):
                if tipo == "Serie":
                    messagebox.showerror("Error", "Temporadas debe ser un número.")
                else:
                    messagebox.showerror("Error", "Duración (minutos) debe ser un número.")
                return


        titulo = capitalizar_titulo(titulo)
        sublista = [proximo_id_pelicula, titulo, tipo, genero, anio, duracion]
        matriz_peliculas.append(sublista)

        # Guardar en archivo
        modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
        messagebox.showinfo("Éxito", f"Película/Serie '{titulo}' agregada con éxito.")
        # Guardar sinopsis
        modulo_sinopsis.guardar_sinopsis_en_archivo("sinopsis.txt", proximo_id_pelicula, titulo, sinopsis)
        root.destroy()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos en todos los campos.")
    except Exception as e:
        messagebox.showerror(f"Ha ocurrido un error inesperado: {e}")

def form_actualizar_pelicula(id_pelicula, seleccion, matriz_peliculas, tree):
    root = tk.Tk()
    root.title("Actualizar Película")
    root.geometry("600x500")

    # Configurar las columnas y filas para centrar el contenido
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(7, weight=1)

    # Etiqueta para el título
    titulo = tk.Label(root, text=f"Actualizar Película - ID: {id_pelicula}", font=("Arial", 16))
    titulo.grid(row=0, column=0, columnspan=2, pady=10)

    # Campos de actualización
    tk.Label(root, text="Título:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_titulo = tk.Entry(root, font=("Arial", 12))
    entry_titulo.insert(0, seleccion[1])
    entry_titulo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Tipo:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
    tipo_combobox = ttk.Combobox(root, font=("Arial", 12), width=18, state="readonly", values=["Película", "Serie"])
    tipo_combobox.grid(row=2, column=1, padx=10, pady=5)
    tipo_combobox.set(seleccion[2])  # Selecciona automáticamente el valor actual

    tk.Label(root, text="Género:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=5, pady=5)

    # Cargar opciones de género desde JSON
    generos = list(modulo_genero.cargar_json().keys())
    genero_combobox = ttk.Combobox(root, font=("Arial", 12), width=18, state="readonly", values=generos)
    genero_combobox.grid(row=3, column=1, padx=10, pady=5)
    if seleccion[3] in generos:
        genero_combobox.set(seleccion[3])  # Selecciona automáticamente el género actual

    tk.Label(root, text="Año:", font=("Arial", 12)).grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_anio = tk.Entry(root, font=("Arial", 12))
    entry_anio.insert(0, seleccion[4])
    entry_anio.grid(row=4, column=1, padx=10, pady=5)

    # Dinámico: Label para duración
    duracion_label = tk.Label(root, text="Duración minutos:", font=("Arial", 12))
    duracion_label.grid(row=5, column=0, sticky="e", padx=5, pady=5)

    unidad = str(seleccion[5]).split(" ")[0] if seleccion[5] else seleccion[5]
    entry_duracion = tk.Entry(root, font=("Arial", 12))
    entry_duracion.insert(0, unidad)
    entry_duracion.grid(row=5, column=1, padx=10, pady=5)

    # Callback para cambiar el texto del Label según el tipo seleccionado
    def actualizar_label_duracion(event):
        if tipo_combobox.get() == "Película":
            duracion_label.config(text="Duración minutos:")
        elif tipo_combobox.get() == "Serie":
            duracion_label.config(text="Duración temporadas:")

    # Vincular el evento de cambio al combobox
    tipo_combobox.bind("<<ComboboxSelected>>", actualizar_label_duracion)

    # TextArea para Sinopsis
    tk.Label(root, text="Sinopsis:", font=("Arial", 12)).grid(row=6, column=0, sticky="ne", padx=5, pady=5)
    text_sinopsis = tk.Text(root, font=("Arial", 12), height=5, width=20, wrap="word")
    _ , sinopsis = modulo_sinopsis.buscar_sinopsis("sinopsis.txt", id_pelicula)
    text_sinopsis.insert("1.0", sinopsis)
    text_sinopsis.grid(row=6, column=1, padx=10, pady=5)

    # Botón para guardar cambios
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: actualizar_datos_pelicula(
            root,
            id_pelicula,
            entry_titulo,
            tipo_combobox,  # Pasar el Combobox actualizado
            genero_combobox,  # Pasar el Combobox actualizado
            entry_anio,
            entry_duracion,
            text_sinopsis,
            matriz_peliculas,
            tree
        )
    )
    btn_guardar.grid(row=7, column=0, pady=20, padx=5, sticky="e")

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.grid(row=7, column=1, pady=20, padx=5, sticky="w")

    root.mainloop()

def actualizar_datos_pelicula(root, id_pelicula, entry_titulo, tipo_combobox, entry_genero, entry_anio, entry_duracion, text_sinopsis, matriz_peliculas, tree):
    try:
        titulo = entry_titulo.get()
        tipo = tipo_combobox.get()  # Obtener el valor del Combobox
        genero = entry_genero.get()
        anio = entry_anio.get()
        duracion = entry_duracion.get()
        sinopsis = text_sinopsis.get("1.0", "end").strip()

        # Validaciones
        if not titulo or not tipo or not genero or not anio or not duracion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        if not modulo_validar.validar_titulo(titulo):
            messagebox.showerror("Error", "Título no válido.")
            return
        if not modulo_validar.validar_anio(anio):
            messagebox.showerror("Error", "Año no válido.")
            return
        if duracion and not modulo_validar.validar_duracion(duracion):
            messagebox.showerror("Error", "Duración no válida.")
            return

        # Actualizar la matriz
        for pelicula in matriz_peliculas:
            if pelicula[0] == id_pelicula:
                pelicula[1] = capitalizar_titulo(titulo)
                pelicula[2] = tipo
                pelicula[3] = genero
                pelicula[4] = anio
                pelicula[5] = duracion
                break

        # Actualizar la sinopsis
        modulo_sinopsis.actualizar_sinopsis("sinopsis.txt", titulo, sinopsis, id_pelicula)

        # Guardar la matriz actualizada
        modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)

        refrescar_grilla(tree, matriz_peliculas)

        messagebox.showinfo("Éxito", f"La película/serie '{titulo}' se ha actualizado correctamente.")
        root.destroy()

    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

def refrescar_grilla(tree, matriz_peliculas):
    for item in tree.get_children():
        tree.delete(item)

    matriz_peliculas_ordenadas = sorted(matriz_peliculas, key=lambda x: int(x[4])) # Ordenar la lista por año de estreno (ascendente)
                            
    # Insertar los datos actualizados en la grilla
    for pelicula in matriz_peliculas_ordenadas:
        duracion = f"{pelicula[5]} Minutos" if pelicula[2] == "Película" else f"{pelicula[5]} Temporadas"
        # Insertar la fila con la duración transformada
        tree.insert("", tk.END, values=(pelicula[0], pelicula[1], pelicula[2], pelicula[3], pelicula[4], duracion))
#-----------------
# Generar reporte
#-----------------
def imprimir_matriz_peliculas_tk(matriz_peliculas, modo="normal"):
    root = tk.Tk()
    root.title("Matriz de Películas")

    tree = ttk.Treeview(root, columns=("ID", "Título", "Tipo", "Género", "Año", "Duración"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Título", text="Título")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Género", text="Género")
    tree.heading("Año", text="Año")
    tree.heading("Duración", text="Duración")
    tree.column("ID", width=50, anchor=tk.CENTER)
    tree.column("Título", width=150, anchor="w")
    tree.column("Tipo", width=150, anchor="w")
    tree.column("Género", width=100, anchor=tk.CENTER)
    tree.column("Año", width=100, anchor="w")
    tree.column("Duración", width=150, anchor="w")

    # Ordenar la matriz por año de estreno (ascendente)
    matriz_peliculas_ordenadas = sorted(matriz_peliculas, key=lambda x: int(x[4]))

    # Transformar la duración antes de insertar en el Treeview
    for pelicula in matriz_peliculas_ordenadas:
        duracion = f"{pelicula[5]} Minutos" if pelicula[2] == "Película" else f"{pelicula[5]} Temporadas"
        # Insertar la fila con la duración transformada
        tree.insert("", tk.END, values=(pelicula[0], pelicula[1], pelicula[2], pelicula[3], pelicula[4], duracion))

    tree.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

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
                id_pelicula = int(seleccion[0])  # Obtener el ID como entero
                form_actualizar_pelicula(id_pelicula, seleccion, matriz_peliculas_ordenadas, tree)
            else:
                messagebox.showwarning("Sin selección", "Por favor, seleccione una película.")
        
        def eliminar_seleccion():
            seleccion = obtener_seleccion(tree)
            if seleccion:
                id_pelicula = int(seleccion[0])
                for pelicula in matriz_peliculas:
                    if pelicula[0] == id_pelicula:
                        matriz_peliculas.remove(pelicula)
                        break
                tree.delete(tree.selection()[0])
                modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
                modulo_sinopsis.eliminar_del_archivo("sinopsis.txt", seleccion[0])
                root.destroy()
                messagebox.showinfo("Éxito", "Película eliminada.")
            else:
                messagebox.showwarning("Sin selección", "Por favor, seleccione una película para eliminar.")

        btn_seleccion = tk.Button(root, text="Actualizar", command=actualizar_seleccion)
        btn_seleccion.pack(pady=10)

        btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_seleccion)
        btn_eliminar.pack(pady=10)

    boton_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
    boton_cerrar.pack(pady=20)

    root.mainloop()
