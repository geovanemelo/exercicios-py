listinha=[0]
for c in range (1,6):
    adc=int(input("Digite um valor a ser adc: "))
    for c in listinha:
        if adc > c:
            listinha.insert(listinha.index(c),adc)
            listinha.pop()
            print(listinha[::-1])
            listinha.append(0)
            break




