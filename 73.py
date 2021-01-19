Tabela=('Flamengo','Santos','Palmeiras','São Paulo', 'Corinthias', 'Atletico-MG','Grêmio','Ceará','Fluminense','Chapecoense','CSA','Bahia','Fortaleza','Avai','Vasco','Cruzeiro')

for cont in range(0,len(Tabela[0:5])):
    if cont == 0:
        print(("Os primeiros colocados do BR são: "))
    print(f'{cont+1}ª -> {Tabela[cont]}')
print('--'*89)
for pos, cont2 in enumerate(Tabela):
    if pos == 0:
        print("Os ultimos colocados são: ")
    if pos > 11:
        print(f'{pos}ª- > {cont2}')
print('--'*89)
print("Todos times participantes são: ") 
for cont3 in sorted(Tabela):
    print (cont3)
print('--'*89)
for pos, cont4 in enumerate(Tabela):
    if cont4 == "Chapecoense":
        print(f'A {cont4} se encontra na {pos}ª posição do campeonato')






