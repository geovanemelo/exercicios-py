primeirotermo=int(input("Digite o primeiro termo da p.a: "))
razao=int(input("Digite a razão da p.a: "))
pm=primeirotermo
c=0
while c < 9:
    primeirotermo=primeirotermo+razao
    c=c+1
    if c == 1:
        print('{}'.format(pm),end='-> ')
    if c <= 8:
        print('{}'.format(primeirotermo),end='-> ')
    else:
        print('{}'.format(primeirotermo),end='. ')




