def mostrar_menu():
    print("\nAplicación de Seguimiento de Películas y Series Vistas")
    print("Menú Principal")
    print("1. Usuarios")
    print("2. Películas/Series")
    print("3. Registros Vistos")
    print("4. Salir")

def mostrar_submenu(opcion):
    if opcion == '1':
        print("\nUsuarios")
        print("a. Agregar Usuario")
        print("b. Actualizar Usuario")
        print("c. Eliminar Usuario")
        print("d. Generar reporte")
        print("e. Volver al Menú Principal")
    elif opcion == '2':
        print("\nPelículas/Series")
        print("a. Agregar Película/Serie")
        print("b. Actualizar Película/Serie")
        print("c. Eliminar Película/Serie")
        print("d. Generar reporte")
        print("e. Volver al Menú Principal")
    elif opcion == '3':
        print("\nRegistros Vistos")
        print("a. Agregar Registro")
        print("b. Actualizar Registro")
        print("c. Eliminar Registro")
        print("d. Generar reporte")
        print("e. Volver al Menú Principal")

def mostrar_submenu_actualizar(opciones):
    while True: 
        print("Seleccione la opción que desea actualizar: ")
        for opcion in opciones:
            id = opciones.index(opcion) + 1
            print(f"({id}) {opcion}")
        try:
            opcion_seleccionada = int(input("Opción: "))
            if 1 <= opcion_seleccionada <= len(opciones):  # Verifica que esté en el rango
                return opciones[opcion_seleccionada - 1]  # Retorna la opción seleccionada
            else:
                print(f"Error: El número debe estar entre 1 y {len(opciones)}.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
