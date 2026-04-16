lista = [98 , 2 , 3 , 4, 5, 6, 7, 8, 9, 3.5, 3.4, 6.4]

menor = lista[0]
menor_indice = 0
for i in range(1,len(lista)):
    if menor > lista[i]:
        menor = lista[i]
        menor_indice = i



def lista_crescente (lista:list) -> int:
    for z in range(0,len(lista)):
        j = (lista[menor_indice:])
        troca_elementos(lista, z, j)
        z = z + 1


def troca_elementos(lista: list, i:int, j: int) -> None:
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

print(lista_crescente(lista))