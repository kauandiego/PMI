print("Digite um valor inteiro")
num1 = int(input())
print("Digite outro")
num2 = int(input())
multi = 0
i = 1
if num1 > num2:
    while multi < num1:
        multi = num2 * i
        i = i + 1
    if multi == num1:
            print("O número %s é múltiplo de %s" % (num1, num2))
    else:
            print("O número %s NÃO é múltiplo de %s" % (num1, num2))
                  
else:
    while multi < num2:
        multi = num1 * i
        i = i + 1
    if multi == num2:
            print("O número %s é múltiplo de %s" % (num2, num1))
    else:
            print("O número %s NÃO é múltiplo de %s" % (num2, num1))









