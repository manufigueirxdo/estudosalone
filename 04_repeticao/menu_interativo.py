opcao = 0

while opcao != 3:
    print("1. Adicionar cliente.")
    print("2. Ver faturamento.")
    print("3. Sair.")
    
    opcao = int(input("Qual opção você deseja? "))
    
    if opcao == 1:
        print("Adicionar cliente em breve.")
    elif opcao == 2:
        print("Ver faturamento em breve.")
    elif opcao == 3:
        print("Encerrando o sistema...")
    else:
        print("Opção inválida! Tente novamente.")