listinha=[]
for c in (range (1,6)):
    listinha.append(int(input(f"Digite o {c}º valor da lista: ")))
print(max(listinha))
print(f'O maior valor da lista é {max(listinha)}',end=' ')
print(f'na posição {listinha.index(max(listinha))+1}')
print(f'O menor valor da lista é {min(listinha)}',end=' ')
print(f'na posição {listinha.index(min(listinha))+1}')