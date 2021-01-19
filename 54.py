from datetime import date
data=date.today()
anoat=data.year
contmenor=0
contmaior=0
for c in range(0,7,1):
    anodenasc=int(input("Entre com sua data de nascimento: "))
    if (anoat-anodenasc)<18:
        contmenor=contmenor+1
    else:
        contmaior=contmaior+1
print("A quantidade de menores de idade é {}. E de maior de idaade é {}".format(contmenor,contmaior))
