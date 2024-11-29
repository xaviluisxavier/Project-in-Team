from gerirTrails import TrailManager


def show_menu():
    print('\nMENU')
    print('1. Gerir Trilhos')
    print('2. Sair')


def show_submenu():
    print('1 - Criar Trilho')
    print('2 - Atualizar Trilhos')
    print('3 - Remover Trilhos')
    print('4 - Visualizar Trilhos')
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
                    trail_manager.createTrail()
                elif opcao2 == '2':
                    print("Função de atualização ainda não implementada.")
                elif opcao2 == '3':
                    print("Função de remoção ainda não implementada.")
                elif opcao2 == '4':
                    print("Função de visualização ainda não implementada.")
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