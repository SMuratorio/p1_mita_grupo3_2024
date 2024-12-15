import modulo_validar, modulo_menu, modulo_varios, modulo_input, modulo_genero, modulo_sinopsis, modulo_matriz
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

matriz_peliculas=modulo_matriz.archivo_a_matriz("peliculas.txt")
titulos_existentes={titulo[1] for titulo in matriz_peliculas}

def crear_matriz_peliculas():
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == "s":
        proximo_id_peliculas = len(matriz_peliculas)+1
        print("\nAgregar pelicula o serie:")
        titulo, tipo, genero, anio, duracion = modulo_input.obtener_pelicula(titulos_existentes)

        sinopsis_formateada=modulo_sinopsis.formatear_sinopsis(titulo)  # Obtener sinopsis formateada
        modulo_sinopsis.guardar_sinopsis_en_archivo(sinopsis_formateada)

        print(f"La {tipo} '{titulo}' creada con ID {proximo_id_peliculas}.")

        sublista = [proximo_id_peliculas, titulo, tipo, genero, anio, duracion]
        matriz_peliculas.append(sublista)
        print("\nPelícula/Serie agregada con éxito.")

        modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
        leer_matriz_peliculas([sublista])

        opcion_seleccionada=modulo_validar.obtener_opcion(primera_consulta=False)

def leer_matriz_peliculas(peliculas):
    print("\nContenido registrado:")
    for fila in peliculas:
        proximo_id, titulo, tipo, genero, año, duracion = fila
        print(f"ID: {proximo_id}")
        print(f"Título: {titulo}")
        print(f"Tipo: {tipo}")
        print(f"Género: {genero}")
        print(f"Año: {año}")
        print(f"Duración: {duracion}")
        print("-" * 30)

def actualizar_matriz_peliculas():
    opcion_seleccionada = modulo_validar.obtener_opcion()
    while opcion_seleccionada == 's':
        id_pelicula = int(modulo_input.obtener_id(matriz_peliculas, "pelicula/serie"))
        dic_pelicula_actualizar = obtener_pelicula(id_pelicula, matriz_peliculas)
        opcion_actualizar = modulo_menu.mostrar_submenu_actualizar(list(dic_pelicula_actualizar.keys())) #convierte las claves en lista
        # Llamada a la nueva función para validar y actualizar el valor
        dic_pelicula_actualizar = validar_y_actualizar_pelicula(opcion_actualizar, dic_pelicula_actualizar, id_pelicula, titulos_existentes)
        actualizar_pelicula(id_pelicula, matriz_peliculas, dic_pelicula_actualizar)
        modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
        
        opcion_seleccionada = modulo_validar.obtener_opcion(False)

def obtener_pelicula(id_pelicula, matriz_peliculas):
    for fila in matriz_peliculas:
        if fila[0] == id_pelicula:
            return {"Titulo":fila[1], "Tipo": fila[2], "Genero": fila[3], "Año": fila[4]}

def actualizar_pelicula(id_pelicula, matriz_peliculas, pelicula_actualizar):
    for fila in matriz_peliculas:
        if fila[0] == id_pelicula:
            fila[1] = pelicula_actualizar["Titulo"]
            fila[2] = pelicula_actualizar["Tipo"]
            fila[3] = pelicula_actualizar["Genero"]
            fila[4] = pelicula_actualizar["Año"]
            return

def validar_y_actualizar_pelicula(opcion_actualizar, dic_pelicula_actualizar, id_pelicula, titulos_existentes):
    validadores = {"Titulo": lambda titulo: modulo_validar.validar_titulo(titulo) and modulo_varios.capitalizar_titulo(titulo) not in titulos_existentes, 
                   "Tipo": modulo_validar.validar_tipo,
                   "Genero": lambda genero: True,
                   "Año": modulo_validar.validar_anio}

    titulo_actual = dic_pelicula_actualizar.get("Titulo")  
    valor_actual = dic_pelicula_actualizar.get(opcion_actualizar) #obtiene valor asociado a esa clave 
    
    if opcion_actualizar == "Genero":
        print(f"Va a actualizar el campo 'Genero' cuyo valor actual es: '{valor_actual}'.")
        nuevo_valor= modulo_genero.seleccionar_genero()
        
    else:
        nuevo_valor = modulo_input.obtener_nuevo_valor(opcion_actualizar, dic_pelicula_actualizar, validadores).capitalize()

    if opcion_actualizar == "Tipo":  # Se verifica si se está actualizando el tipo
        if nuevo_valor in ["película", "pelicula"]:
            duracion = modulo_input.obtener_dinamico("Ingrese la duración de la película (en minutos): ","Duración no válida. Por favor, ingrese un número entero positivo.",
                                                      modulo_validar.validar_duracion)
            dic_pelicula_actualizar["Duracion"] = f"{duracion} minutos"  # Actualizar duración para película
        elif nuevo_valor == "serie":
            duracion = modulo_input.obtener_dinamico("Ingrese la cantidad de temporadas: ","Cantidad no válida. Por favor, ingrese un número entero positivo.",
                                                      modulo_validar.validar_duracion)
            dic_pelicula_actualizar["Duracion"] = f"{duracion} temporadas"  # Actualizar duración para serie
    
    if opcion_actualizar == "Titulo":
        titulos_existentes.discard(titulo_actual);titulos_existentes.add(nuevo_valor)
    
    dic_pelicula_actualizar[opcion_actualizar] = nuevo_valor #diccionario que almacena la información de un usuario.
    print(f"{nuevo_valor} con ID {id_pelicula} ha sido actualizado.") #Movi el print aca
    return dic_pelicula_actualizar

