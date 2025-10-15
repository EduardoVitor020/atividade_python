numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1} número inteiro: "))
    numeros.append(numero)

for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print("\nLista com valores negativos substituídos por 0:")
print(numeros)
