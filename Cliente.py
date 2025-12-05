import socket

c = socket.socket()
c.connect(("127.0.0.1", 5000))

msg = c.recv(1024)
print("Conectado al servidor")