n=0
c=0
s=0
while c < 11:
    if c == 0:
        n=int(input("Quer ver a tabuada de qual numero? "))
        c=c+1
        if n < 0:
            break
    else:
        s=n*c
        print(f'{n} x {c} = {s}')
        c=c+1
    if c == 11:
        c=0



