# Inicializa as variáveis
notas = []
soma = 0
valido = True

# Loop para pedir as 4 notas
for i in range(4):
    try:
        nota = float(input(f"Digite a {i+1}ª nota (entre 0 e 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            soma += nota
        else:
            print(f"Nota inválida: {nota}. Insira uma nota entre 0 e 10.")
            valido = False
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        valido = False
        break

# Verifica se todas as notas são válidas e exibe a média
if valido:
    media = soma / len(notas)
    print(f"A média das notas é: {media:.2f}")
else:
    print("Não foi possível calcular a média devido a entradas inválidas.")
