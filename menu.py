from gerirTrails import TrailManager

def show_menu():
    print('\nMENU')
    print('1. Gerir Trilhos')
    print('2. Sair')

def show_submenu():
    print('1 - Criar Trilho')
    print('2 - Atualizar Trilhos')
    print('3 - Remover Trilhos')
    print('4 - Visualizar Trilho')
    print('5 - Voltar')

def main():
    # Criar uma instância da classe TrailManager
    trail_manager = TrailManager()
    while True:
        show_menu()
        opcao1 = input('Escolha uma opção -> ')
        if opcao1 == '1':
            while True:
                show_submenu()
                opcao2 = input('Escolha uma opção -> ')
                if opcao2 == '1':
                    trail_manager.createTrail('trails.csv')
                elif opcao2 == '2':
                    trail_manager.updateTrail("trails.csv")
                elif opcao2 == '3':
                    trail_manager.removeTrail('trails.csv')
                elif opcao2 == '4':
                    trail_manager.readTrail('trails.csv')
                elif opcao2 == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao1 == '2':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()