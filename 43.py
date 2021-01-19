#calculo de indice de massa corporea

Peso=float(input("Entre com seu peso (em kg): " ))
Altura=float(input("Entre com sua altura (em metros): " ))
Imc=Peso/(Altura**2)

if Imc < 18.5:
    print("Seu imc é {:.2f} e você está abaixo do peso".format(Imc))
elif Imc >= 18.5 and Imc < 25:
    print("seu imc é {:.2f} e você está no peso ideal".format(Imc))
elif Imc >= 25 and Imc < 30:
    print("seu imc é {:.2f} e você está com sobrepeso".format(Imc))
elif Imc >= 30 and Imc < 35:
    print("seu imc é {:.2f} e você está com obesidade grau 1".format(Imc))
elif Imc >= 35 and Imc <40:
    print("seu imc é {:.2f} e você está com obesidade grau 2".format(Imc))
else:
    print("seu imc é {:.2f} e você está com obesidade grau 3".format(Imc))
