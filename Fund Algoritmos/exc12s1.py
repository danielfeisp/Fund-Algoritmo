import time
def fatorial(numero_paia):
    f = 1
    for i in range (1,numero_paia+1):
        f = f*i
    return f
x = int(input("Digite um número: "))
while x!=0:
    print(fatorial(x))
    x = int(input("Digite um número: "))
time.sleep(3)
# Determina o resultado de fatorial de um número
