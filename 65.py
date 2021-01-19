
media=0
c=0
somador=0
resp='S'
while resp in 'S':
    n=int(input("Digite um numero: "))
    c=c+1
    somador=somador+n
    media=somador/c
    resp=str(input("Desejar continuar? ")).upper().strip()[0]
print('a soma de todos o numeros foi {}'.format(somador))
print('e a media foi {}'.format(media))
