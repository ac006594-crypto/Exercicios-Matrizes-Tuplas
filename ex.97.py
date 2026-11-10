matriz = []
posicoes = ["a", "b"], ["c", "d"]

for i in range(2):
    linha = []
    for j in range(2):
        letra = posicoes[i][j]
        valor = float(input(f"Digite o elemento [{letra}]: "))
        linha.append(valor)
    matriz.append(linha)

determinante = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
print()


print(" Matriz M:")
print(f" | {matriz[0][0]:>4.1f}  {matriz[0][1]:>4.1f} |")
print(f" | {matriz[1][0]:>4.1f}  {matriz[1][1]:>4.1f} |")


if determinante.is_integer():
    print(f"\nResult: det(M) = {int(determinante)}")
else:
    print(f"\nResult: det(M) = {determinante:.2f}")
