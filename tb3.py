nots = []

for i in range(4):
    nt = float(input("digite as notas: "))
    nots.append(nt)
print("Suas notas:")

for nt in nots:
    print(nt)
media = sum(nots) / len(nots)
print("Sua média:", media)