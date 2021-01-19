#programa que lê duas notas, faz média e  diz se foi aprovado ou reprovado

n1=float(input("Entre com sua primeira nota: "))
n2=float(input("Entre com sua segunda nota: "))

Media=(n1+n2)/2

if Media < 5:
    print("Você foi reprovado!\nSua nota foi: {:.2f}".format(Media))
elif Media >= 5 and  Media<6:
    print("Você esta de recuperação\nSua nota foi: {:.2f}".format(Media))
else:
    print("Você foi aprovado!\nSua nota foi: {:.2f}".format(Media))
