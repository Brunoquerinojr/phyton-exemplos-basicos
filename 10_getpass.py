import getpass as gtp

usuario = input("Nome do usuário: ")
senha = gtp.getpass("Digite sua senha: ")

if len(senha) >= 6:
    print(f"Usuario cadastrado com sucesso!")
else:
    print("Atenção! A senha precisa ter 6 digitos")