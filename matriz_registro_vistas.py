#Matriz registro vistas
import validar

def crear_contenido_registro_vistas(contenido_registro_vistas, usuario_id,pelicula_id, estado, calificacion, matriz1, matriz2):
    apellido = validar.obtener_apellido_usuario(matriz2, usuario_id)
    titulo = validar.obtener_titulo_pelicula(matriz1, pelicula_id)
    
    item = [usuario_id, apellido, pelicula_id, titulo, estado, calificacion]
    contenido_registro_vistas.append(item)
    print(f"El usuario {usuario_id} ha actualizado el estado de la película/serie '{titulo}' con ID {pelicula_id}.")

def leer_contenido_registro_vistas(contenido_registro_vistas):
    if not contenido_registro_vistas:
        print("No hay contenido disponible.")
        return
    
    for item in contenido_registro_vistas:
        usuario_id,apellido, pelicula_id, titulo, estado, calificacion = item
        print(f"ID del usuario: {usuario_id}")
        print(f"Apellido: {apellido}")
        print(f"ID Pelicula/serie: {pelicula_id}")
        print(f"Titulo: {titulo}")
        print(f"Estado: {estado}")
        print(f"Calificacion: {calificacion}")
        print("-" * 30)

def actualizar_contenido_registro_vistas(contenido_registro_vistas, nuevo_id_registro, nuevo_id_pelicula, estado=None, calificacion=None):
    for item in contenido_registro_vistas:
        if item[0] == nuevo_id_registro:
            item[2] = nuevo_id_pelicula if nuevo_id_pelicula is not None and nuevo_id_pelicula != '' else item[2]
            item[4] = estado if estado is not None and estado != '' else item[4]
            item[5] = calificacion if calificacion is not None and calificacion != '' else item[5]
            print(f"Pelicula/serie con ID {item[2]} ingresado por el usuario con ID {nuevo_id_registro} actualizada.")
            return
    print(f"No se encontró el contenido con ID {nuevo_id_registro}.")

def eliminar_contenido_registro_vistas(contenido, item_id):
    for item in contenido:
        if item[0] == item_id:
            contenido.remove(item)
            print(f"El {item[2]} con ID {item_id} ha sido eliminado.")
            return
    print(f"No se encontró el contenido con ID {item_id}.")

def imprimir_matriz_registro_vistas(matriz3, ids_registro, encabezado_registros):
    """
    Pre: Recibe una matriz ya creada.
    Pos: Muestra por consola los elementos de la matriz.
    """
    # Imprimir el encabezado
    print(" " * 12, end="")  # Espacio para alinear con los nombres
    for i in encabezado_registros:
        print(f"{i:>15}", end="") 
    print()   

    # Imprimir cada fila con el nombre de la pelicula/serie
    for i in range(len(matriz3)):
        print(f"{ids_registro[i]:<12}", end="")
        for j in range(len(matriz3[i])):
            valor = str(matriz3[i][j]).capitalize() #mayuscula
            print(f"{valor:>15}", end="")
        print()

