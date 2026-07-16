from Item import Item

class Weapon(Item):
    def __init__(self, name: str, description: str, value: int, attack: int):
        super().__init__(name, description, value)
        self.attack = attack