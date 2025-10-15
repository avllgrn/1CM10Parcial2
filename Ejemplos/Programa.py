import os

if __name__ == '__main__':
    os.system('cls')

    i = 10
    while i >= 0:               # Mientras el valor de i sea mayor o igual a cero,
        print(f' {i} ')         # Se pinta el valor de la variable
        i = i-1                 # Con cada vuelta del ciclo, la variable decrementa su valor en uno
