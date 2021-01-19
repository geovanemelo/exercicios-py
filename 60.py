#Calculo de fatorial(com while)

num=int(input("Digite o numero desejado: "))
inic=1
fatr=1
while inic <= num:
    fatr=fatr*inic
    inic=inic+1
print(fatr)