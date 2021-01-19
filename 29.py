Vcarro=int(input("Em qual velocidade o carro estava?  "))
if Vcarro<=80:
    print("Velocidade dentro da lei, sem multa!")
    exit()
else:
    print("Velocidade acima do limite")
multa=(Vcarro-80)*7
print("A sua multa é de: R${} reais".format(multa))
