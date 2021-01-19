import time
import random
print("O computador irá pensar em numero de 1 a 5, tente adivinhar!")
n=random.randrange(1,6)
n1=int(input("Chute um numero: "))
print("Processando...")
time.sleep(2)
if n==n1:
    print("Parabéns, você acertou!")
else:
    print("Você errou meu amigo. O numero pensado pelo computador foi: {}".format(n))


