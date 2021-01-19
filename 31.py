#Faça um programa que pergunte a distância e determine
#o preço da passagem. Sendo R$ 0,50 até 200 km
#e R$ 0,45 para viagens mais longas

kmViagem=int(input("Entre com o valor em km da distancia da viagem: "))
if kmViagem <= 200:
    preço=kmViagem*0.50
    print("A sua viagem tera o preço de: R${} reais".format(preço))
else:
    preço=kmViagem*0.45
    print("A sua viagem tera o preço de: R${} reais".format(preço))
print("\n\n\nOBrigado!")