import time
print("Definidor de números primos altamente funcional")
x = int(input("Digite um número: "))
while x!=0:
    if x>1:
        Primo=True
        for i in range (2,x):
            if x % i==0:
                Primo=False
                break
        if not Primo:
            print("Não é Primo")
        else:
            print("Primo")        
    else:
        print("Primo")
    x = int(input("Digite um número: "))
time.sleep(3)
#Identificador de número primo que para quando digita 0