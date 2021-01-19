from random import randrange
valoresPares=0
matriz=[[0,0,0],[0,0,0],[0,0,0]]
somaColuna3=0
for x in range(0,3):
    for y in range (0,3):
        matriz[x][y]=randrange(1,6)
print('Essa é a matriz: ')
for x in range (0,3):
    for y in range (0,3):
        print(f'[{matriz[x][y]:^5}]',end=' ')
    print()
for c in matriz[x]:
    for c in matriz[y]:
        if c % 2 ==0:
            valoresPares=valoresPares+c
print(f'A soma dos valore pares é: {valoresPares}')
for x in range(0,3):
    somaColuna3=somaColuna3+matriz[x][2]
print(f'A soma da coluna 3 é: {somaColuna3}')

for y in range (0,3):
    if y == 0:
        maiorElemento=matriz[1][y]
    elif matriz [1][y] > maiorElemento:
        maiorElemento=matriz[1][y]
print(f'O maior elemento da segunda linha é {maiorElemento}')

