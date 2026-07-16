from Weapon import Weapon
from Armour import Armour, ArmourSlot
from Inventory import Inventory

class Player:
    def __init__(self, name: str):
        self.name = name
        self.max_health = 20
        self.health = self.max_health
        self.level = 0
        self.xp = 0
        self.gold = 0

        self.inventory = Inventory()


        self.weapon: Weapon = Weapon(
            name="Iron Sword",
            description="Basic Iron Swrod",
            value=10,
            attack=3
        )
        self.armour: Armour = Armour(
            name="Leather Chestpiece",
            description="Basic Leather Chestpiece",
            value=10,
            defense=5,
            slot=ArmourSlot.CHEST
        )
        
        self.inventory.add_item(self.weapon)
        self.inventory.add_item(self.armour)