from Jugador import Jugador
from Barco import Barco

jugador1 = Jugador("Jugador 1")
jugador2 = Jugador("Jugador 2")

barcosAcolocar = ["acorazado", "fragata", "fragata", "corbeta", "corbeta", "lancha", "lancha", "lancha"]

for nombre in barcosAcolocar:
    b1 = Barco(nombre)
    jugador1.mapa.colocarBarco(b1)
    b2 = Barco(nombre)
    jugador2.mapa.colocarBarco(b2)

def turnoDisparo(jugador, enemigo):
    print(f"\n{jugador.nombre} - tu mapa:")
    jugador.mapa.imprimir()
    print(f"\n{jugador.nombre} - mapa del enemigo:")
    for i in range(10):
        fila = []
        for j in range(10):
            val = enemigo.mapa.mapa[i][j]
            if val == "🔥" or val == ".":
                fila.append(val)
            else:
                fila.append("~")
        print(fila)

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
    val = enemigo.mapa.mapa[fila][col]
    if val == "⛵":
        enemigo.mapa.mapa[fila][col] = "🔥"
        print("¡Tocado!")
    elif val == "~":
        enemigo.mapa.mapa[fila][col] = "."
        print("Agua…")
    else:
        print("Ya habías disparado aquí.")
    return val

def barcosRestantes(jugador):
    for fila in jugador.mapa.mapa:
        if "⛵" in fila:
            return True
    return False

turno = 1
while True:
    if turno == 1:
        resultado = turnoDisparo(jugador1, jugador2)
        if not barcosRestantes(jugador2):
            print("\n¡Jugador 1 ha ganado! 🎉")
            break
        if resultado == "~":
            turno = 2
    else:
        resultado = turnoDisparo(jugador2, jugador1)
        if not barcosRestantes(jugador1):
            print("\n¡Jugador 2 ha ganado! 🎉")
            break
        if resultado == "~":
            turno = 1
