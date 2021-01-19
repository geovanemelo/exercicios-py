from random import  randrange
randomnumero=(randrange(1,11))
numerohumano=int(input("O computador pensou em um numero de 0 a 10\nAchas que consegue adivinhar? Tente:"))
c=0
while numerohumano != randomnumero:
    if numerohumano>randomnumero:
        print("Você errou, o numero do computador é menor que {}".format(numerohumano))
        numerohumano=int(input("Tente outra vez: "))
        c=c+1
    elif numerohumano<randomnumero:
        print("Você errou, o numero do computador é maior que {}".format(numerohumano))
        numerohumano = int(input("Tente outra vez: "))
        c=c+1
print("Parabens, você acertou após {} tentativas".format(c))
