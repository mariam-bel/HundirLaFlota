import random

class Barco:
    tamanyos = {
        "lancha": 1,
        "corbeta": 2,
        "fragata": 3,
        "acorazado": 4
    }

    todasCoordenadas = []

    def __init__(self, nombre):
        nombre = nombre.lower()

        if nombre not in Barco.tamanyos:
            raise Exception("Tipo de barco no válido.")

        self.nombre = nombre
        self.tamanyo = Barco.tamanyos[nombre]
        self.coords = self.generarCoords()

    def generarCoords(self):
        generado = False

        while not generado:
            orientacion = random.randint(0, 1)
            coordenadas = []

            if orientacion == 0:
                fila = random.randint(0, 9)
                col_inicio = random.randint(0, 9 - self.tamanyo)
                for i in range(self.tamanyo):
                    coordenadas.append([fila, col_inicio + i])

            else:
                col = random.randint(0, 9)
                fila_inicio = random.randint(0, 9 - self.tamanyo)
                for i in range(self.tamanyo):
                    coordenadas.append([fila_inicio + i, col])

            valido = True
            for c in coordenadas:
                if c in Barco.todasCoordenadas:
                    valido = False
                    break

            if valido:
                for c in coordenadas:
                    Barco.todasCoordenadas.append(c)
                generado = True

        return coordenadas
    def __str__(self):
        return f"Barco: {self.nombre} Coordendas: ({self.coords}) Tamaño: {self.tamanyo}"
