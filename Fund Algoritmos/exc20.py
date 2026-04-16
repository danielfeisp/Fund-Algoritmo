lista = [(1, 'Roberto'), (10, 'Amanda'), (3, 'Fulano'), (10, 'Ciclano'),(6, 'Beltrano')]
def menor_numero (lista:list) -> float:
    maior = lista[0]
    for i in range(1,len(lista)):
        if maior < lista[i]:
            maior = lista[i]
    print("A melhor nota é: %d" % maior[0])
    print("O(A) melhor aluno(a) é: %s" % maior[1])
menor_numero(lista)