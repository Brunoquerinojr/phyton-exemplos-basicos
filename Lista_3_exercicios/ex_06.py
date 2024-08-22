# Inicializa o número
n = 0

# Cabeçalho da tabela
print("nro\tquad\tcubo")

# Laço while para calcular quadrados e cubos
while n <= 50:
    quadrado = n ** 2
    cubo = n ** 3
    print(f"{n}\t{quadrado}\t{cubo}")
    n += 1
