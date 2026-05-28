def campo_vacio(valor):
    return valor is None or str(valor).strip() == ""


def validar_campos_obligatorios(datos):
    for campo, valor in datos.items():
        if campo_vacio(valor):
            return False, f"El campo '{campo}' es obligatorio."

    return True, "Datos válidos."


def pedir_texto(mensaje, validacion_extra= None):
    while True:
        valor = input(mensaje).strip()
        if campo_vacio(valor):
            print("Este campo no puede estar vacio")
            continue
        if validacion_extra:
            es_valido, resultado = validacion_extra(valor)
            if not es_valido:
                print("Error: El formato o número ingresado es inválido. Intente de nuevo.")
                continue
            return resultado
        return valor


def pedir_entero(mensaje, validacion_extra=None):
    while True:
        valor = input(mensaje).strip()
        try:
            numero =  int(valor)

            if validacion_extra is not None:
                if not validacion_extra(numero):
                    print("Error: El valor no cumple con los requisitos del sistema Intente de nuevo.")
                    continue
            return numero
        except ValueError:
            print("ERROR: Debe ingresar un número entero válido.")


def pedir_decimal(mensaje):
    while True:
        valor = input(mensaje).strip()
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

def pedir_cantidad_stock(mensaje, tipo_movimiento, stock_disponible):
    while True:
        cantidad = pedir_entero(mensaje)
        
        if cantidad == 0:
            return 0
        if cantidad < 0:
            print("Error: La cantidad debe ser mayor a cero. Intente de nuevo.")
            continue

        if tipo_movimiento == "VENTA" and stock_disponible < cantidad:
            print(f"Error: Stock insuficiente. Stock actual disponible: {stock_disponible}. Intente otra cantidad.")
            continue

        return cantidad