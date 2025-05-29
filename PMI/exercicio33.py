numero = int(input("Digite algum numero "))

i= int(1)
print("A sequência fica:")
while i <= numero:
    if i > 1:
        print (1/i, end=" ")
    else:
        print("1", end=" ")
    i = i + 1