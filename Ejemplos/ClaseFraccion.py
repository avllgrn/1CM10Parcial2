from os import system

class Fraccion:
    def __init__(self, numerador=0, denominador=1):
        try:
            self.numerador = int(numerador)
            self.denominador = int(denominador)
        except:
            self.numerador = 0
            self.denominador = 1
        print(f'Objeto {self} construido')

    def __del__(self):
        print(f'Objeto {self} destruido')

    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    def pideleAlUsuarioTuEstado(self):
        try:
            self.numerador = int(input('Ingresa numerador '))
            self.denominador = int(input('Ingresa denominador '))
        except:
            self.numerador = 0
            self.denominador = 1

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, numerador, denominador):
        try:
            self.numerador = int(numerador)
            self.denominador = int(denominador)
        except:
            self.numerador = 0
            self.denominador = 1

    def guardaTuEstado(self, ArchivoSalida):
        ArchivoSalida.write(f'{self.numerador},{self.denominador}')

    def cargaTuEstado(self, ArchivoEntrada):
        datos = ArchivoEntrada.readline().split(',')
        self.numerador = int(datos[0])
        self.denominador = int(datos[1])

if __name__ == '__main__':
    system('cls')
