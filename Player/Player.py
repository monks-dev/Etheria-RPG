from Player.Inventory import Inventory
from Player.Equipment import Equipment, EquipmentSlot

from Items.Weapon import Weapon
from Items.Shield import Shield
from Items.Armour import Armour

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
        
        self.equipment.main_hand = Weapon("Iron Sword", "Basic Sword", 10, 3)
        self.equipment.chest = Armour("Leather Chestplate", "Leather", 10, 5)