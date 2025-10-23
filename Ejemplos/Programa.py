import os
import math

def factorial(n):
    f = 1       # La multiplicación acumulada DEBE comenzar en uno

    i = 1
    while i<=n: # Contador en rango [1, fin]
        f = f*i

        i = i+1 # De uno en uno
    return f

def serieE(x, n):
    s = 0

    i = 0
    while i<=n:
        # print(f'i = {i}\te^{x} = {s}')
        s = s + math.pow(x, i)/factorial(i)
        i = i+1
    return s

if __name__ == '__main__':
    os.system('cls')

    x = float(input('Ingresa x '))
    n = int(input('Ingresa n '))
    print()

    e = serieE(x, n)

    print()
    print(f'e^{x}! = {e}')
