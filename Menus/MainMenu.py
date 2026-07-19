from Menus.Menu import Menu

class MainMenu(Menu):
    def __init__(self, title: str = "Main Menu"):
        super().__init__(title=title)

        self.add_option("1", "View Inventory")
        self.add_option("2", "Exit Game")


