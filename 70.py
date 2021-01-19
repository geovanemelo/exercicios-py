totaldec=0
valormaisbaixo=10000
compramaisbarata=''
acimadecem=0
while True:
    nomedoproduto=str(input("Qual o nome do produto comprado?"))
    valor=float(input("E Qual é o valor dele?"))
    totaldec=totaldec+valor
    if valor < valormaisbaixo:
        valormaisbaixo=valor
        compramaisbarata=nomedoproduto
    if valor > 100:
        acimadecem=acimadecem+1
    seguir=' '
    while seguir not in 'SN':
        seguir=str(input("Deseja seguir?[S/N]")).upper().strip()[0]
    if seguir == 'N':
        break
print('\n'*100)
print('-'*50)
print(f'O total gastado foi: {totaldec}\n')
print(f'{acimadecem} produtos custaram mais de R$100\n')
print(f'O produto mais barato foi {compramaisbarata}')
print('-'*50)
