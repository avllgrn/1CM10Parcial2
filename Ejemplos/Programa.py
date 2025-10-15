import os
import math
import matplotlib.pyplot

def gradosAradianes(grados):
    return grados * math.pi / 180

def fDeXseno(xGrados):
    xRadianes = gradosAradianes(xGrados)                    # Se convierte a radianes los grados recibidos
    return math.sin(xRadianes)                              # Se contesta el seno de los radianes convertidos

def grafica():
    ini = float(input('Ingresa inicio de la gráfica '))
    fin = float(input('Ingresa fin de la gráfica '))
    inc = math.fabs( float(input('Ingresa incremento de la tabla ')) )

    if inc!=0:                                              # Si hay incremento, 

        X = []                                              # Se define una lista vacía, para los valores que tomará x
        Y = []                                              # Se define una lista vacía, para los valores que tomará y

        # Contador para generar los valores de la gráfica
        i = ini                                             # Se inicializa el contador
        while i<fin:                                        # Se condiciona el final del contador

            X.append( i )                                   # Se agrega el valor actual del contador i,                      a la lista X
            Y.append( fDeXseno(i) )                         # Se agrega el valor actual del contador i evaluado en fDeXseno, a la lista Y 

            i = i+inc                                       # Se incrementa el contador


        # Después de generar los valores,
        matplotlib.pyplot.plot(X,Y)                         # Se genera la gráfica (en memoria)
        matplotlib.pyplot.show()                            # Se muestra la gráfica

    else:
        print('Error! Se genera ciclo infinito')


if __name__ == '__main__':
    os.system('cls')

    grafica()
