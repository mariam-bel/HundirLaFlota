import socket

class Servidor:
    def __init__(self, puerto=5000):
        self.server = socket.socket()
        self.server.bind(("0.0.0.0", puerto))
        self.server.listen(2)

        print("Esperando jugadores...")
        self.j1, _ = self.server.accept()

        print("Jugador 1 conectado")
        self.j2, _ = self.server.accept()

        print("Jugador 2 conectado")
        self.j1.send(b"OK")
        self.j2.send(b"OK")


        def enviar(self, jugador, mensaje):
            jugador.send(mensaje.encode())


        def recibir(self, jugador):
            return jugador.recv(1024).decode()


        def iniciarPartida(self):
            turno = 1
            while True:
                if turno == 1:
                    self.enviar(self.j1, "TURNO")
                    self.enviar(self.j2, "ESPERA")
                    coords = self.recibir(self.j1)
                    self.enviar(self.j2, coords)
                    turno = 2
                else:
                    self.enviar(self.j2, "TURNO")
                    self.enviar(self.j1, "ESPERA")
                    coords = self.recibir(self.j2)
                    self.enviar(self.j1, coords)
                    turno = 1