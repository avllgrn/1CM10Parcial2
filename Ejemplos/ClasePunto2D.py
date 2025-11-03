from os import system

class Punto2D:
    def __init__(self, x=0.0, y=0.0):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            self.x = 0.0
            self.y = 0.0
        print(f'Objeto {self} construido')

    def __del__(self):
        print(f'Objeto {self} destruido')

    def __str__(self):
        return f'({self.x}, {self.y})'

    def pideleAlUsuarioTuEstado(self):
        try:
            self.x = float(input('Ingresa x '))
            self.y = float(input('Ingresa y '))
        except:
            self.x = 0.0
            self.y = 0.0

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            self.x = 0.0
            self.y = 0.0

    def guardaTuEstado(self, ArchivoSalida):
        ArchivoSalida.write(f'{self.x},{self.y}')

    def cargaTuEstado(self, ArchivoEntrada):
        datos = ArchivoEntrada.readline().split(',')
        self.x = float(datos[0])
        self.y = float(datos[1])

if __name__ == '__main__':
    system('cls')
