print("Digite 2 números inteiros")
num1 = int(input())
num2 = int(input())

if num1 > num2:
    dif = num1 - num2
    print("A diferença entre os dois é de %s" % (dif))
elif num1 == num2:
    print("Não há diferença!")
else:
    dif = num2 - num1
    print("A diferença entre os dois é de %s" % (dif))