from Barco import Barco
from Mapa import generarMapaVacio, printMapa, generarMapaLleno

mapa = []
generarMapaVacio(mapa)

printMapa(mapa)

def generarBarcos(mapa, posicion):
    barco = "🍆"
    mapa[posicion[0][0]][posicion[1][1]] = barco

b  = Barco("lancha")
b2 = Barco("corbeta")

generarBarcos(mapa, b2.coords)

generarMapaLleno(mapa)

