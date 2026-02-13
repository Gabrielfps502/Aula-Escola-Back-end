Usuarios = {}
while True:
    print("1- Cadastrar:")
    print("2- Login")
    print("3- Sair")
    opção = input("Escolha:")
    
    if opção == "1":
        Login = input("Login:").strip()
        if Login in Usuarios or Login == "":
            print("Login invalido ou já existente")
            continue
        senha = input ("Senha: ").strip()
        Usuarios[Login] = senha 
        print("Usuario Cadastrado!")

    elif opção == "2":
        Login = input("Login:").strip()
        senha = input("senha:").strip()
        if Login in Usuarios and Usuarios[Login] == senha:
            print("Login Realizado")
        else:
            print("Login incorreto")
    elif opção == "3":
        break