def eliminar_matriz_peliculas():
    eliminar_pelicula = modulo_validar.obtener_opcion()
    while eliminar_pelicula == 's':
        print("\nEliminar contenido:")
        id_pelicula = int(modulo_input.obtener_id(matriz_peliculas, "pelicula/serie"))
        titulo = obtener_pelicula(id_pelicula, matriz_peliculas)["Titulo"]
        # Eliminar el pelicula
        matriz_peliculas[:] = [item for item in matriz_peliculas if item[0] != id_pelicula] #[:] evita la creación de una nueva lista y modifica la lista existente.
        modulo_sinopsis.eliminar_del_archivo("sinopsis.txt", titulo) # Eliminar la sinopsis asociada a la película
        
        print(f"La pelicula/serie con ID {id_pelicula} ha sido eliminado.")
        modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
        
        eliminar_pelicula = modulo_validar.obtener_opcion(primera_consulta=False)
    
def imprimir_matriz_peliculas(contenido_peliculas):
    for i in range(len(contenido_peliculas)):
        contenido_peliculas[i][1] = contenido_peliculas[i][1][:8]  #Recortar el título a 8 caracteres

    for pelicula in contenido_peliculas:  # Convertir el año a entero si está en formato de cadena
        pelicula[4] = int(pelicula[4])  # Convertir el año de estreno a entero
                            
    matriz_peliculas_ordenadas = sorted(contenido_peliculas, key=lambda x: x[4]) # Ordenar la lista por año de estreno (ascendente)
    encabezado_pelilculas = ["ID", "Título", "Tipo", "Género", "Año", "Duración"]  # Atributos de cada contenido

    ancho_columna=25  
    modulo_varios.imprimir_linea(len(encabezado_pelilculas), ancho_columna)# Imprimir la línea superior del cuadro
    
    print("|" + "|".join([f"{encabezado:<{ancho_columna}}" for encabezado in encabezado_pelilculas]) + "|")  # Imprimir el encabezado
    
    modulo_varios.imprimir_linea(len(encabezado_pelilculas), ancho_columna)    # Imprimir la línea interior del cuadro
    
    for fila in matriz_peliculas_ordenadas:    # Imprimir cada fila de la matriz
        print("|" + "|".join([f"{str(valor).capitalize():<{ancho_columna}}" for valor in fila]) + "|")
    
    modulo_varios.imprimir_linea(len(encabezado_pelilculas), ancho_columna) # Imprimir la línea inferior del cuadro

def imprimir_matriz_peliculas_tk(matriz_peliculas):
    root = tk.Tk()
    root.title("Matriz de Películas")

    tree = ttk.Treeview(root, columns=("ID", "Título", "Tipo", "Género", "Año", "Duración"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Título", text="Título")  # Corregido: "Título" en lugar de "Titulo"
    tree.heading("Tipo", text="Tipo")
    tree.heading("Género", text="Género")
    tree.heading("Año", text="Año")
    tree.heading("Duración", text="Duración")
    tree.column("ID", width=50, anchor=tk.CENTER)
    tree.column("Título", width=150, anchor="w")  # Corregido: "Título"
    tree.column("Tipo", width=150, anchor="w")
    tree.column("Género", width=100, anchor=tk.CENTER)
    tree.column("Año", width=100, anchor="w")
    tree.column("Duración", width=100, anchor="w")

    for pelicula in matriz_peliculas:
        tree.insert("", tk.END, values=pelicula)

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
            id_pelicula = int(seleccion[0])  # Obtener el ID como entero
            form_actualizar_pelicula(id_pelicula, seleccion, matriz_peliculas, tree)
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
            messagebox.showinfo("Éxito", "Película eliminada.")
        else:
            messagebox.showwarning("Sin selección", "Por favor, seleccione una película para eliminar.")

    btn_seleccion = tk.Button(root, text="Actualizar", command=mostrar_seleccion)
    btn_seleccion.pack(pady=10)

    btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_seleccion)
    btn_eliminar.pack(pady=10)

    boton_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
    boton_cerrar.pack(pady=20)

    root.mainloop()

def form_actualizar_pelicula(id_pelicula, seleccion, matriz_peliculas, tree):
    root = tk.Tk()
    root.title("Actualizar Película")
    root.geometry("400x400")

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
    entry_tipo = tk.Entry(root, font=("Arial", 12))
    entry_tipo.insert(0, seleccion[2])
    entry_tipo.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Género:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_genero = tk.Entry(root, font=("Arial", 12))
    entry_genero.insert(0, seleccion[3])
    entry_genero.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Año:", font=("Arial", 12)).grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_anio = tk.Entry(root, font=("Arial", 12))
    entry_anio.insert(0, seleccion[4])
    entry_anio.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Duración:", font=("Arial", 12)).grid(row=5, column=0, sticky="e", padx=5, pady=5)
    entry_duracion = tk.Entry(root, font=("Arial", 12))
    entry_duracion.insert(0, seleccion[5])
    entry_duracion.grid(row=5, column=1, padx=10, pady=5)

    # Botón para guardar cambios
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: actualizar_datos_pelicula(
            root,
            id_pelicula,
            entry_titulo,
            entry_tipo,
            entry_genero,
            entry_anio,
            entry_duracion,
            matriz_peliculas,
            tree
        )
    )
    btn_guardar.grid(row=6, column=0, padx=5, pady=20, sticky="e")

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.grid(row=6, column=1, padx=5, pady=20, sticky="w")

    root.mainloop()

