import socket

server = socket.socket()
server.bind(("0.0.0.0", 5000))
server.listen(2)

print("Esperando jugadores...")

j1, _ = server.accept()
j2, _ = server.accept()

j1.send(b"OK")
j2.send(b"OK")
