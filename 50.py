#ler 6 numero inteiros e somar os pares
s=0
t=0
co=0
for c in range (0,6):
    s=int(input("Entre com um numero: "))
    if s % 2 == 0:
        t=t+s
        co=co+1
print("Foram contabilizados {} numeros pares e a soma é {}".format(co,t))
