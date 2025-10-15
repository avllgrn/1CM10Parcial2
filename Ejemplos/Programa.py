import os

if __name__ == '__main__':
    os.system('cls')

    ini = float(input('Ingresa inicio del contador '))
    fin = float(input('Ingresa fin del contador '))
    dec = float(input('Ingresa decremento del contador '))

    i = ini                     # Valor inicial de la variable contador
    while i > fin:              # Mientras el valor de i sea mayor al fin,
        print(f' {i} ')         # Se pinta el valor de la variable
        i = i-dec               # Con cada vuelta del ciclo, la variable decrementa su valor en dec
