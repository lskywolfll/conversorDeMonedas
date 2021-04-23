
def get_input(typ, msg, err):
    while True:
        try:
            return typ(input(msg))
        except ValueError:
            print("Por favor ingresa {0}".format(err))

# edad = get_input(int, "Escribe tu edad: ", "un numero valido")

# if edad > 17:
#     print("Eres mayor")
# else:
#     print("Eres menor")