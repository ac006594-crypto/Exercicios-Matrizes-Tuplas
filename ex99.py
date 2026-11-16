
matriz1 = []
matriz2 = []
resultado = []

print("Digite os valores da primeira matriz:")
for i in range(4):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
    matriz1.append(linha)

print("Digite os valores da segunda matriz:")
for i in range(4):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
    matriz2.append(linha)

for i in range(4):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    resultado.append(linha)

print("Resultado da soma:")

for linha in resultado:
    print(linha)
