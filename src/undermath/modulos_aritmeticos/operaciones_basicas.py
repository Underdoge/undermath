def sumar(valores=[]):
    """ Acepta una lista con enteros o flotantos y los suma """

    suma = 0
    for valor in valores:
        try:
            valor = float(valor)
        except ValueError:
            print("Únicamente puedes sumar números enteros o flotantes, \
separados por espacios.")
            return
        suma += valor
    if isinstance(suma, float):
        print(f"Resultado de la suma: {suma}")


def restar(valores=[]):
    """ Resta el valor[1] del valor[0]"""

    resta = 0
    try:
        valores[0] = float(valores[0])
        valores[1] = float(valores[1])
        resta = valores[0] - valores[1]
    except ValueError:
        print("Únicamente puedes sumar enteros o flotantes.")
        return
    if isinstance(resta, float):
        print(f"Resultado de la resta: {resta}")


def multiplicar(valores=[]):
    """ Acepta una lista con enteros o flotantos y los multiplica """

    multiplicacion = 1
    for valor in valores:
        try:
            valor = float(valor)
        except ValueError:
            multiplicacion = None
            print("Únicamente puedes multiplicar números enteros o flotantes, \
separados por espacios.")
            return
        multiplicacion *= valor
    if isinstance(multiplicacion, float):
        print(f"Resultado de la multiplicacion: {multiplicacion}")


def dividir(valores=[]):
    """ Dividr el valor[0] entre valor[1]"""

    division = 0
    try:
        valores[0] = float(valores[0])
        valores[1] = float(valores[1])
        division = valores[0] / valores[1]
    except ValueError:
        print("Únicamente puedes dividir enteros o flotantes.")
    except ArithmeticError:
        print("No puedes dividir entre cero.")
        return
    if isinstance(division, float):
        print(f"Resultado de la división: {division}")
