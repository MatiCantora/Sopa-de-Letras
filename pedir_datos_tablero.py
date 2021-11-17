from pedir_dato import pedir_dato
import math

# Creamos una lista vacía y el nombre del archivo
lista_palabras = []
archivoNombre = ""

# Pedimos N y definimos la cantidad de palabras
N = pedir_dato()
numeroDePalabras = math.floor(N / 3) - 1

# Definimos la funcion pedir datos tablero
def pedir_datos_tablero():
    for palabra in range(numeroDePalabras):
        palabra = (
            input("Ingrese las palabras o [fin] para terminar: ").lower())
        if len(palabra) > (N / 3):
            print("la palabra no se puede incluir en la sopa de letras")
        elif palabra in lista_palabras:
            print("la palabra '{}' ya fue ingresada".format(palabra))
        elif palabra == "fin":
            break
        else:
            lista_palabras.append(palabra)

        print(lista_palabras)

# Definimos la funcion nombre archivo
def pedir_nombre_archivo():
    archivoNombre = input("Nombre del archivo: ")
    if len(archivoNombre) <= 40:
        return archivoNombre
    else:
        pedir_nombre_archivo(
            "El nombre del archivo es muy largo, intentar de nuevo: ")
