# Aprovar emprestimo para casa: pergunte o valor da casa
# Pergunte o salário mensal e em quantos anos ele vai pagar o emprestimo
# Mostre o valor das parcelas e se poderá ser efetuado o emprestimo
# Valores da parcela não podem passar de 30% do salario

ValorCasa=float(input("Por favor, entre com o valor total da casa: "))
Parcelamento=float(input("Em quantos anos haverá parcelamento do valor: "))
Salario=float(input("Informe seu salário mensal: "))
PrestaçãoMensal=ValorCasa/(Parcelamento*12)
TrintaSalario=Salario*0.30
if TrintaSalario>=PrestaçãoMensal:
    print("\033[32m*-\033[m"*80)
    print("\033[34mVocê está apto para o emprestimo!\033[m")
    print("O valor da suas parcelas mensais serão de: \033[31;mR${:.2f}\033[m".format(PrestaçãoMensal))
    print("\033[32m*-\033[m" * 80)
else:
    print("\033[35m--\033[m" * 80)
    print("\033[31mVocê não está apto para o emprestimo\033[m")
    print("O valor das prestações de {:.2f} são maiores que 30% de sua renda mensal de {:.2f}".format(PrestaçãoMensal,TrintaSalario))
    print("\033[35m--\033[m" * 80)
