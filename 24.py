# lê um nome de cidade e retorna se ela começa com "santo" ou não no primeiro nome

cidade=str(input("Digite o nome da cidade a ser analisada: "))

cidadesplitada=cidade.lower().split()

print("santo" in cidadesplitada [0])