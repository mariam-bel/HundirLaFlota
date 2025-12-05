class Mapa:
    def __init__(self):
        self.size = 10
        self.mapa = [["~"for _ in range(self.size)] for _ in range(self.size)]

    # Aleatorio
    def generarBarco(self,barco):
        for fila,col in barco.coords:
            self.mapa[fila][col] = barco.icono

    #Manual
    def generarBarcoManual(self,barco,coords):
        if len(coords) != barco.size:
            raise ValueError("Las coordenadas deben ser acorde al mapa.")
        if not self.validarCoords(coords):
            raise ValueError("Coordenadas fuera del mapa.")
        barco.coords = coords
        for f,c in coords:
            self.mapa[f][c] = barco.icono

    def disparo(self,fila,col):
        celda = self.mapa[fila][col]
        if celda =="~":
            self.mapa[fila][col] = "."
            return "Has tocado agua"
        if celda == "⛵":
            self.mapa[fila][col] = "🔥"
            return "¡Barco tocado!"
        if celda in [".", "🔥"]:
            raise ValueError("Ya has disparado en esta posición.")

    def generarMapa(self):
        mapa = []
        for i in range(10):
            mapa.append([])
            for j in range(10):
                mapa[i].append("~")