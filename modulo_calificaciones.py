import modulo_matriz
import tkinter as tk
from tkinter import ttk

def promedio_peliculas(matriz_peliculas, matriz_registro_vistas, indice=0, calificaciones=None):
    # Inicializa el diccionario de calificaciones en la primera llamada
    calificaciones = calificaciones or {}

    # Verificar si hemos llegado al final de la lista
    if indice == len(matriz_registro_vistas):
        # Cuando llegamos al final de la matriz, calculamos el promedio de cada película
        return {titulo: datos['suma'] / datos['contador'] for titulo, datos in calificaciones.items()}

    # Procesa la calificación actual si es mayor a 0
    registro = matriz_registro_vistas[indice]
    calificacion, titulo = int(registro[6]), registro[4]
    
    if calificacion > 0:
        if titulo in calificaciones:
            calificaciones[titulo]['suma'] += calificacion
            calificaciones[titulo]['contador'] += 1
        else:
            calificaciones[titulo] = {'suma': calificacion, 'contador': 1}

    # Llamada recursiva con el siguiente índice
    return promedio_peliculas(matriz_peliculas, matriz_registro_vistas, indice + 1, calificaciones)

def promedio_por_genero(matriz_peliculas, matriz_registro_vistas, indice=0, calificaciones_por_genero=None):
    # Inicializa el diccionario en la primera llamada con los géneros como claves y listas vacías como valores
    calificaciones_por_genero = calificaciones_por_genero or {fila[3]: [] for fila in matriz_peliculas}  # {"accion": [calificaciones]}

    # Verifica si hemos llegado al final de la matriz de registros
    if indice == len(matriz_registro_vistas):
        # Cuando se procesan todas las vistas, calculamos el promedio por género
        return {genero: (sum(cals) / len(cals) if cals else 0) for genero, cals in calificaciones_por_genero.items()}

    # Procesa la calificación actual si es mayor a 0
    vista = matriz_registro_vistas[indice]
    id_pelicula, calificacion = int(vista[3]) - 1, int(vista[6])  # convierte ID a índice en la matriz de películas
    if calificacion > 0:
        genero = matriz_peliculas[id_pelicula][3]  # Se asume que el género está en la columna 3
        calificaciones_por_genero[genero].append(calificacion)  # Agrega la calificación a la lista del género
    
    # Llamada recursiva con el siguiente índice
    return promedio_por_genero(matriz_peliculas, matriz_registro_vistas, indice + 1, calificaciones_por_genero)

def mostrar_promedios(calcular_promedio, titulo):
    # Cargar las matrices desde los archivos
    matriz_peliculas = modulo_matriz.archivo_a_matriz("peliculas.txt")
    matriz_registro_vistas = modulo_matriz.archivo_a_matriz("registros.txt")

    # Calcular los promedios utilizando la función proporcionada
    promedios = calcular_promedio(matriz_peliculas, matriz_registro_vistas)

    # Crear una ventana para mostrar los promedios
    ventana_promedios = tk.Toplevel()
    ventana_promedios.title(titulo)
    ventana_promedios.geometry("500x400")

    # Etiqueta de título
    tk.Label(ventana_promedios, text=titulo, font=("Arial", 16)).pack(pady=10)

    # Crear un Treeview para mostrar los datos
    tree = ttk.Treeview(ventana_promedios, columns=("Item", "Promedio"), show="headings")
    tree.heading("Item", text="Item")
    tree.heading("Promedio", text="Promedio")
    tree.column("Item", width=250)
    tree.column("Promedio", width=100, anchor="center")
    tree.pack(pady=20, fill="both", expand=True)

    # Insertar los datos en el Treeview
    for item, promedio in promedios.items():
        if promedio > 0:  # Solo mostrar elementos con calificaciones mayores a 0
            tree.insert("", "end", values=(item, f"{promedio:.2f}"))

    # Botón para cerrar la ventana
    tk.Button(ventana_promedios, text="Cerrar", command=ventana_promedios.destroy).pack(pady=10)