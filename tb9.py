vtrA = []

for i in range(10):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    vtrA.append(numero)
soma = sum(num**2 for num in vtrA)
print("A soma dos quadrados dos elementos é:", soma)