from time import sleep
n1=int(input("Digite um primeiro numero: "))
n2=int(input("Digite um segundo numero: "))
menu=int(input("---MENU---\nO que você deseja fazer com esses numeros?\n[1]Somar\n[2]Multiplicar\n[3]Maior numero entre os dois\n[4]Digitar novos numeros\n[5]Sair do programa"))
while menu != 5:
    if menu==1:
        soma=n1+n2
        print("o resultado da soma entre {} e {} é: {}".format(n1,n2,soma))
        sleep(3)
        menu=int(input("E agora, o que você deseja fazer com esses numeros?\n[1]Somar\n[2]Multiplicar\n[3]Maior numero entre os dois\n[4]Digitar novos numeros\n[5]Sair"))
    elif menu==2:
        mult=n1*n2
        print("O resultado da multiplicação entre {} e {} é: {}".format(n1,n2,mult))
        sleep(3)
        menu=int(input("E agora, o que você deseja fazer com esses numeros?\n[1]Somar\n[2]Multiplicar\n[3]Maior numero entre os dois\n[4]Digitar novos numeros\n[5]Sair"))
    elif menu==3:
        if n1>n2:
            print("O numero {} é maior que o numero {}".format(n1,n2))
        elif n2>n1:
            print("O numero {} é maior que o numero {}".format(n2,n1))
        elif n1==n2:
            print("Os numeros {} e {} tem o mesmo valor".format(n1,n2))
        sleep(3)
        menu=int(input("E agora, o que você deseja fazer com esses numeros?4\n[1]Somar\n[2]Multiplicar\n[3]Maior numero entre os dois\n[4]Digitar novos numeros\n[5]Sair"))
    elif menu==4:
        n1=int(input('Entre com um novo valor para o primeiro numero: '))
        n2=int(input('Entre com um novo valor para o segundo numero: '))
        sleep(3)
        menu = int(input("E agora, o que você deseja fazer com esses numeros?4\n[1]Somar\n[2]Multiplicar\n[3]Maior numero entre os dois\n[4]Digitar novos numeros\n[5]Sair"))
    elif menu>5:
        print("Opção invalida, retornando ao menu..")
        sleep(3)
        menu = int(input("---MENU---\nO que você deseja fazer com esses numeros?\n[1]Somar\n[2]Multiplicar\n[3]Maior numero entre os dois\n[4]Digitar novos numeros\n[5]Sair do programa"))
print("Obrigado por usar nosso programa!")
sleep(1)