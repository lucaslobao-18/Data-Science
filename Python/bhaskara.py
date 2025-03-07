from math import sqrt

delta = int(input("insira o valor de delta: "))
b = int(input("insira o valor de b:"))
a = int(input("insira o valor de a:"))
b=b*-1
raiz_dt = sqrt(delta)

x1 = (b+raiz_dt)/(2*a)
x2 = (b-raiz_dt)/(2*a)

print("o valor de x1 eh:",x1)
print("o valor de x2 eh:",x2)