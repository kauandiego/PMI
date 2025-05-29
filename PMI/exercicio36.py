def fatorial(num):
    if num > 1:
        return num * fatorial(num - 1)
    else:
        return 1

numero = int(input("Digite algum numero "))

i= int(1)
print("A sequência fica:")
while i <= numero:
    if i > 1:
        print (1/(fatorial(i)), end=" ")
    else:
        print("1", end=" ")
    i = i + 1