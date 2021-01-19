maisdezoito=0
homem=0
mulhermenos20=0
while True:
    idade=int(input("Quantos anos você tem? "))
    if idade > 18:
        maisdezoito=maisdezoito+1
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input("Digite o sexo [M/F]")).upper().strip()[0]
    if sexo == 'M':
        homem=homem+1
    if sexo == 'F' and idade < 20:
        mulhermenos20=mulhermenos20+1
    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar?[S/N]')).strip()[0].upper()
    if resp == 'N':
        break
print('\n' * 100)
print('-'*20)
print("FIM/ESTASTISICAS")
print('-'*20)
print(f'Foram contabilizados {homem} homens')
print(f'\n{maisdezoito} pessoas com mais de 18 anos')
print(f'\ne {mulhermenos20} mulheres com menos de 20 anos')
print('-'*20)




