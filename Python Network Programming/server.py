import socket
port = 1234
address = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address, port))
server.listen(5)
print("Listening...")

while True:
  con, addr = server.accept()
  print("Connected with", addr)
  con.send(bytes("Hello Client", "utf-8"))