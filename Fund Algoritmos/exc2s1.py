import time

n = int(input("Escreva um número inteiro aleatório: "))
if n < 0:
    print("Você escreveu um número negativo")
elif n > 0:
    print("Você escreveu um número positivo")
else:
    print("Você digitou o número zero")

time.sleep(3)