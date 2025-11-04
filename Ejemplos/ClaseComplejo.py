from os import system

class Complejo:
    def __init__(self, real=0.0, imaginario=0.0):
        try:
            self.real = float(real)
            self.imaginario = float(imaginario)
        except:
            self.real = 0.0
            self.imaginario = 0.0
        print(f'Objeto {self} construido')

    def __del__(self):
        print(f'Objeto {self} destruido')

    def __str__(self):
        cadena = f'{self.real}'
        if self.imaginario>=0:
            cadena += '+'
        cadena += f'{self.imaginario}'+'i'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        try:
            self.real = float(input('Ingresa real '))
            self.imaginario = float(input('Ingresa imaginario '))
        except:
            self.real = 0.0
            self.imaginario = 0.0

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, real, imaginario):
        try:
            self.real = float(real)
            self.imaginario = float(imaginario)
        except:
            self.real = 0.0
            self.imaginario = 0.0

    def guardaTuEstado(self, ArchivoSalida):
        ArchivoSalida.write(f'{self.real},{self.imaginario}')

    def cargaTuEstado(self, ArchivoEntrada):
        datos = ArchivoEntrada.readline().split(',')
        self.real = float(datos[0])
        self.imaginario = float(datos[1])

if __name__ == '__main__':
    system('cls')
