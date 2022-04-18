import socket

code = "15000"
n = "6000"

message = code + "&" + n

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(("127.0.1.1", 50002))
  print(s)
  s.sendall(bytes(message, encoding='utf-8'))

  while (True):
    dados = s.recv(1024)
    if (dados):
      print(f"Resposta do servidor: {dados.decode()}")
