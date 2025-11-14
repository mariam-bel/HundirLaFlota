class Barco:
    barcos = ["lancha","corbeta","fragata","acorazado"]
    def __init__(self, nombre):
        if nombre in self.barcos:
            self.__nombre = nombre.lower()
        else:
            raise NameError("Introduzca un barco correcto.")

    def __getNombre(self):
        return self.__nombre

    def getSize(self):
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