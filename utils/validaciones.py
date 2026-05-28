def campo_vacio(valor):
    return valor is None or str(valor).strip() == ""


def validar_campos_obligatorios(datos):
    for campo, valor in datos.items():
        if campo_vacio(valor):
            return False, f"El campo '{campo}' es obligatorio."

    return True, "Datos válidos."


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje)

        if not campo_vacio(valor):
            return valor

        print("Este campo no puede estar vacío.")


def pedir_entero(mensaje):
    while True:
        valor = input(mensaje)

        try:
            return int(valor)
        except ValueError:
            print("ERROR: Debe ingresar un número entero válido.")


def pedir_decimal(mensaje):
    while True:
        valor = input(mensaje)

        try:
            return float(valor)
        except ValueError:
            print("ERROR: Debe ingresar un número decimal válido.")


def validar_identificacion_ecuatoriana(documento):
    doc = str(documento).strip()
    
    if len(doc) == 13:
        if doc[10:] != "001":
            return False, None
        cedula = doc[:10] 
    elif len(doc) == 10:
        cedula = doc
        doc = cedula + "001" 
    else:
        return False, None

    if not cedula.isdigit():
        return False, None
    
    provincia = int(cedula[:2])
    if not (1 <= provincia <= 24 or provincia == 30):
        return False, None

    if int(cedula[2]) >= 6:
        if len(doc) == 13:
            return True, doc
        return False, None

    verificador = int(cedula[9])
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    suma = 0

    for i in range(9):
        valor = int(cedula[i]) * coeficientes[i]
        if valor >= 10:
            valor -= 9
        suma += valor

    total_modulo = suma % 10
    digito_esperado = 0 if total_modulo == 0 else 10 - total_modulo

    if digito_esperado == verificador:
        return True, doc 
    return False, None