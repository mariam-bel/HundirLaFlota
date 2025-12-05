import socket

class Cliente:
    def __init__(self, ip="127.0.0.1", puerto=5000):
        self.c = socket.socket()
        self.c.connect((ip, puerto))
        print(self.c.recv(1024).decode())


    def enviar(self, mensaje):
        self.c.send(mensaje.encode())


    def recibir(self):
        return self.c.recv(1024).decode()


    def iniciar(self):
        while True:
            estado = self.recibir()
            if estado == "TURNO":
                print("¡Tu turno, furcia!")
                fila = input("Fila 0-9: ")
                col = input("Columna 0-9: ")
                self.enviar(f"{fila},{col}")
        else:
            print("Esperando al otro jugador...👀")
            coords = self.recibir()
            print(f"El enemigo disparó a: {coords} 🙊")