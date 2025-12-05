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

def generarPosDisparo(mapa):
    pos = (int(input("Infrese la letra a la que quiere disparar: ")),int(input("Ingrese la posición de la letra: ")))
    return pos

def generarDisparo(mapa,D, icono = "✨"):
    mapa[D[0]][D[1]] = icono

b  = Barco("lancha")
corbeta1 = Barco("corbeta")
corbeta2 = Barco("corbeta")
corbeta3 = Barco("corbeta")
fragata1 = Barco("fragata")
acorazado1 = Barco("acorazado")

print(corbeta1)
print(corbeta2)
print(corbeta3)
print(fragata1)
print(acorazado1)

generarBarcos(mapa, corbeta1.coords)
generarBarcos(mapa, corbeta2.coords)
generarBarcos(mapa, corbeta3.coords)
generarBarcos(mapa, fragata1.coords)
generarBarcos(mapa, acorazado1.coords)



fin = False
while not fin:
    posDisparo = generarPosDisparo(mapa)
    generarDisparo(mapa, posDisparo)
    generarMapaLleno(mapa)
    if posDisparo[0]==corbeta3.coords[0] and posDisparo[1]==corbeta3.coords[1]:
        print("MUY BIEN")
    else:
        print("MAL, GIL 🤸🏻")
