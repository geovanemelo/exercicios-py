c=1
t=[]
#lendo os 5 valores pelo teclado
while c < 6:
    n=int(input("Digite o valor"))
    t.append(n)
    c=c+1
#convertendo a lista para uma tupla
t=tuple(t)
print(t)
#contando quantas vezes aparece o 9
print(f"o valor 9 apareceu {t.count(9)}")
if 3 in t:
    print(f"o valor 3 apareceu na posição: {t.index(3)}")
else:
    print('o valor 3 não contém na lista')
print('os valores pares foram: ',end='')
for c in t:
    if c%2==0:
        print(c,end=' ')

