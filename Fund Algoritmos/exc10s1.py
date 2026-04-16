import time

Maior = 0

for algo in range (0,6):
    n=int(input("Bota uns número ae: "))
    if Maior<n:
        Maior=n
print("Esse número é o Maior: %d" %Maior )

time.sleep(3)

#Computador identifica o maior número entre 6 números