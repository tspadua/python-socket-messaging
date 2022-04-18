import socket
import sympy
from _thread import *

from this import d

def calculate_primes(code, n):
    i = 0
    prime_count_after = 0
    prime_count_before = 0

    prime_to_find_after = code
    prime_to_find_before = code

    while (prime_count_after < n or prime_count_before < n):
        i+=1
        current_sum = code+i
        current_sub = code-i
        if sympy.isprime(current_sum):
            prime_count_after += 1
            if (prime_count_after == n):
                prime_to_find_after = current_sum
        if sympy.isprime(current_sub):
            prime_count_before += 1
            if (prime_count_before == n):
                prime_to_find_before = current_sub
                
    return prime_to_find_before * prime_to_find_after

def handle_connection_thread(conexao, addr):
    while True:
      
      dados = conexao.recv(1024)
      if (dados):
        decoded = dados.decode()
        print(f"Mensagem recebida: {decoded}")

        inputs = decoded.split("&")
        print(inputs)
        if (len(inputs) > 1):
          code = int(inputs[0])
          n = int(inputs[1])

          key = str(calculate_primes(code, n))
          print("KEY " + key)
          print(conexao)
          conexao.sendall(bytes(key, encoding='utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((socket.gethostname(), 50003))
  print(s)
  s.listen()
  while True:
    conexao, addr = s.accept()

    print(f"Cliente conectado: {addr}")
    start_new_thread(handle_connection_thread, (conexao, addr))