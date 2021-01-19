import datetime
print("Coloque 0 se quiser analisar o ano anual")
ano=int(input("Entre com o ano a ser analisado: "))

if ano==0:
    ano=datetime.date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("Ano de{} .Este ano é bissexto".format(ano))
else:
    print("Ano de {} .Este ano não é bissexto".format(ano))
