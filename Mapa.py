class Mapa:
    def __init__(self):
        self.mapa = []
        self.generarMapaVacio()

    def colocarBarco(self,barco):
        for coord in barco.coords:
            fila = coord[0]
            col = coord[1]
            self.mapa[fila][col]="⛵"

    def generarMapaVacio(self):
        for i in range(10):
            fila = []
            for j in range(10):
                fila.append("~")
            self.mapa.append(fila)

    def imprimir(self):
        print("    A   B   C   D   E   F   G   H   I   J")
        for i in range(10):
            if i != 9:
                print(f"{i + 1}  {self.mapa[i]}")
            else:
                print(f"{i + 1} {self.mapa[i]}")

    def disparar(self, fila,col):
        if self.mapa[fila][col] == "⛵":
            self.mapa[fila][col] = "🔥"
            return "tocado"
        elif self.mapa[fila][col] == "~":
            self.mapa[fila][col] = "."
            return "agua"
        else:
            return "¡Zona ya disparada!"

    def mostrarMapa(self):
        print("    A   B   C   D   E   F   G   H   I   J")
        for i in range(10):
            if i < 9:
                print(f"{i + 1}   {self.mapa[i]}")
            else:
                print(f"{i + 1}  {self.mapa[i]}")