from pedir_datos_tablero import N
import random 

# Tamaño con N requerida
tableroTamaño = N

ubicacionSolucion = []

# Definimos la funcion para crear el tablero
tablero = [['_' for _ in range (tableroTamaño)] for _ in range(tableroTamaño)]

# Definimos la funcion para insertar palabras en la matriz
def generar_tablero(palabras):
    orientaciones = ['izquierda', 'arriba']
    for palabra in palabras:
        tamanioPalabra = len(palabra)

        ubicado = False 

        while not ubicado:
            orientacion = random.choice(orientaciones)
            if orientacion == 'izquierda': 
                paso_x = 1
                paso_y = 0
            if orientacion == 'arriba':
                paso_x = 0
                paso_y = 1

            x_position = random.randint(0, tableroTamaño)
            y_position = random.randint(0, tableroTamaño)

            ending_x = x_position + tamanioPalabra * paso_x
            ending_y = y_position + tamanioPalabra * paso_y

            if ending_x < 0 or ending_x >= tableroTamaño: continue
            if ending_y < 0 or ending_y >= tableroTamaño: continue

            ubicacionSolucion.append({"Palabra: " + palabra + " | X Inicial: "+ str(y_position+1) + " | Y Inicial: " + str(x_position+1) + " | X Final: " + str(ending_y+1) + " | Y Final: " + str(ending_x+1)})

            falloAlUbicar = False

            for i in range(tamanioPalabra):
                caracter = palabra[i]
                
                newPosition_x = x_position + i * paso_x
                newPosition_y = y_position + i * paso_y
                nuevaPosicionCaracter = tablero[newPosition_x][newPosition_y]

                if nuevaPosicionCaracter != '_':
                    if nuevaPosicionCaracter == caracter: continue
                else:
                    falloAlUbicar = True
                    break
            
            if falloAlUbicar:
                continue
            else:
                for i in range(tamanioPalabra):
                    caracter = palabra[i]

                    new_position_x = x_position + i * paso_x
                    new_position_y = y_position + i * paso_y

                    tablero[new_position_x][new_position_y] = caracter
                
                ubicado = True
    return tablero
    
# Reemplazo de espacios por letras
for x in range(tableroTamaño):
    for y in range(tableroTamaño):
        if (tablero[x][y] == '_'):
            tablero[x][y] = random.choice("abcdefghijklmnopqrstuvwxyz")
