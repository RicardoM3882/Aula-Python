vtr = []

for i in range(5):
    num = int(input("Digite o número inteiro: "))
    vtr.append(num)
soma = sum(vtr)
mult = 1

for num in vtr:
    mult *= num
print("Números digitados:", vtr)
print("Soma dos números:", soma)
print("Multiplicação dos números:", mult)