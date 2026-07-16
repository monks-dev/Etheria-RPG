from Inventory import Inventory
from Equipment import Equipment


class Player:
    def __init__(self, name: str):
        self.name = name
        self.max_health = 20
        self.health = self.max_health
        self.level = 0
        self.xp = 0
        self.gold = 0

        self.inventory = Inventory()
        self.equipment = Equipment()
        
        self.inventory.add_item(self.weapon)
        self.inventory.add_item(self.armour)