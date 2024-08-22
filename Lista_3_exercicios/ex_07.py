while True:
    # Exibe o menu para o usuário
    print("Opções de Programas:")
    print("1 - Eu programo em Python")
    print("2 - Eu programo em PHP")
    print("3 - Eu programo em Java")
    
    # Solicita a escolha do usuário
    escolha = input("Escolha uma opção (1, 2 ou 3): ")
    
    # Verifica a escolha e exibe a mensagem correspondente
    if escolha == '1':
        print("Eu estou estudando Python!")
        break
    elif escolha == '2':
        print("Eu estou estudando PHP!")
        break
    elif escolha == '3':
        print("Eu estou estudando Java!")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
