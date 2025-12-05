from Jugador import Jugador
from Barco import Barco

jugador1 = Jugador("A")
jugador2 = Jugador("B")

barcosAcolocar = ["acorazado", "fragata", "fragata", "corbeta", "corbeta", "lancha", "lancha", "lancha"]

for nombre in barcosAcolocar:
    b1 = Barco(nombre)
    jugador1.mapa.colocarBarco(b1)
    b2 = Barco(nombre)
    jugador2.mapa.colocarBarco(b2)

def turnoDisparo(jugador, enemigo):
    enemigo.mapa.imprimir()
    while True:
        try:
            fila = int(input(f"{jugador.nombre}, fila (0-9): "))
            col = int(input(f"{jugador.nombre}, columna (0-9): "))
            if 0 <= fila <= 9 and 0 <= col <= 9:
                break
            else:
                print("Valores fuera de rango.")
        except:
            print("Introduce números válidos.")
    resultado = enemigo.mapa.disparar(fila, col)
    if resultado == "tocado":
        print("¡Barco tocado!")
    elif resultado == "agua":
        print("¡Agua tocada!")
    else:
        print("¡Zona ya disparada!")
    return resultado

def quedan_barcos(jugador):
    for fila in jugador.mapa.mapa:
        if "⛵" in fila:
            return True
    return False

turno = 1
while True:
    if turno == 1:
        resultado = turnoDisparo(jugador1, jugador2)
        if not quedan_barcos(jugador2):
            print("¡A ha ganado! 🎉")
            break
        if resultado == "agua":
            turno = 2
    else:
        resultado = turnoDisparo(jugador2, jugador1)
        if not quedan_barcos(jugador1):
            print("¡B ha ganado! 🎉")
            break
        if resultado == "agua":
            turno = 1
