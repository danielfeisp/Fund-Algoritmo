v = int(input("Insira um numero bacanudo: "))



def encontra_valor(z: list, v: int) -> bool:
    for i in range( 0, len(z)):
        if z[i] == v:
            return True
    return False

encontra_valor(z, 11)