def eh_cons(crt):
    cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return crt in cons


vtr = []
for i in range(10):
    crt = input("digite seus caracteres: ")
    vtr.append(crt)


total_cons = 0
cons_encontradas = []

for crt in vtr:
    if eh_cons(crt):
        total_cons += 1
        cons_encontradas.append(crt)

print("Total de consoantes lidas", total_cons)
print("Consoantes encontradas: ", end="")
for cons in cons_encontradas:
    print(cons, end=" ")
print()