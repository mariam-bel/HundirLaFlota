from Barco import Barco
from Mapa import generarMapaVacio, printMapa, generarMapaLleno

mapa = []
generarMapaVacio(mapa)

printMapa(mapa)

"""
    Necesitamos:
        1 portaaviones
        3 lanchas 
        2 corbetas
        2 fragats
"""

def generarBarcos(mapa,posicion, icono = "⛵"):
    for fila,col in posicion:
        mapa[fila][col] = icono

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

generarBarcos(mapa, b2.coords)
generarBarcos(mapa, b3.coords)
generarBarcos(mapa, b4.coords)
generarBarcos(mapa, b5.coords)
generarBarcos(mapa, b6.coords)

generarMapaLleno(mapa)

