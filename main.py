from Player.Player import Player
from Menus.MainMenu import MainMenu
import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def view_inventory():
    pass

def exit_game():
    pass

menu_actions = {
    "1": view_inventory,
    "2": exit_game
}

def display_equipment(player: Player):
    print(("-" * 10 ) + "Equipment" + ("-" * 10 ))
    for equipment in player.equipment.get_equipment():
        if equipment == None:
            continue
        print(equipment)


def display_player_stats(player: Player):
    print(("=" * 29 ))
    print(("-" * 8 ) + " Player Info " + ("-" * 8 ))
    print(f"Name : {player.name}")
    print(f"Health : {player.health}/{player.max_health}")
    print(f"Level : {player.level} - Xp : {player.xp}")
    print(f"Gold : {player.gold}")
    print(("=" * 29 ))
    
    display_equipment(player)

    print(("=" * 29 ))

def main_menu():
    running = True
    player = Player(input("What would you like your name to be: "))

    menu = MainMenu()

    while running:
        clear_screen()
        display_player_stats(player)
        menu.display()


        choice = menu.get_choice()

        if choice == "1":
            print("Inventory Open")
        elif choice == "2":
            print("L Gamer")
            running = False


        # option = input("[Choice] > ").strip()
        # if option not in menu_actions:
        #     input(f"Invalid choice '{option}'. Press Enter to continue.")
        #     continue

        # menu_actions[option]()

if __name__ == "__main__":
    main_menu()