#soma de todos os numeros impares que são multiplos de tres entre
# o intervalo de 1 a 500
s=0
for c in range(1,501,2):
  if c%3==0:
      s=s+c
print(s)


