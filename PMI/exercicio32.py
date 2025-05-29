def fatorial(num):
    if num > 1:
        return num * fatorial(num - 1)
    else:
        return 1



numero = int(input("Digite um numero inteiro "))
fator = fatorial(numero)



print(fator)