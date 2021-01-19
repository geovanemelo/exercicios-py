from random import randrange
from time import sleep
num=0
c=0
escolha=str(input("Escolha par ou impar [I/P]")).strip()[0].lower()
while escolha in 'par' or escolha in 'impar':
    num=int(input("Escolha seu numero: "))
    print(f'Sua escolha foi {num}\nAgora é a vez do computador escolher...')
    sleep(2)
    print('--'*20)
    pcnum=randrange(0,11)
    print(f'A Escolha do computador foi {pcnum}')
    print('--' * 20)
    soma=pcnum+num
    print(f'A soma das mãos foram {soma}')
    print('--' * 20)
    if soma % 2 == 0:
        if escolha == 'p':
            print("Parabéns, você venceu!")
            c=c+1
            escolha = str(input("Escolha par ou impar [I/P]")).strip()[0].lower()
        elif escolha == 'i':
            print("Infelizmente você perdeu...")
            break
    else:
        if escolha == 'i':
            print ("Parabéns, você venceu!")
            c=c+1
            escolha = str(input("Escolha par ou impar [I/P]")).strip()[0].lower()
        elif escolha == 'p':
            print("Infelizmente você perdeu...")
            break
print(f'Você ganhou {c} seguidas!')
