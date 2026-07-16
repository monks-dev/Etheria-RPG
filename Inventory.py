from Item import Item

class Inventory():
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        # Dont call list.remove() unless we sure the item exsist,
        if (item not in self.items):
            return False

        self.items.remove(item)
        return True

    def print_items(self):
        for item in self.items:
            print(f"Name: {item.name} - Value: {item.value}")