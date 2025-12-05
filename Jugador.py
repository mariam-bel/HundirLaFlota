from typing import List

from Barco import *
from Mapa import *


class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.mapa = Mapa()
        self.mapaEnemigo = Mapa()
        self.mapaEnemigo.generarMapaVacio()

    def colocarBarcos(self,barco):
        self.mapaPropio.colocarBarco(barco)

    def dispararA(self,enemigo,fila,col):
        resultado = enemigo.mapaPropio.disparar(fila,col)
        if resultado == "¡Zona ya disparada!":
            self.mapaEnemigo.mapa[fila][col] = "🔥"
        elif resultado == "¡Agua tocada!":
            self.mapaEnemigo.mapa[fila][col] = "."
        return resultado