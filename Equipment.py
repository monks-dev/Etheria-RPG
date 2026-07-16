from Weapon import Weapon
from Shield import Shield
from Armour import Armour
from enum import Enum, auto

class EquipmentSlot(Enum):
    MAIN_HAND = auto()
    OFF_HAND = auto()
    TWO_HAND = auto()

    HEAD = auto()
    CHEST = auto()
    LEGS = auto()
    BOOTS = auto()

    RING = auto()
    NECKLACE = auto()


class Equipment:
    def __init__(self):

        self.main_hand: Weapon | None = None
        self.off_hand: Weapon | Shield | None = None

        self.head: Armour | None = None
        self.chest: Armour | None = None
        self.legs: Armour | None = None
        self.boots: Armour | None = None

        self.ring: Armour | None = None
        self.necklace: Armour | None = None

    
    def equip_item(item: Weapon | Shield | Armour, slot: EquipmentSlot):
        pass