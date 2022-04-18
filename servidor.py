import socket
from this import d

from _thread import *
 
def handle_connection_thread(conexao, addr):
    while True:
      dados = conexao.recv(1024)
      if (dados):
        decoded = dados.decode()
        print(f"Mensagem recebida: {decoded}")

        inputs = decoded.split("&")

        key_params = "Unexpected range"
        if (len(inputs) > 1):
          code = int(inputs[0])
          n = int(inputs[1])

          if (n > 1 and n < 15000):
              if ((code) > 10):
                  key_params = inputs[0] + "&" + inputs[1]
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
          s2.connect(("127.0.1.1", 50003))
          s2.sendall(bytes(key_params, "utf-8"))
          keygen_response = str(s2.recv(1024))
          if (keygen_response):
            conexao.sendall(bytes(keygen_response, encoding='utf-8'))
 
 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((socket.gethostname(), 50002))
  print(s)
  s.listen()
  while True:
    conexao, addr = s.accept()

    print(f"Cliente conectado: {addr}")
    start_new_thread(handle_connection_thread, (conexao, addr))