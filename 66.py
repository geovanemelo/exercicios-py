n = s = c =0
while True:
    n=int(input("Digite um numero: "))
    if n == 999:
        break
    s=s+n
    c=c+1
print(f'a soma dos {c} valores foi {s}')
