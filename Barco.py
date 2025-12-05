import random

class Barco:
    barcos = ["lancha","corbeta","fragata","acorazado"]
    todasCoordenadas = []
    def __init__(self, nombre):
        if nombre in self.barcos:
            self.__nombre = nombre.lower()
        else:
            raise NameError("Introduzca un barco correcto.")
        self.__size = self.__getSize
        self.__coords = self.__generateCoords(self.__size, self.todasCoordenadas)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def coords(self):
        return self.__coords

    @property
    def __getSize(self):
        size = 0
        if(self.__nombre == "lancha"):
            size = 1
        if(self.__nombre == "corbeta"):
            size = 2
        if(self.__nombre == "fragata"):
            size = 3
        if(self.__nombre == "acorazado"):
            size = 4
        return size

    @staticmethod
    def __generateCoords(size, coords):
        while True:
            orientacion = random.randint(0,1)

            if orientacion == 0:
                fila = random.randint(0,9)
                col_inicio = random.randint(0,9-size)
                coordenada = [[fila,col_inicio + i] for i in range(size)]
            else:
                col = random.randint(0, 9)
                fila_inicio = random.randint(0, 9 - size)
                coordenada = [[fila_inicio + i, col] for i in range(size)]

            if any(c in coords for c in coordenada):
                continue

            for c in coordenada:
                coords.append(c)

            return coordenada

    def __str__(self):
        return f"Barco: {self.__nombre} | Tamaño: {self.__getSize} | Coordenadas: {self.__coords}"



b  = Barco("lancha")
b2 = Barco("corbeta")
b3 = Barco("corbeta")
b4 = Barco("corbeta")
b5 = Barco("fragata")
b6 = Barco("acorazado")
print(b)
print(b2)
print(b3)
print(b4)
print(b5)
print(b6)

