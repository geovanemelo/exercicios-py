#Ler nome de uma pessoa e ver se tem 'silva no nome'

nome=str(input("Digite o seu nome inteiro: ")).lower().strip().split()

print('silva'in nome[0:])

