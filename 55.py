menorpeso=0
maiorpeso=0
for p in range(1,6):
    peso=float(input("Entre com o peso da {}ª pessoa:".format(p)))
    if p == 1:
        maiorpeso=peso
        menorpeso=peso
    else:
        if peso > maiorpeso:
            maiorpeso=peso
        if peso < menorpeso:
            menorpeso=peso
print('o maior valor encontrado foi {} e o menor foi {}'.format(menorpeso,maiorpeso))