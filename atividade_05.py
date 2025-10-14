# Atividade 05 
# Faça um programa que receba dois números inteiros.
# Implemente as seguintes sub-ro9nas:
# 1. soma(int a , int b): retorna a soma de a com b
# 2. subtração(int a, int b): retorna a diferença entre a e b
# 3. mul;plicação(int a, int b): retorna a mul;plicação de a por b
# 4. potencia(int a, int b): retorna o valor de a elevado a b

# • Todas as sub-ro;nas devem usar somente as operações de soma e
# subtração. Na sub-ro;na potencia, u;lize a sub-ro;na mul;plicação
# criada anteriormente.

# • O programa deve apresentar uma tela na qual será solicitado para o
# usuário que entre com dois números, na sequência será solicitado ao
# usuário que escolha o ;po operação que deseja.

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b




def multiplicacao(a, b):
    resultado = 0
    negativo = False

   
    if b < 0:
        b = -b
        negativo = True

    for _ in range(b):
        resultado = soma(resultado, a)

    if negativo:
        resultado = -resultado

    return resultado

def potencia(a, b):
    if b == 0:
        return 1
    resultado = a
    for _ in range(1, b):
        resultado = multiplicacao(resultado, a)
    return resultado


# Programa principal
print(" Calculadora com Sub-Rotinas")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("\nEscolha a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Potência")

opcao = int(input("Opção: "))

if opcao == 1:
    print(f"Resultado da soma: {soma(a, b)}")
elif opcao == 2:
    print(f"Resultado da subtração: {subtracao(a, b)}")
elif opcao == 3:
    print(f"Resultado da multiplicação: {multiplicacao(a, b)}")
elif opcao == 4:
    print(f"Resultado da potência: {potencia(a, b)}")
else:
    print("Opção inválida!")