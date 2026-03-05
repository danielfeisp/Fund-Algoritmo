import time

peso = float(input("Digite seu peso, em kilogramas aqui: ").replace(',', '.'))
altura = float(input("Digite sua altura, em metros, aqui: ").replace(',', '.'))
IMC = peso / altura ** 2

if IMC < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= IMC < 24.99:
    print("Você está com o seu peso ideal, Parabéns")
elif 25.0 <= IMC < 29.99:
    print("Você está levemente acima do peso")
elif 30.0 <= IMC < 34.99:
    print("Você possui obesidade grau I")
elif 35.0 <= IMC < 39.99:
    print("Você possui obesidade grau II (severa)")
else:
    print("Você possui obesidade grau III (mórbida)")

time.sleep(3)