valores = [12, 88, 45, 23, 88, 9, 37, 55, 64, 12, 70, 18, 23, 41, 73, 37, 60, 29, 55, 8, 91, 33, 70, 12]

# Média
soma = 0
tamanho = 0
for i in valores:
    soma += i
    tamanho += 1

print(soma/tamanho)

# Moda
for i in valores:


# Mediana
valores.sort()
if tamanho % 2 == 0:
    n1 = valores[tamanho // 2 - 1]
    n2 = valores[tamanho // 2]
    print((n1 + n2) / 2)
else:
    print(valores[tamanho // 2])
