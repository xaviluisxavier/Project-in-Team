from TrailManager import TrailManager
from GuideManager import Guide

def show_menu():
    print('\nMENU')
    print('1. Manage Trails')
    print('2. Manage Guides')
    print('3. Exit')

def show_submenu():
    print('1 - Create Trail')
    print('2 - Update Trails')
    print('3 - Remove Trails')  # This option allows for removing trails
    print('4 - View Trail')
    print('5 - Back')

def show_guide_submenu():
    print('1 - Create Guide')
    print('2 - Update Guides')
    print('3 - Remove Guides')
    print('4 - View Guide')
    print('5 - Back')

def main():
    # Create an instance of TrailManager and Guide classes
    trail_manager = TrailManager()
    guide_manager = Guide()

    while True:
        show_menu()
        option1 = input('Choose an option -> ')
        if option1 == '1':
            while True:
                show_submenu()
                option2 = input('Choose an option -> ')
                if option2 == '1':
                    # Create a new trail
                    trail_manager.create_trail('trails.csv')  # Calls create_trail method
                elif option2 == '2':
                    # Update Trails
                    trail_manager.update_trail("trails.csv")  # Calls update_trail method
                elif option2 == '3':
                    # Remove Trails
                    trail_manager.remove_trail('trails.csv')  # Calls remove_trail method
                elif option2 == '4':
                    # View Trail
                    trail_manager.read_trail('trails.csv')  # Calls read_trail method
                elif option2 == '5':
                    break  # Go back to main menu
                else:
                    print("Invalid option. Try again.")
        elif option1 == '2':
            while True:
                show_guide_submenu()
                option3 = input('Choose an option -> ')
                if option3 == '1':
                    guide_manager.add_guide('guides.json')  # Ensure this method exists
                elif option3 == '2':
                    pass  # Implement update functionality
                elif option3 == '3':
                    pass  # Implement remove functionality
                elif option3 == '4':
                    pass  # Implement view functionality
                elif option3 == '5':
                    break  # Go back to main menu
                else:
                    print("Invalid option. Try again.")
        elif option1 == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Try again.")


main()