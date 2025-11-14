
#Aleatorio
mapa = []

def generarMapaVacio(mapa):
    for i in range(10):
        mapa.append([])
        for j in range(10):
            mapa[i].append("~")
generarMapaVacio(mapa)

def printMapa(mapa):
    x = 1
    print("    A    B    C    D    E    F    G    H    J    K")
    for fila in mapa:
        if x != 10:
            print(f"{x} {fila}")
        else:
            print(f"{x}{fila}")
        x += 1

def generarMapaLleno(mapa):
    x = 1
    print("    A    B    C    D    E    F    G    H    J    K")
    for i in range(len(mapa)-1,-1,-1):
        if x != 10:
            print(f"{x} {mapa[i]}")
        else:
            print(f"{x}{mapa[i]}")
        x += 1
