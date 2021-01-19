from time import sleep
boletim=[]
aluno=[]
notas=[]
op=''
indiv=0
while True:
    aluno.append(input("Digite o nome do aluno: "))
    notas.append(int(input("Digite a 1ª nota: ")))
    notas.append(int(input("Digite a 2ª nota: ")))
    aluno.append(notas[:])
    boletim.append(aluno[:])
    aluno.clear()
    notas.clear()
    op=input("Deseja continuar?[S/N]: ").capitalize()
    if op == 'N':
        break
    else:
        continue
print('*'*30)
print(f'Boletim')
print('*'*30)
#print(boletim)
print(f'Num.',end=' '*5)
print(f'ALUNO',end=' '*5)
print(f'MEDIA',end=' '*5)
print()
for i,a in enumerate(boletim):
    print(f'{i:^5}{a[0]:^10}    {sum(a[1])/len((a[1]))}')
print('*'*30)
sleep(1)
while True:
    indiv=int(input("Digite o numero do aluno desejado: "))
    if indiv != 999:
        for i,a in enumerate (boletim):
            if indiv==i:
                print(f'Aluno {a[0]}:')
                print(f'Primeira nota -> {a[1][0]}')
                print(f'Segunda nota -> {a[1][1]}')
                print(f'Media -> {sum(a[1])/len((a[1]))}')
                print('*'*30)
                break
                sleep(1)
            # elif indiv !=i:
            #     print('Aluno não encontrado')
            #     print('*'*30)
            #     sleep(1)
    else:
        break
print('fim')




