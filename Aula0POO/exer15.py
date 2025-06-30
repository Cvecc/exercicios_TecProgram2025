#Crie um menu que permita ao usuário escolher opções até ele decidir sair.

while True:
    print("\nMenu de Cores:")
    print("1 - Vermelho")
    print("2 - Azul")
    print("3 - Verde")
    print("4 - Amarelo")
    print("5 - Sair")

    escolha = int(input("Escolha uma opção (1-5): "))

    if escolha == 1:
        print("Você escolheu a cor Vermelho.")
    elif escolha == 2:
        print("Você escolheu a cor Azul.")
    elif escolha == 3:
        print("Você escolheu a cor Verde.")
    elif escolha == 4:
        print("Você escolheu a cor Amarelo.")
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")