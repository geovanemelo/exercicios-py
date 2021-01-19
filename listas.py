# lista=[4,3,2,1]
# print(lista)
# #acrescentando valores no final da lista
# lista.append(0)
# print(lista)
# #acrescentando valores aonde quiser devido ao primeiro parametro da funçao
# lista.insert(0,5)
# print(lista)
# #removendo o valor pela chave dele
# lista.pop(0)
# print(lista)
# #removendo valor pelo seu 'nome'
# lista.remove(4)
# print(lista)
# #atribuiçao de valores a lista com list e range
# listacomvalores=list(range(5,11,2))
# print(listacomvalores)
# #ordenando valores
# valoresdesordenados=[4,1,7,7,33,99,44,32,0,5]
# print(sorted(valoresdesordenados))
# #saber quantos elementos tem na lista
# print(len(valoresdesordenados))'''
# '''num=[1,4,6,8,3,5,11,10,44,32,4]
# num.insert(0,2)
# print(num)
# print(f'essa lista contém {len(num)} elementos')
# print(f'essa lista contem {num.count(4)} elementos iguais a 4')
listinha=[]
for c2 in range(0,2):
    listinha.append(int(input("Digite valores: ")))
for c,v in enumerate(listinha):
    print(f'na posição {c} o valor é {v}...')