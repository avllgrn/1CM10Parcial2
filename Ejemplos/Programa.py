import os
import math

def gradosAradianes(grados):
    return grados * math.pi / 180

def funcion1():
    grados = float(input('Ingresa grados '))
    radianes = gradosAradianes(grados)
    print(f'{grados}° = {radianes} rad')

def fDeXcuadrada(x):
    return x**2

def funcion2():
    x = float(input('Ingresa x '))
    y = fDeXcuadrada(x)
    print(f'f({x}) = {y}')

def selecciona(opcion):
    match opcion:
        case '1':
            funcion1()
        case '2':
            funcion2()
        case '3':
            print('Adiós! =)')
        case _:
            print('Opción invalida... =(')

def menu():
    os.system('cls')
    print('1. Grados a radianes')
    print('2. f(x) = x^2')
    print('3. Salir')
    opcion = input('¿Cuál es tu opción? ')
    os.system('cls')
    selecciona(opcion)
    return opcion

if __name__ == '__main__':
    os.system('cls')

    while menu() != '3':   # Mientras la funcion menu retorne valores distintos de tres, continúa el ciclo
        input('\n\nPresiona una tecla para continuar...')
