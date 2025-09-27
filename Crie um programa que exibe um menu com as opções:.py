while True:
    print("\n[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá! Seja bem-vindo.")
    elif opcao == "2":
        print("Você escolheu a opção de Ajuda.")
    elif opcao == "3":
        print("Saindo do programa... Até logo!")
        break
    else:
        print("Opção inválida, tente novamente.")