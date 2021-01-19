listinha=list()
op=''
while True:
    listinha.append(int(input("Entre com algum valor: ")))
    op=str(input("Desejar continuar?[S/N]")).upper()
    if op in "NÃO":
        break
    else:
        continue
print(len(listinha))
print(sorted(listinha)[::-1])
if 5 in listinha:
    print('tem 5')
else:
    print('n tem 5')