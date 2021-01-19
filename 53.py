frase=str(input('Digite a frase a ser analisada: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso=inverso+junto[letra]
if junto==inverso:
    print("É Um palindromo")
else:
    print("nao é palindro")