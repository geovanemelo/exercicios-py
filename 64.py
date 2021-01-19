n=0
s=0
c=0
n=int(input("Digite o valor inicial: "))
while n != 999:
    s=s+n
    c=c+1
    n=int(input("Digite o valor para continuar a soma: "))
print('O valor total somado foi: {}\nForam digitados: {} numeros'.format(s,c))

