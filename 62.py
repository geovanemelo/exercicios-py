primeirotermo=int(input("Digite o primeiro termo da p.a: "))
razao=int(input("Digite a razão da p.a: "))
pm=primeirotermo
c=0
cc=0
ultimotermo=0
while c < 9:
    primeirotermo=primeirotermo+razao
    c=c+1
    if c == 1:
        print('{}'.format(pm),end='-> ')
    if c <= 8:
        print('{}'.format(primeirotermo),end='-> ')
    else:
        print('{}'.format(primeirotermo),end='. ')
        ultimotermo=primeirotermo
maistermos=int(input("\nDigite quantos termos a mais você quer: "))
maistermosmenos1=maistermos-1
if maistermos !=0:
    while cc < maistermos:
        if cc != maistermosmenos1:
            ultimotermo=ultimotermo+razao
            print('{}'.format(ultimotermo),end='-> ')
            cc=cc+1
        else:
            ultimotermo = ultimotermo + razao
            print('{}'.format(ultimotermo), end=' ')
            cc = cc + 1
        if cc == maistermos:
            maistermos=int(input("\nQuantos termos a mais: "))
            maistermosmenos1=maistermos-1
            cc=0

