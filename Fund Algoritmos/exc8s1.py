import time

print("Somador de números altamente funcional")

acumulador = 0

for controlador in range (0,10):
    perg = int(input("Digite um número para somatória: "))
    acumulador=acumulador+perg
    if perg == 0:
        break
print(acumulador)

time.sleep(3)

# Soma 10 números aleatórios