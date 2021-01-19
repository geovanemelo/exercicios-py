numeros=("Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez")
n=12
op=0
while True:
    n=int(input("Digite o valor desejado entre 0 a 10: "))
    while n > 10 or n < 0:
        n = int(input("Digite o valor desejado entre 0 a 10: "))
    for c in numeros:
        print(f'Você digitou o numero : {numeros[n]}')
        break
    op=int(input("Digite [1] para continuar e [2] para sair: "))
    while op != 1 and op != 2:
        op = int(input("Digite [1] para continuar e [2] para sair: "))
    if op == 2:
        break







