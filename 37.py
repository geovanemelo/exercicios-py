#converter um numero decimal para binario,octal ou hexa. escolha do usuario

num=int(input("Escreva o numero a ser trabalhado: "))
print("-*"*80)
r=int(input("Escreva [1]: Para converter para binário\nEscreva [8]: Para converter para octal\nEscreva [16]: Para converter para hexadecimal\nSua opção: "))
print("-*"*80)
if r == 1:
    print("O numero {} convertido para binário é {}". format(num,bin(num)[2:]))
elif r == 8:
    print("o numero {} convertido para octal é {}". format(num,oct(num)[2:]))
elif r == 16:
    print("O numero {} convertido para hexadecimal é {}". format(num,hex(num)[2:]))
else:
    print("Opção invalida")