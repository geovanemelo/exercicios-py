#aumentar o salario do funcionario em 15% para quem recebe até 1.250.00
#aumentar em 10% quem recebe mais que 1.250.00

salario=float(input("Entre com o salário do trabalhador: "))
if salario<=1250:
    aumento = (salario*15)/100
    salarioA=salario+aumento
    print("O salário de {} foi aumentado para {}".format(salario,salarioA))
else:
    aumento = (salario * 10) / 100
    salarioA = salario + aumento
    print("O salário de {} foi aumentado para {}".format(salario, salarioA))

print("Obrigado, aproveite os seus {} a mais :)!".format(aumento))