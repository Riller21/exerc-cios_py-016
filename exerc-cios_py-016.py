# Número de alunos
num_alunos = 30

# Listas para armazenar idades e alturas
idades = []
alturas = []

# Preencher as listas com dados fornecidos pelo usuário
for i in range(num_alunos):
    idade = int(input(f"Insira a idade do aluno {i + 1}: "))
    altura = float(input(f"Insira a altura do aluno {i + 1} em metros: "))
    idades.append(idade)
    alturas.append(altura)

# Calculando a média de altura
media_altura = sum(alturas) / num_alunos

# Contando alunos com mais de 13 anos e altura inferior à média
alunos_contados = 0
for i in range(num_alunos):
    if idades[i] > 13 and alturas[i] < media_altura:
        alunos_contados += 1


print(f"Quantidade de alunos com mais de 13 anos e altura inferior à média: {alunos_contados}")