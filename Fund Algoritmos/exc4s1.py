import time

x = float(input("Digite o código de origem do produto: "))

if x==1:
    print("Carne Bovina R$69,90/kg, vindo do Sul")
elif x==2:
    print("Castanhas do Pará R$57,99/kg, vindo do Norte")
elif x==3:
    print("Camarão, R$79,99/kg, vindo da Leste")
elif x==4:
    print("Caixa de Ovo com 12u, R$15,00, vindo do Oeste")
elif x==5 or x==6:
    print("Carne Seca para escondidinho, R$39,99, vindo do Nordeste")
elif x==7 or x==8 or x==9:
    print("Laranja da Turma da Mônica 18u, R$12,99, vindo do Sudeste")
elif 10<=x<=20:
    print("Leite de Soja, R$5,99, vindo do Centro-Oeste")
elif 25<=x<=30:
    print("Cajá, R$6,99/kg, vindo do Nordeste")

time.sleep(2)