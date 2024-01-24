vt = []

for i in range(10):
    numeros = float(input("digite os numeros inteiros: "))
    vt.append(numeros)
print("os numeros em ordem inversa:")

for i in range(9, -1, -1):
    print(vt[i])