import string
listagem=[]
listagemfake=['ronaldinho','22','ronaldao','33']
alfabeto=string.ascii_letters
conta=0
#criação da tupla com entrada de dados
while True:
    prod=input("Digite o nome do produto: ").capitalize()
    if prod=="X":
        break
    else:
        listagem.append(prod)
    preço=(input("Digite o preço do produto: "))
    listagem.append(preço)
listagem=tuple(listagem)
print(listagem)
print("*"*30)
print(f'{"LISTAGEM DE COMPRAS":^40}')
print("*"*30)
print(f'{"PRODUTO":<30}',end='')
print(f'{"PREÇO"}')
for c in listagem:
    if c[0] in alfabeto:
        print(f'{c:.<30}',end='')
    else:
        print(f'R${c:>3}')
        trans=int(c)
        conta=conta+trans
print(f'{"TOTAL":.<30}',end='')
print(f'RS{conta:>3}')

