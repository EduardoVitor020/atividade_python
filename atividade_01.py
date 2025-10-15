# Atividade 01
# 1 - Faça um programa que:
# 1.1 - Receba o nome e a nota de 10 alunos e guarde em uma estrutura de dados.
# 1.2 - Calcule a média das notas recebidas.
# 1.3 - Imprima a média das notas.
# 1.4 - Imprima a maior e a menor nota, bem como quais os alunos que obtiveram essas notas.
# 1.5 - Imprima uma listagem contendo o nome e nota dos alunos, que obtiveram notas abaixo da média.
# 1.6 - Imprima uma listagem contendo os nomes e notas dos alunos, que obtiveram notas maiores ou iguais à média.

# Parte 1.1 - Receber nome e nota de 10 alunos
alunos = []

for i in range(10):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append({'nome': nome, 'nota': nota})

# Parte 1.2 e 1.3 - Calcular e imprimir a média das notas
soma_notas = sum(aluno['nota'] for aluno in alunos)
media = soma_notas / len(alunos)
print(f"\nMédia da turma: {media:.2f}")

# Parte 1.4 - Maior e menor nota + alunos correspondentes
notas = [aluno['nota'] for aluno in alunos]
maior_nota = max(notas)
menor_nota = min(notas)

print(f"\nMaior nota: {maior_nota:.2f}")
for aluno in alunos:
    if aluno['nota'] == maior_nota:
        print(f"Aluno com maior nota: {aluno['nome']}")

print(f"\nMenor nota: {menor_nota:.2f}")
for aluno in alunos:
    if aluno['nota'] == menor_nota:
        print(f"Aluno com menor nota: {aluno['nome']}")

# Parte 1.5 - Alunos com notas abaixo da média
print("\nAlunos com notas abaixo da média:")
for aluno in alunos:
    if aluno['nota'] < media:
        print(f"{aluno['nome']} - Nota: {aluno['nota']:.2f}")

# Parte 1.6 - Alunos com notas acima ou iguais à média
print("\nAlunos com notas iguais ou acima da média:")
for aluno in alunos:
    if aluno['nota'] >= media:
        print(f"{aluno['nome']} - Nota: {aluno['nota']:.2f}")
