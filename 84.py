pessoa=[]
nome=''
peso=0
contador=0
op=''
cadastro=[]
while True:
   nome=input("Digite o seu nome: ")
   pessoa.append(nome)
   peso=int(input("Digite o seu peso: "))
   pessoa.append(peso)
   cadastro.append(pessoa[:])
   #print(cadastro)
   pessoa.clear()
   contador=contador+1
   op=input("Deseja continuar?[S/N]").upper()
   if op =='N':
       break
   else:
       continue
print(f'Total de pessoas cadastradas: {contador}')
print('As pessoas acima do peso são: ')
for c in cadastro:
    if c[1]>80:
        print(f'{c[0]} com {c[1]}KG')
print('As pessoas abaixo do peso são: ')
for c2 in cadastro:
    if c2[1]<60:
        print(f'{c2[0]} com {c2[1]}KG')






