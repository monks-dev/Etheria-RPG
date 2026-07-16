from enum import Enum, auto
from Item import Item



class Armour(Item):
    def __init__(self, name: str, description: str, value: int, defense: int, slot: ArmourSlot):
        super().__init__(name, description, value)
        self.defense = defense
        self.slot = slot