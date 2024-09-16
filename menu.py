def mostrar_menu():
    print("\nAplicación de Seguimiento de Películas y Series Vistas")
    print("Menú Principal")
    print("1. Usuarios")
    print("2. Películas/Series")
    print("3. Registros Vistos")
    print("4. Salir")

def mostrar_submenu(opcion):
    if opcion == '1':
        print("Usuarios")
        print("a. Agregar Usuario")
        print("b. Listar Usuarios")
        print("c. Actualizar Usuario")
        print("d. Eliminar Usuario")
        print("e. Generar reporte")
        print("f. Volver al Menú Principal")
    elif opcion == '2':
        print("Películas/Series")
        print("a. Agregar Película/Serie")
        print("b. Listar Películas/Series")
        print("c. Actualizar Película/Serie")
        print("d. Eliminar Película/Serie")
        print("e. Generar reporte")
        print("f. Volver al Menú Principal")
    elif opcion == '3':
        print("Registros Vistos")
        print("a. Agregar Registro")
        print("b. Listar Registros")
        print("c. Actualizar Registro")
        print("d. Eliminar Registro")
        print("e. Generar reporte")
        print("f. Volver al Menú Principal")