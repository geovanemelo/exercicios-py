todosNumeros=[[],[]]
valor=0
for c in range(1,8):
    valor=int(input("Digite o {}º valor: ".format(c)))
    if valor % 2 == 0:
        todosNumeros[0].append(valor)
    else:
        todosNumeros[1].append(valor)
    print(todosNumeros)
print(f'Os numeros pares são: {sorted(todosNumeros[0])}')
print(f'Os numeros impares são: {sorted(todosNumeros[1])}')

