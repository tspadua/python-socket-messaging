import socket
from this import d

from _thread import *
import threading
 
def handleConnectionThread(conexao, addr):
    while True:
      dados = conexao.recv(1024)
      if (dados):
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
      
        conexao.sendall(bytes(response, encoding='utf-8'))
 
 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((socket.gethostname(), 5002))
  print(s)
  s.listen()
  while True:
    conexao, addr = s.accept()

    print(f"Cliente conectado: {addr}")
    start_new_thread(handleConnectionThread, (conexao, addr))