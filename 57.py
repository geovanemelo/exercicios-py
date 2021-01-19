s=str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while s not in 'MF':
    s=str(input("dados invalidos. Insira corretamente seu sexo[M/F]: ")).strip().upper()[0]
if s=='M':
    s='Masculino'
elif s=="F":
    s="Feminino"
print("SEXO {} registrado".format(s))
