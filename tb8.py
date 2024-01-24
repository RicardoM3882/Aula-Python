ida = []

alt = []

for i in range(5):

    idade = int(input("digite a idade: "))
    altura = float(input("qual a altura: "))
    ida.append(idade)
    alt.append(altura)
print("Idades na ordem inversa:")

for idade in reversed(ida):
    print(idade)
print("Alturas na ordem inversa:")

for altura in reversed(alt):
    print(altura)