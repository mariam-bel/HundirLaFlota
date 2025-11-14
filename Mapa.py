
#Aleatorio
mapa = []
def generarMapa(mapa):
    for i in range(10):
        mapa.append([])
        for j in range(10):
            mapa[i].append("~")
generarMapa(mapa)

def printMapa(mapa):
    x = 1
    print("    A    B    C    D    E    F    G    H    J    K")
    for fila in mapa:
        if x != 10:
            print(f"{x} {fila}")
        else:
            print(f"{x}{fila}")
        x += 1


printMapa(mapa)

