import modulo_validar

# Prueba para correos válidos
def test_correos_validos():
    correos_validos = [
        "ejemplo@dominio.com",
        "nombre.apellido@dominio.co",
        "user+name@dominio.info",
        "user_name@dominio.net",
        "123user@dominio.com",
        "user@sub.dominio.com"
    ]
    for email in correos_validos:
        assert modulo_validar.validar_email(email) == True

# Prueba para correos inválidos
def test_correos_invalidos():
    correos_invalidos = [
        "ejemplo@dominio",               # Falta el TLD (e.g., .com)
        "@dominio.com",                  # Falta la parte del nombre
        "nombre@dominio.c",              # TLD de solo una letra
        "nombre.apellido@dominio,com",   # TLD con coma en vez de punto
        "nombre.apellido@dominio..com",  # TLD con doble punto
        "nombre apellido@dominio.com",   # Espacio en el correo
        "nombre@dominio_com"             # Guion bajo en el dominio
    ]
    for email in correos_invalidos:
        assert modulo_validar.validar_email(email) == False

# Prueba para dni válidos
def test_dni_valido():
    dnis_validos = [
        "12.345.678",
        "01.234.567",
        "99.999.999",
        "00.000.000",
    ]
    for dni in dnis_validos:
        assert modulo_validar.validar_dni(dni) == True

# Prueba para dni inválidos
def test_dni_invalido():
    dnis_invalidos = [
        "12345678",         # Sin puntos
        "12.3456.78",       # Formato incorrecto
        "123.456.789",      # Primera sección de 3 dígitos
        "12.345.6789",      # Última sección con 4 dígitos
        "12.34.5678",       # Sección intermedia de 2 dígitos
        "AA.BBB.CCC",       # Letras en vez de dígitos
        "12-345-678",       # Uso de guiones en vez de puntos
        " 12.345.678 ",     # Espacios adicionales
        "",                 # Cadena vacía
    ]
    for dni in dnis_invalidos:
        assert modulo_validar.validar_dni(dni) == False

# Prueba para años válidos
def test_anios_validos():
    anios_validos = [
        "1900", "1999", "2000", "2099", "2023", "1987"
    ]
    for anio in anios_validos:
        assert modulo_validar.validar_anio(anio) == True

# Prueba para años inválidos
def test_anios_invalidos():
    anios_invalidos = [
        "1800",         # Año fuera de rango (anterior a 1900)
        "2100",         # Año fuera de rango (posterior a 2099)
        "1899",         # Año fuera de rango (anterior a 1900)
        "2200",         # Año fuera de rango (posterior a 2099)
        "abcd",         # Caracteres no numéricos
        "20A1",         # Mezcla de caracteres y números
        "202",          # Año incompleto (menos de 4 dígitos)
        "20234",        # Año con más de 4 dígitos
        "",             # Cadena vacía
        " 2000 ",       # Año con espacios
    ]
    for anio in anios_invalidos:
        assert modulo_validar.validar_anio(anio) == False