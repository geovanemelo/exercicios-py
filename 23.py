#Programa que analisa um numero e da sua casas

n=int(input('Digite o numero a ser analisado: '))
u=n // 1 % 10
d=n // 10 % 10
c=n // 100 % 10
m=n // 1000 % 10

print("O numero a ser analisado é {}".format(n))
print("Unidade: {}". format(u))
print("Dezena: {}". format(d))
print("Centena: {}". format(c))
print("Milhar: {}".format(m))