from random import randint
from time import sleep
num=0
jogos=[]
lista=[]
contador=0
print('*'*30)
print('        JOGO DA MEGA')
print('*'*30)
quant=int(input("Quantos jogos você quer que eu sorteie?"))
tot=1
while tot <= quant:
    contador=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            contador=contador+1
        if contador >=6 :
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*3,f'Sorteando {quant} jogos','-='*3)
for i,l in enumerate (jogos):
    print(f'Jogo {i+1} :{l}')
    sleep(1.5)
print("Boa sorte!")