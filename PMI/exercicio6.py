print("Qual o valor de X?")
x = float(input())
print("E o de Y?")
y = float(input())
copia = x
x = y
y = copia
print("Minha nossa, os valores foram trocados! Agora X = %s e Y = %s" % (x, y))
