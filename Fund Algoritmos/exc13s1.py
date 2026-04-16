import time
def área(base,altura):
    x = base*altura/2
    return x
b = int(input("Digite a base do triângulo: "))
a = int(input("Digite a altura do triângulo: "))
while b>0 and a>0:
    triangulo = área(b,a)
    print(triangulo)
    b = int(input("Digite a base do triângulo: "))
    a = int(input("Digite a altura do triângulo: "))
time.sleep(3)
# Define a área de um triângulo