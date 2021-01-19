listinha=[]
adc=0
op=''
while True:
    adc=int(input("Adicione um valor para a lista: "))
    if adc in listinha:
        print('Valor já contido na lista')
    else:
        listinha.append(adc)
    op=input("Deseja continuar?[S/N]: ").upper()
    if op in 'NAO':
        break
print(f'você adicionou os valores {listinha}')
print(f'{sorted(listinha)} e assim são eles em ordem crescente')