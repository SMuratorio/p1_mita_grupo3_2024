import modulo_matriz

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

def imprimir_promedios(calcular_promedio, titulo):
    matriz_peliculas=modulo_matriz.archivo_a_matriz("peliculas.txt")
    matriz_registro_vistas=modulo_matriz.archivo_a_matriz("registros.txt")
    promedios = calcular_promedio(matriz_peliculas, matriz_registro_vistas)
    print(f"\n{titulo}:")
    for item, promedio in promedios.items():
        if promedio > 0:  # Solo imprimir elementos con calificaciones mayores a 0
            print(f"{item}: {promedio:.2f}")
