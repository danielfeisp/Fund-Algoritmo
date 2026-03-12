import time
def eh_primo (numero_verificar):
    primo = True
    for i in range(2,numero_verificar):
        if numero_verificar % i == 0:
            primo = False
    return primo
print("Definidor de números primos altamente funcional")
n = int(input("Digite um número: "))
while(n != 0):
    v= eh_primo(n)
    if v==False:
        print("Não é Primo")
    else:
        print("É primo")
    n=int(input("Digite um número: "))
time.sleep(3)
# Número primo, porém definindo uma função "eh_primo", tem menos linhas