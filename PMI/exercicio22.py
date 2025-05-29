print("Digite um valor inteiro")
num1 = int(input())
print("Digite outro")
num2 = int(input())

if num1 > num2:
    print("Os valores ordenados na ordem crescente ficam assim: %s, %s" % (num2, num1))
else:
    print("Os valores ordenados na ordem crescente ficam assim: %s, %s" % (num1, num2))