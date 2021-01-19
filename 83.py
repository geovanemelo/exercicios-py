listinha=[]
listinharpar=[]
listinhaimpar=[]
num=0
while True:
    num=int(input("Digite um valor a ser adicionado(0=stop:) "))
    if num==0:
        break
    else:
        listinha.append(num)
for c in listinha:
    if c % 2 == 0:
        listinharpar.append(c)
    else:
        listinhaimpar.append(c)
print('\n'*100)
print('-'*20)
print('Numeros pares:\n')
print(f'Numeros: {listinharpar}\nQuantidade: {len(listinharpar)}\n')
print(f'Maior: {max(listinharpar)}\nMenor:{min(listinharpar)}')
print('-'*20)
print('Numeros impares:\n')
print(f'Numeros: {listinhaimpar}\nQuantidade: {len(listinhaimpar)}\n')
print(f'Maior: {max(listinhaimpar)}\nMenor:{min(listinhaimpar)}')

