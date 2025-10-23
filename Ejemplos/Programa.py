import os

def factorial(n):
    f = 1       # La multiplicación acumulada DEBE comenzar en uno

    i = 1
    while i<=n: # Contador en rango [1, fin]
        f = f*i

        i = i+1 # De uno en uno
    return f

if __name__ == '__main__':
    os.system('cls')

    n = int(input('Ingresa n '))

    f = factorial(n)

    print(f'{n}! = {f}')
