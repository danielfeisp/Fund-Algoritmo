lista = [98 , 2 , 3 , 4, 5, 6, 7, 8, 9, 3.5, 3.4, 6.4]

def menor_numero (lista:list) -> float:
    menor = lista[0]
    for i in range(1,len(lista)):
        if menor > lista[i]:
            menor = lista[i]
    return menor
print(menor_numero(lista))        