from Items.Weapon import Weapon
from Items.Shield import Shield
from Items.Armour import Armour
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

        self.main_hand: Weapon  = None
        self.off_hand: Weapon | Shield  = None

        self.head: Armour  = None
        self.chest: Armour  = None
        self.legs: Armour  = None
        self.boots: Armour  = None

        self.ring: Armour  = None
        self.necklace: Armour  = None


    def get_equipment(self) -> tuple:
        return (self.main_hand, self.off_hand, self.head, self.chest, self.legs, self.boots, self.ring, self.necklace)

    def equip_item(item: Weapon | Shield | Armour, slot: EquipmentSlot):
        pass