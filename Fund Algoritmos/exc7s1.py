import time

print("Definidor de números primos altamente funcional")

x = int(input("Digite um número de 1 a 1000: "))
divisores = 0

for i in range (2,x):
    if x % i == 0:
        divisores=divisores+1
if divisores==2:
    print("Primo")
else:
    print("Não é primo")

time.sleep(3)