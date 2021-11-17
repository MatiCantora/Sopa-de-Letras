from pedir_datos_tablero import *
from generar_tablero import generar_tablero, tablero, ubicacionSolucion
import csv, os, time
    
# Definimos la funcion que busca la palabra en la sopa de letras
def buscar_palabra(palabra_usuario, jugador):
    for palabra in lista_palabras:
        if palabra == palabra_usuario:

            print("La palabra:",palabra, "fue encontrada!")
            input("Presione [Enter] para continuar")

            for index, value in enumerate(lista_palabras):
                if value == palabra:
                    lista_palabras[index] = palabra.upper()
                    print(lista_palabras)                
                    generar_tablero(lista_palabras)
                    break
            jugador.puntaje += 1
            break
    

# Funcion de puntaje
def jugar_sopa_letras(jugador):
    juego_terminado = False
    while not juego_terminado:
        if jugador.puntaje != len(lista_palabras):
            os.system("cls")
            print("\n")

            for fila in tablero:
                    for elemento in fila:
                        print(" {}|".format(elemento),end="")
                    print()

            print("Puntaje:", str(jugador.puntaje))
            print("\n")
            
            buscar_palabra(input("Palabra encontrada: "), jugador)
        else:
            juego_terminado = True



# Creamos la clase Jugador y pedimos su nombre
class Jugador:
    def __init__(self,):
        self.nombre = self.obtener_datos_usuario()
        self.puntaje = 0
        self.intentos = 0

    def obtener_datos_usuario(self):
        usuarioNombre = input("Nombre de usuario (no mayor a 40): ")
        if len(usuarioNombre) <= 40:
            return usuarioNombre
        else:
            self.obtener_datos_usuario("ERROR, el nombre del archivo es muy largo, intentar de nuevo: ")

# Creamos la clase Tablero y donde se guardará
class Tablero:
    def __init__(self, celdas, ubicacionSolucion,nombre):
        self.nombre_archivo = nombre
        self.guardar_tablero = self.guardar_tablero(celdas, ubicacionSolucion)
        
    def guardar_tablero(self,celdas, soluciones):
        with open(self.nombre_archivo + ".csv","w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter="|")
            writer.writerow(celdas)
            writer.writerows(tablero)

        with open(self.nombre_archivo + "_solucion" + ".csv","w", newline='') as csvfile:    
            writer = csv.writer(csvfile)
            writer.writerows(soluciones)

# Nos permite elegir el tablero en base a los "csv" que tenemos creados
def elegir_tablero():
    dir = '.'
    with os.scandir(dir) as ficheros:
        a=0
        for fichero in ficheros:
            if fichero.name.endswith(".csv"):
                a+=1
                print(str(a)+" - "+fichero.name)
    while True:
        i = input("Ingrese el número del tablero que quiere jugar: ")
        if(i.isnumeric()):
            if (int(i)>0 and int(i)<=a):
                break
    with os.scandir(dir) as ficheros:
        a=0
        for fichero in ficheros:
            if fichero.name.endswith(".csv"):
                a+=1
                if (a==int(i)):
                    with open(fichero) as archivo:
                        for matrix in archivo:
                            return(matrix)

# Creamos una cuenta regresiva para generar emocion :D
def countdown(num_of_secs):
        print("Espere, estamos trabajando en ello")
        while num_of_secs:
            m, s = divmod(num_of_secs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            print(min_sec_format)
            time.sleep(1)
            num_of_secs -= 1

        input("Todo listo, ENTER para jugar!")
        os.system("cls")

# El main() de toda nuestra Sopa
def main():
    nuevo_jugador = Jugador()
    nombre_archivo = pedir_nombre_archivo()
    pedir_datos_tablero()
    celdas = []
    generar_tablero(lista_palabras)
    soluciones = []
    nuevo_tablero = Tablero(celdas, ubicacionSolucion, nombre_archivo)
    tablero = elegir_tablero()
    countdown(10)
    jugar_sopa_letras(nuevo_jugador)
    print("El Juego ha terminado, Tu puntaje es de" + str(nuevo_jugador.puntaje) + " puntos")

main()

                      
