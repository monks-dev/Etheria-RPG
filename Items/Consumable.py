from Items.Item import Item

class Consumable(Item):
    def __init__(self, name: str, description: str, value: int, health_on_use: int):
        super().__init__(name, description, value)
        self.health_on_use = health_on_use

    def use(self, player : Player):
        if player.health >= player.max_health: # Checking to see if the player is at full health or not so they dont use the consumable
            return False
        # Else if the player isnt full then use the consumable
        player.health = min(player.max_health, player.health + self.health_on_use)

        return True