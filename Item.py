class Item:
    def __init__(self, name: str, description: str, value: int):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self) -> str:
        return self.name