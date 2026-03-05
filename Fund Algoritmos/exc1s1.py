import time

a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))
if a + b > c and b + c > a and a + c > b:
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        if a == b and a != c or a == c and a != b or b == c and a != c:
            print("É um triângulo ísosceles retângulo")
        else:
            print("É um triângulo escaleno retângulo") 
    else:
        if a == b and a == c:
            print("É um triângulo equilátero")
        elif a == b and a != c or a == c and a != b or b == c and a != c:
            print("É um triângulo ísosceles")
        else:
            print("É um triângulo escaleno")        
        
else:
    print("isso não é nem um triângulo cara")
time.sleep(3)

# acho que vendi minha alma para aprender esse negócio tão rápido