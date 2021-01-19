termos=int(input("Quantos termos você deseja mostrar?"))
pf=0
sf=1
tf=pf+sf
c=3
print ('{}-> {}'.format(pf,sf),end='-> ')
while c <= termos:
    tf=pf+sf
    print('{}'.format(tf),end='-> ')
    pf=sf
    sf=tf
    c=c+1
print("fim")

