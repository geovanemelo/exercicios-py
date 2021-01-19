n1=int(input("Entre com o primeiro numero: "))
n2=int(input("Entre com o segundo numero: "))
n3=int(input("Entre com o terceiro numero: "))
lista=[n1,n2,n3]

lista=(sorted(lista))

print("O menor numero é {}".format(lista[0]))
print("O maior numero é {}". format(lista[2]))


