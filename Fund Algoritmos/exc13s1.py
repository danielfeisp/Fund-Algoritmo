def área(base,altura):
    x = base*altura/2
    return x
b = int(input("Digite a base do triângulo: "))
a = int(input("Digite a altura do triângulo: "))
triangulo = área(b,a)
print(triangulo)