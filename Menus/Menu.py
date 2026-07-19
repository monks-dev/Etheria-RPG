class Menu:
    def __init__(self, title: str):
        self.title = title
        self.options: dict[str, str] = {}

    def add_option(self, key: str, label: str):
        self.options[key] = label

    def display(self) -> None:
        print(("-" * 10 ) + self.title + ("-" * 10 ))

        for key, label in self.options.items():
            print(f"[{key}] - {label}")

    def get_choice(self) -> str:
        while True:
            choice = input("[Choice] >").strip().upper()

            if choice in self.options:
                return choice

            print(f"Invalid choice: {choice}")
    