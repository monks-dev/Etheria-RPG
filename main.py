from Player import Player

def main_menu():

    player = create_player()

    print(("-" * 10 ) + " Etheria " + ("-" * 10 ))

    print_player_stats(player)
    print_options()

def create_player():
    return Player(input("What would you like your name to be : "))


def print_player_stats(player: Player):
    print(("=" * 29 ))
    print(f"Name : {player.name}")
    print(f"Health : {player.health}/{player.max_health}")
    print(f"Level : {player.level} - Xp : {player.xp}")
    print(f"Gold : {player.gold}")
    print(f"Weapon : {player.weapon.name} - Attack : {player.weapon.attack}")
    print(f"Armour : {player.armour.name} - Defense : {player.armour.defense}")
    print(("=" * 29 ))
    print(("-" * 29 ))


def print_options():
    print("[1] - View Inventory ")
    print("[2] - Exit")


main_menu()