def validar_entrada(valores=[]):
    lista_flotantes = []
    for valor in valores:
        try:
            lista_flotantes.append(float(valor))
        except ValueError:
            return False
    return lista_flotantes


def media(valores=[]):
    """ Acepta una lista con enteros o flotantes y obtiene la media """

    media = 0
    for valor in valores:
        try:
            valor = float(valor)
        except ValueError:
            print("Únicamente puedes usar números enteros o flotantes, \
separados por espacios.")
            return
        media += valor
    if isinstance(media, float):
        print(f"La media es: {media/len(valores)}")


def mediana(valores=[]):
    """ Acepta una lista con enteros o flotantes y obtiene la mediana """

    if validar_entrada(valores):
        mediana = 0
        valores.sort()
        mitad = len(valores) // 2
        mediana = (float(valores[mitad]) + float(valores[~mitad])) / 2
        print(f"La mediana es: {mediana}")
    else:
        print("Únicamente puedes usar números enteros o flotantes, \
separados por espacios.")


def moda(valores=[]):
    """ Acepta una lista con enteros o flotantes y obtiene la moda """

    if validar_entrada(valores):
        print(f"La moda es {max(set(valores), key=valores.count)}")
    else:
        print("Únicamente puedes usar números enteros o flotantes, \
separados por espacios.")


def desviacion_estandar_muestral(valores=[]):
    """ Acepta una lista con enteros o flotantes y obtiene la desviacion
    estandar muestral """

    if validar_entrada(valores):
        valores = validar_entrada(valores)
        print(f"La desviación estándar muestral es \
{(sum((float(x)-(sum(valores) / len(valores)))**2 for x in valores) / (len(valores)-1))**0.5}.")
    else:
        print("Únicamente puedes usar números enteros o flotantes, \
separados por espacios.")


def desviacion_estandar_poblacional(valores=[]):
    """ Acepta una lista con enteros o flotantes y obtiene la desviacion
    estandar poblacional """

    if validar_entrada(valores):
        valores = validar_entrada(valores)
        print(f"La desviación estándar poblacional es \
{(sum((float(x)-(sum(valores) / len(valores)))**2 for x in valores) / (len(valores)))**0.5}.")
    else:
        print("Únicamente puedes usar números enteros o flotantes, \
separados por espacios.")
