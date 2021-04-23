from condicional import get_input

def convert_to_clp(dolares, valor_dolar):

    resultado = dolares * valor_dolar

    return resultado

def calculo_dolares(pesos, valorDolar):
    resultado = pesos / valorDolar
    redondeo = round(resultado, 2)
    txt = str(redondeo)
    return txt

def flujo(pais, valorDolar):
    pesos = get_input(float, f"¿Cuántos pesos {pais} tienes ?: ", "un numero valido")
    dolares = calculo_dolares(pesos, valorDolar)
    print(f"Tienes ${dolares} dolares")

if __name__ == '__main__':

    menu = """
        Bienvenido al conversor de monedas 🤑💸

        1- Pesos Colombianos
        2- Pesos Chilenos
        3- Pesos argentinos
        4- Pesos mexicanos
    """

    print(menu)

    opcion = get_input(int, "Elige una opción: ", "un numero valido")

    if opcion == 1:
        flujo("Colombianos", 3875)
    elif opcion == 2:
        flujo("Chilenos", 723.75)
    elif opcion == 3:
        flujo("Argentinos", 65)
    elif opcion == 4:
        valor_dolar = 24
        flujo("Mexicanos", 24)
    else:
        print("No existe esa opcion")