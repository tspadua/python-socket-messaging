import socket
import sympy
import concurrent.futures

from this import d

def calculatePrime(code, n):
    i = 0
    prime_count_after = 0
    prime_count_before = 0

    prime_to_find_after = code
    prime_to_find_before = code

    while (prime_count_after < n and prime_count_before < n):
        i+=1
        current_sum = code+i
        current_sub = code-i
        if sympy.isprime(current_sum):
            prime_count_after += 1
            if (prime_count_after == n):
                prime_to_find_after = current_sum
        if sympy.isprime(current_sub):
            prime_count_before += 1
            if (prime_count_after == n):
                prime_to_find_before = current_sub
                
    return [prime_to_find_before, prime_to_find_after]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((socket.gethostname(), 5003))
  print(s)
  s.listen()
  conexao, addr = s.accept()
  with conexao:
    print(f"Processo conectado: {addr}")
    while True:
      dados = conexao.recv(1024)
      if not dados:
        break
      decoded = dados.decode()
      print(f"Mensagem recebida: {decoded}")
      inputs = decoded.split("&")
      if (len(inputs) > 1):
        code = int(inputs[0])
        n = int(inputs[1])

        primes = calculatePrime(code, n)

        key = str(primes[0]*primes[1])
    
      conexao.sendall(bytes(key, encoding='utf-8'))