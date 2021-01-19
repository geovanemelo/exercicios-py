from random import randrange
matriz=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
soma1Coluna=0
soma3Linha=0
nPares=[]
for linha in range (0,4):
    for coluna in range (0,3):
        matriz[linha][coluna]=randrange(0,9)
for linha in range(0,4):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^10}]',end=' ')
    print()
#soma dos valores da primeira coluna
for linha in range(0,3):
   soma1Coluna=soma1Coluna+matriz[linha][0]
print(f'o valor da soma da primeira coluna é: {soma1Coluna}')
#soma dos valores da terceira linha
for coluna in range (0,3):
    soma3Linha=matriz [2][coluna]+soma3Linha
print(f'o valor da soma da terceira linha é {soma3Linha}')
#soma de todos os numeros impares
for linha in range(0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 != 0:
            nPares.append(matriz[linha][coluna])
print(f'Os numeros impares da lista matriz são: {sorted(nPares)}')