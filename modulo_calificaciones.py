def promedio_peliculas(matriz_peliculas, matriz_registro_vistas, indice=0, calificaciones=None):
    # Inicializa el diccionario en la primera llamada
    calificaciones = calificaciones or {}

    # Caso base: calcular y retornar promedios cuando se procesan todas las vistas
    if indice >= len(matriz_registro_vistas):
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
    # Inicializa el diccionario en la primera llamada
    calificaciones_por_genero = calificaciones_por_genero or {fila[3]: [] for fila in matriz_peliculas}

    # Caso base: calcular y retornar promedios cuando se procesan todas las vistas
    if indice >= len(matriz_registro_vistas):
        return {genero: (sum(cals) / len(cals) if cals else 0) for genero, cals in calificaciones_por_genero.items()}

    # Procesa la calificación actual si es mayor a 0
    vista = matriz_registro_vistas[indice]
    id_pelicula, calificacion = vista[3] - 1, int(vista[6])
    if calificacion > 0:
        calificaciones_por_genero[matriz_peliculas[id_pelicula][3]].append(calificacion)

    # Llamada recursiva con el siguiente índice
    return promedio_por_genero(matriz_peliculas, matriz_registro_vistas, indice + 1, calificaciones_por_genero)

def imprimir_promedios(matriz_peliculas, matriz_registro_vistas, calcular_promedio, titulo):
    promedios = calcular_promedio(matriz_peliculas, matriz_registro_vistas)
    print(f"\n{titulo}:")
    for item, promedio in promedios.items():
        if promedio > 0:  # Solo imprimir elementos con calificaciones mayores a 0
            print(f"{item}: {promedio:.2f}")
