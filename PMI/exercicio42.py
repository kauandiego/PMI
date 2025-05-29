copia= int(1)
copia2 = int(1)
i= int(1)
print("A sequência fica:")
while i <= 50:
    if i > 1:
        copia2 = copia
        copia = i
        cu = int(i+copia2)
        print( i / (i+copia2), end=" ")
        print(" %s/%s)" % (i,cu))
    else:
        print("1", end=" ")
    i = i + 1