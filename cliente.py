import socket

code = "15"
n = "6000"

message = code + "&" + n

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(("127.0.1.1", 5002))
  print(s)
  s.sendall(bytes(message, encoding='utf-8'))
  dados = s.recv(1024)
  print(f"Resposta do servidor: {dados.decode()}")