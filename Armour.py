from Item import Item


class Armour(Item):
    def __init__(self, name: str, description: str, value: int, defense: int):
        super().__init__(name, description, value)
        self.defense = defense