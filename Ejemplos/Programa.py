import os

def sumaDesdeIniHastaFin(ini, fin):
    s = 0       # La suma acumulada DEBE comenzar en cero

    i = ini
    while i<=fin: # Contador en rango [ini, fin)
        s = s+i

        i = i+1 # De uno en uno
    return s

if __name__ == '__main__':
    os.system('cls')

    ini = int(input('Ingresa ini '))
    fin = int(input('Ingresa fin '))

    s = sumaDesdeIniHastaFin(ini, fin)

    print(f's = {s}')
