import os

def sumaDesdeCeroHasta(n):
    s = 0       # La suma acumulada DEBE comenzar en cero

    i = 0       
    while i<=n: # Contador en rango [0, n)
        s = s+i

        i = i+1 # De uno en uno
    return s

if __name__ == '__main__':
    os.system('cls')

    n = int(input('Ingresa n '))

    s = sumaDesdeCeroHasta(n)

    print(f's = {s}')
