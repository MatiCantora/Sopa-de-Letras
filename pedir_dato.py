# Funcion pedir N
def pedir_dato():
    try:
        N= int(input("Ingresar un número mayor o igual a 15: "))
        # Validamos que N sea solo numérico
        if type(N) is int and N >= 15:
            return N
        else:
            return pedir_dato(int(input("ERROR, ingrese numero mayor o igual a 15: ")))
    except ValueError:
        input("ERROR, no ingresó un numero, [ENTER] para continuar...")
        return pedir_dato()
