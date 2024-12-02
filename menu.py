from gerirTrails import TrailManager
from gerirGuias import Guia


def show_menu():
    print('\nMENU')
    print('1. Gerir Trilhos')
    print('2. Gerir Guias')
    print('3. Sair')


def show_submenu():
    print('1 - Criar Trilho')
    print('2 - Atualizar Trilhos')
    print('3 - Remover Trilhos')
    print('4 - Visualizar Trilho')
    print('5 - Voltar')


def show_submenu_guia():
    print('1 - Criar Guia')
    print('2 - Atualizar Guias')
    print('3 - Remover Guias')
    print('4 - Visualizar Guia')
    print('5 - Voltar')


def main():
    # Criar uma instância da classe TrailManager e Guia
    trail_manager = TrailManager()
    guia_manager = Guia()

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
            while True:
                show_submenu_guia()
                opcao3 = input('Escolha uma opção -> ')
                if opcao3 == '1':
                    guia_manager.adicionar_guia('guias.json')
                elif opcao3 == '2':
                    pass
                    # guia_manager.atualizar_guia('guias.json')  # Supondo que esse método exista
                elif opcao3 == '3':
                    pass
                   # guia_manager.remover_guia('guias.json')  # Supondo que esse método exista
                elif opcao3 == '4':
                    pass
                   # guia_manager.visualizar_guia('guias.json')  # Supondo que esse método exista
                elif opcao3 == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao1 == '3':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()