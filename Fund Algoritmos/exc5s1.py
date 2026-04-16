import time

print("Organizador de números de forma decrescente altamente funcional")

x = int(input("Insira um numero aqui: "))
y = int(input("Insira outro numero aqui: "))
z = int(input("Insira outro numero aqui: "))

if x>=y and x>=z and y>=z:
    print("Esta é a ordem correta: %d,%d,%d" % (x,y,z))
elif x>=y and x>=z and z>=y:
    print("Esta é a ordem correta: %d,%d,%d" % (x,z,y))
elif y>=x and x>=z and y>=z:
    print("Esta é a ordem correta: %d,%d,%d" % (y,x,z))
elif y>=x and z>=x and y>=z:
    print("Esta é a ordem correta: %d,%d,%d" % (y,z,x))
elif x>=y and z>=x and z>=y:
    print("Esta é a ordem correta: %d,%d,%d" % (z,x,y))
else:
    print("Esta é a ordem correta: %d,%d,%d" % (z,y,x))

time.sleep(2)

# Organiza números de forma decrescente