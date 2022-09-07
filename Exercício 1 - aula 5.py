primeira = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
segunda = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
k = int(input(f'\nDigite uma constante para multiplicar a diagonal da matriz: \n'))

def imprimir(matriz):
    for i in range(0, 3):
        print(f"{matriz[i]}")

#ESSA PARTE TÁ ZERANDO AS MATRIZES
for i in range(0, 3):
    for j in range(0, 3):
        primeira[i][j] = int(input(f"Digite um valor para a matriz: \n"))
        if(i==j):
            primeira[i][j] = segunda[i][j] * k
        else:
            primeira[i][j] = segunda[i][j]

print()
imprimir(primeira)
imprimir(segunda)