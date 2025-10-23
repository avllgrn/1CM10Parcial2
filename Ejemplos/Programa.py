import os
import math

def serieFibonacci(n):
    s = 0       # La suma acumulada DEBE comenzar en cero

    a = 0
    b = 1

    if n>=0 and n<=1:
        print(f'{a}')
        if n==1:
            print(f'{b}')
    elif n>1:
        print(f'{a}')
        print(f'{b}')
        i=2         # Contador en rango [2, n]
        while i<=n:
            c = a+b
            print(f'{c}')
            a=b
            b=c
            i = i+1

if __name__ == '__main__':
    os.system('cls')

    n = int(input('Ingresa n '))
    print()

    serieFibonacci(n)
    print()
