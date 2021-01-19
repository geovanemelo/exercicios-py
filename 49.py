#tabuado usando laço for

num=int(input("Digite o numero desejado: "))
r=0
for c in range(0,11):
    r=num*c
    print("{} x {} = {}".format(num,c,r))