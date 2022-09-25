#Dimensões das matrizes

lA = int(input('\nNúmero de linhas da matriz A: '))
cA = int(input('Número de colunas da matriz A: '))
lB = int(input('Número de linhas da matriz B: '))
cB = int(input('Número de colunas da matriz B: '))

#Agora vamos testar se há a possibilidade de multiplicação

if (cA != lB):
    print('Não é possível efetuar a multiplicação entre as duas matrizes porque o número de colunas da primeira é diferente do número de linhas da segunda!')
    exit()

#Digitação da matriz A

matrizA = []
for i in range(lA):
    linha = []
    for j in range(cA):
        linha.append(int(input('Digite o valor de ['+ str(i) +','+ str(j) +'] da matriz A: ')))
        matrizA.append(linha)
print('\nPrimeiro print da matrizA:\n')
print(matrizA)
print()

#Digitação da matriz B

matrizB = []
for i in range(lB):
    linha = []
    for j in range(cB):
        linha.append(int(input('Digite o valor de ['+ str(i) +','+ str(j) +'] da matriz B: ')))
        matrizB.append(linha)
print('\nPrimeiro print da matriz B:\n')
print(matrizB)
print()


matrizR = []

#gera matriz resultante:

for i in range(lA):
    linha = []
    for j in range(cB):
        valorR = 0
        for k in range(cA):
            valorR = valorR + matrizA[i][k]*matrizB[k][j]
            linha.append(valorR)
    matrizR.append(linha)

#imprime matriz A

print('\nMatriz A:')
for i in range(lA):
        print(f'{matrizA[i][j]}')

print('\nMatriz B:')
for i in range(lB):
    print(matrizB[i][j])

#imprime matriz resultante

print('\nMatriz Resultante:')
for i in range(lA):
    print(matrizR[i])