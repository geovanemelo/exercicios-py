#programa do alistamento

Ano=int(input("Entre com seu de nascimento: "))
AnoC=(2019-Ano)

if AnoC<18:
    AnoF=18-AnoC
    print("Você precisa se alistar daqui há {}".format(AnoF))
elif AnoC==18:
    print("Você precisa se alistar esse ano!")
else:
    anop=(AnoC-18)
    if anop==1:
        print("Você se alistou no ano passado!")
    else:
        print("Você já se alistou a {} anos atrás".format(anop))
