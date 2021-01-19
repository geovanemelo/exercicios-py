t1=float(input("Entrê com o primeiro segmento do triangulo: "))
t2=float(input("Entrê com o segundo segmento do triangulo: "))
t3=float(input("Entrê com o terceiro segmento do triangulo: "))

if t1<(t2+t3) and t2<(t1+t3) and t3<(t1+t3):
    print("Com esses segmentos é possivel fazer um triangulo!")
    if t1==t2 and t1==t3 and t2==t3:
        print("Este é um triangulo equilatero")
    elif (t1==t2) or (t1==t3) or (t2==t3):
        print('Esté é um triangulo Isósceles')
    else:
        print('Este triangulo é escaleno')
else:
    print("Com estes segmentos não é possivel fazer um triangulo")