vtr1 = []

vtr2 = []

for i in range(10):
    elemento1 = int(input("digite o elemento do 1 vetor: "))
    vtr1.append(elemento1)
    elemento2 = int(input("digite o elemento do 2 vetor: "))
    vtr2.append(elemento2)

vtr3 = []

for i in range(10):
    vtr3.append(vtr1[i])
    vtr3.append(vtr2[i])
print("Terceiro vetor com os elementos intercalados:")
print(vtr3)