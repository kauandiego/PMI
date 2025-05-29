numero = int(input("Digite um número "))
i = int(1)
print("A tabuada desse número é: ")
while i <= 10:
    if i <10:
        print(numero * i, end=", ")
    else:
        print(numero * i)
    i = i + 1