
def get_input(typ, msg, err):
    while True:
        try:
            return typ(input(msg))
        except ValueError:
            print("Por favor ingresa {0}".format(err))