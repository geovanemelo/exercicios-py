Preço=float(input('Entre com o preço do produto: '))
FormaDePagamento=int(input('Escolha uma forma de pagamento\n[1]: A vista no dinheiro\n[2]: A vista no cartão\n[3]: Em até três vezes no cartão\n[4]: 3x ou mais no cartão: '))
if FormaDePagamento==1:
    print("Você terá 10% de desconto\nNovo preço:R${:.2f}".format(Preço*0.9))
elif FormaDePagamento==2:
    print("Voce terá 5% de desconto\nNovo preço: R${:.2f}".format(Preço*0.95))
elif FormaDePagamento==3:
    print("Você terá o preço de R${:.2f} mantido".format(Preço))
elif FormaDePagamento==4:
    print("Você terá 20% de juros\nNovo preço: R${:.2f}".format(Preço*1.20))
else:
    print("Forma de pagamento Invalida ")