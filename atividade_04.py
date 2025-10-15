# Solicita os 6 números sorteados
sorteados = []
for i in range(6):
    num = int(input(f"Digite o {i+1}º número sorteado: "))
    sorteados.append(num)

# Solicita os 6 números do cartão do usuário
cartao = []
for i in range(6):
    num = int(input(f"Digite o {i+1}º número do seu cartão: "))
    cartao.append(num)

# Conta quantos números o usuário acertou
pontos = 0
for num in cartao:
    if num in sorteados:
        pontos += 1

print(f"Você fez {pontos} ponto(s)!")