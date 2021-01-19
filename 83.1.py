expressao=str(input("Digite sua expressao: "))
pilha=list()

for simb in expressao:
    if simb == "(":
        pilha.append(simb)
    elif simb == ")":
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print("Expressão valida!")
else:
    print("Erro na expressão")