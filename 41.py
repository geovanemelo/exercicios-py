#Programa que identifica a idade do usuario pelo ano de nascimento
#e informa a categoria dele na natação

Nascimento=int(input("Entre com o seu ano de nascimento: "))
Idade=(2019-Nascimento)

if Idade<=9:
    print('Sua categoria é Mirim')
elif Idade >9 and Idade <=14:
    print('Sua categoria é Infantil')
elif Idade > 14 and Idade <=19:
    print('Sua categoria é Junior')
elif Idade > 19 and Idade <= 20:
    print('Sua categoria é Senior')
else:
    print('Sua categoria é Master')