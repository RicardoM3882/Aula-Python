num = []
for i in range(20):
    nume = int(input("digite os numeros inteiros: "))
    num.append(nume)

par = []
impar = []
for nume in num:
    if nume % 2 == 0:
        par.append(nume)
    else:
        impar.append(nume)


print("Números digitados:", num)
print("Números pares:", par)
print("Números ímpares:", impar)