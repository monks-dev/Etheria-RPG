from Player import Player
import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

running = True

player = Player(input("What would you like your name to be : "))

def view_inventory():
    pass

def exit_game():
    pass

menu_actions = {
    "1": view_inventory,
    "2": exit_game
}
clear_screen()
while running:
    
    print(("-" * 10 ) + " Etheria " + ("-" * 10 ))
    print(("=" * 29 ))
    print(f"Name : {player.name}")
    print(f"Health : {player.health}/{player.max_health}")
    print(f"Level : {player.level} - Xp : {player.xp}")
    print(f"Gold : {player.gold}")
    print(f"Weapon : {player.equipment.main_hand} - Attack : {player.equipment.main_hand.attack}")
    print(f"Armour : {player.equipment.chest} - Defense : {player.equipment.chest.defense}")
    print(("=" * 29 ))
    print(("-" * 29 ))
    print("[1] - View Inventory ")
    print("[2] - Exit")
    
    option = input("[Choice] > ").strip()
    action = menu_actions.get(option)
    if action:
        action()
    else:
        clear_screen()
        print(f"\nInvalid choice {option}. Please try again !")


def main_menu():
    print(("-" * 10 ) + " Etheria " + ("-" * 10 ))

    print_player_stats(player)
    print_options()

def print_player_stats(player: Player):
    pass


#main_menu()