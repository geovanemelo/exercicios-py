#Algoritmo que lê um numero, transforma para radiando e exibe o valor do seno,cosseno e tangente


import math
angulo=int(input("Digite o angulo a ser calculado: "))
seno=math.sin(math.radians(angulo))
print("O Seno do angulo {} é igual a: {:.2f}".format(angulo,seno))
coseno=math.cos(math.radians(angulo))
print("O Coseno do angulo {} é igual a: {:.2f}".format(angulo,coseno))
tang=math.tan(math.radians(angulo))
print("A tangente do angulo {} é igual a: {:.2f}".format(angulo,tang))