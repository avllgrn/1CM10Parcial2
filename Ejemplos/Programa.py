import os

def contadorAscendente(ini, fin, inc):
    i = ini                     # Valor inicial de la variable contador
    while i < fin:              # Mientras el valor de i sea menor al fin,
        print(f' {i} ')         # Se pinta el valor de la variable
        i = i+inc               # Con cada vuelta del ciclo, la variable incrementa su valor en inc

def contadorDescendente(ini, fin, dec):
    i = ini                     # Valor inicial de la variable contador
    while i > fin:              # Mientras el valor de i sea mayor al fin,
        print(f' {i} ')         # Se pinta el valor de la variable
        i = i-dec               # Con cada vuelta del ciclo, la variable decrementa su valor en dec

if __name__ == '__main__':
    os.system('cls')

    ini = float(input('Ingresa inicio del contador '))
    fin = float(input('Ingresa fin del contador '))
    
    if ini < fin:
        inc = float(input('Ingresa incremento del contador '))

        if inc>0:                               # Si el incremento es positivo, 
            contadorAscendente(ini, fin, inc)   # se invoca la funcion que cuenta
        else:
            print('Error! Se genera ciclo infinito')

    else:
        dec = float(input('Ingresa decremento del contador '))

        if dec>0:                               # Si el decremento es positivo, 
            contadorDescendente(ini, fin, dec)   # se invoca la funcion que cuenta
        else:
            print('Error! Se genera ciclo infinito')
