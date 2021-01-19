#Programa que leia uma frase e diga quantas vezes aparece A
#onde apareceu primeiro e por ultimo

frase=str(input("Digite a frase a ser Analisada:")).lower().strip()

aparecimentoA=frase.count('a')

primeiravezA=frase.find('a')

ultimavezA=frase.rfind('a')

print(aparecimentoA)
print(primeiravezA)
print(ultimavezA)