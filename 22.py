##Programa que lê o nome da algumas informaçoes sobre


nome='Geovane Melo Da Silva'

print("Nome com todas letras maiusculas: {}".format(nome.upper()))
print("Nome com todas letras minusculas: {}".format(nome.lower()))
NomeInteiro=len(nome)
QuantidadeDeEspaços=nome.count(' ')
NomeSemEspaço=NomeInteiro-QuantidadeDeEspaços
print("Quantidade de letras sem espaço no nome: {}".format(NomeSemEspaço))
print("Quantidade de letras no primeiro nome: {}".format(len(nome.split()[0])))
