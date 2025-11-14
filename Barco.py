import random


class Barco:
    barcos = ["lancha","corbeta","fragata","acorazado"]
    coords = []
    def __init__(self, nombre):
        if nombre in self.barcos:
            self.__nombre = nombre.lower()
        else:
            raise NameError("Introduzca un barco correcto.")
        self.__size = self.__getSize
        self.__coords = self.__generateCoords(self.__size, self.coords)


    def __getNombre(self):
        return self.__nombre

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
        coordenadasBarco = []
        for i in range(size):
            coord = [random.randint(0,10),random.randint(0,10)]
            while coord in coords:
                coord = [random.randint(0, 10), random.randint(0, 10)]
            coordenadasBarco.append(coord)
            coords.append(coord)
        return coordenadasBarco

    def __str__(self):
        return f"Barco: {self.__nombre} | Tamaño: {self.__getSize} | Coordenadas: {self.__coords}"


b  = Barco("lancha")
b2 = Barco("corbeta")
b22 = Barco("corbeta")
b3 = Barco("fragata")
b4 = Barco("acorazado")
print(b)
print(b2)
print(b22)
print(b3)
print(b4)