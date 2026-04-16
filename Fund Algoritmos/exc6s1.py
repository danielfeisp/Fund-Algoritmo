import time

vv = int(input("Digite a velocidade da via: "))
vc = int(input("Digite a velocidade do carro: "))
m = float(((vc-vv)/vv)*100)

if 0<m<20:
    print("Velocidade {:.0f}% acima do limite".format(int(m)))
    print("Penalidade: Multa de R$ 130,16.")
    print("Pontuação: 4 pontos na CNH.")
elif 0>=m:
    print("Velocidade do carro está dentro da velocidade da via")
elif 20<=m<=50:
    print("Velocidade {:.0f}% acima do limite".format(int(m)))
    print("Penalidade: Multa de R$ 195,23.")
    print("Pontuação: 5 pontos na CNH.")
else:
    print("Velocidade {:.0f}% acima do limite".format(int(m)))
    print("Penalidade: Multa de R$ 880,41.")
    print("Pontuação: 7 pontos na CNH.")

time.sleep(5)

# Determina se um carro toma multa ou não

