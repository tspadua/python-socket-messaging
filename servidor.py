import socket
from this import d

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((socket.gethostname(), 5002))
  print(s)
  s.listen()
  conexao, addr = s.accept()
  with conexao:
    print(f"Cliente conectado: {addr}")
    while True:
      dados = conexao.recv(1024)
      if not dados:
        break
      decoded = dados.decode()
      print(f"Mensagem recebida: {decoded}")

      inputs = decoded.split("&")

      response = "Unexpected range"
      if (len(inputs) > 1):
        code = int(inputs[0])
        n = int(inputs[1])

        if (n > 5000 and n < 15000):
            if ((code) > 10):
                response = inputs[0] + "&" + inputs[1]

        s.connect(("127.0.1.1", 5003))
    
      conexao.sendall(bytes(response, encoding='utf-8'))