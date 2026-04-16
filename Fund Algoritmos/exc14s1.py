import time

def data_magica(dia, mês, ano):
    ano2 = ano
    while ano2 > 100:
        ano2 = ano2-100
    if dia*mês == ano2:
        print("%d/%d/%d" % (dia,mês,ano))

for ano in range (1901,2027):
    for mês in range (1,13):
        for dia in range (1,32):
                data_magica(dia,mês,ano)

time.sleep(20)