def form_agregar_pelicula(matriz_peliculas):
    root = tk.Tk()
    root.title("Agregar Película")
    root.geometry("400x400")

    # Configurar las columnas y filas para centrar el contenido
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(7, weight=1)

    # Etiqueta para el título
    titulo = tk.Label(root, text="Agregar Película", font=("Arial", 16))
    titulo.grid(row=0, column=0, columnspan=2, pady=10)

    # Campos para agregar película
    tk.Label(root, text="Título:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_titulo = tk.Entry(root, font=("Arial", 12))
    entry_titulo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Tipo:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_tipo = tk.Entry(root, font=("Arial", 12))
    entry_tipo.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Género:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_genero = tk.Entry(root, font=("Arial", 12))
    entry_genero.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Año:", font=("Arial", 12)).grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_anio = tk.Entry(root, font=("Arial", 12))
    entry_anio.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Duración:", font=("Arial", 12)).grid(row=5, column=0, sticky="e", padx=5, pady=5)
    entry_duracion = tk.Entry(root, font=("Arial", 12))
    entry_duracion.grid(row=5, column=1, padx=10, pady=5)

    # Botón para guardar película
    btn_guardar = tk.Button(
        root,
        text="Guardar",
        font=("Arial", 12),
        command=lambda: agregar_datos_pelicula(
            root,
            entry_titulo,
            entry_tipo,
            entry_genero,
            entry_anio,
            entry_duracion,
            matriz_peliculas
        )
    )
    btn_guardar.grid(row=6, column=0, pady=20, padx=5, sticky="e")

    # Botón para cerrar
    btn_cerrar = tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.destroy)
    btn_cerrar.grid(row=6, column=1, pady=20, padx=5, sticky="w")

    root.mainloop()

def actualizar_datos_pelicula(root, id_pelicula, entry_titulo, entry_tipo, entry_genero, entry_anio, entry_duracion, matriz_peliculas, tree):
    titulo = entry_titulo.get()
    tipo = entry_tipo.get()
    genero = entry_genero.get()
    anio = entry_anio.get()
    duracion = entry_duracion.get()

    for pelicula in matriz_peliculas:
        if pelicula[0] == id_pelicula:
            pelicula[1] = titulo
            pelicula[2] = tipo
            pelicula[3] = genero
            pelicula[4] = anio
            pelicula[5] = duracion
            break

    modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
    refrescar_grilla(tree, matriz_peliculas)
    messagebox.showinfo("Éxito", f"Película '{titulo}' actualizada con éxito.")
    root.destroy()

def agregar_datos_pelicula(root, entry_titulo, entry_tipo, entry_genero, entry_anio, entry_duracion, matriz_peliculas):
    titulo = entry_titulo.get()
    tipo = entry_tipo.get()
    genero = entry_genero.get()
    anio = entry_anio.get()
    duracion = entry_duracion.get()
    proximo_id = len(matriz_peliculas) + 1

    nueva_pelicula = [proximo_id, titulo, tipo, genero, anio, duracion]
    matriz_peliculas.append(nueva_pelicula)

    modulo_matriz.guardar_matriz_en_archivo("peliculas.txt", matriz_peliculas)
    messagebox.showinfo("Éxito", f"Película '{titulo}' agregada con éxito.")
    root.destroy()

def refrescar_grilla(tree, matriz_peliculas):
    for item in tree.get_children():
        tree.delete(item)
    for pelicula in matriz_peliculas:
        tree.insert("", tk.END, values=pelicula)