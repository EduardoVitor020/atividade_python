# Atividade 02
# 2 - Faça um programa que:
# 2.1 - Receba do usuário 10 números inteiros e coloque em uma estrutura de dados.
# 2.3 - Na sequência solicite ao usuário que informe um novo número inteiro, e verifique se este número encontra-se
# registrado.
# 2.4 - Caso positivo, imprima a(s) posição(ões) em que este número estiver na estrutura. 
# Caso contrário, exiba uma mensagem avisando ao usuário informando que o número não se encontra na estrutura.

# Parte 2.1 - Receber 10 números inteiros
numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Parte 2.3 - Solicitar novo número e verificar se existe
numero_busca = int(input("\nDigite um número para buscar: "))

# Parte 2.4 - Verificar posições
posicoes = [i for i, num in enumerate(numeros) if num == numero_busca]

if posicoes:
    print(f"\nO número {numero_busca} foi encontrado nas posições: {posicoes}")
else:
    print(f"\nO número {numero_busca} **não foi encontrado** na estrutura.")
