somaidade=0
mediaidade=0
maioridadehomem=0
nomemaisvelho=''
contmm20=0
for p in range(1,5):
    print('---- {}ª pessoa ----'.format(p))
    nome=str(input("Entre com o nome da {}ª pessoa: ".format(p))).strip()
    idade=int(input("Idade: "))
    sexo=str(input("[M/F]: ")).strip().upper()
    somaidade=somaidade+idade
    if p==1 and sexo=='M':
        maioridadehomem=idade
        nomemaisvelho=nome
    if sexo=='M'and idade > maioridadehomem:
        maioridadehomem=idade
        nomemaisvelho=nome
    if sexo == "F" and idade < 20:
        contmm20=contmm20+1
    if nomemaisvelho=='':
        nomemaisvelho=str("nao tem homem")

mediaidade=somaidade/p
print("a idade média das pessoas é de {}".format(mediaidade))
print("o homem mais velho é o {}".format(nomemaisvelho))
print("a quantidade mulheres com -20 anos é {}".format(contmm20))