med = []

for i in range(10):
    notas = []

    for j in range(4):
        nota = float(input(f'Digite a nota do {i+1}º aluno: '))
        notas.append(nota)
    media = sum(notas) / len(notas)
    med.append(media)
contador = 0

for media in med:
    if media >= 7.0:
        contador += 1
print("O número de alunos com média maior ou igual a 7.0 é:", contador)