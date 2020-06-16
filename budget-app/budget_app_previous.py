class Category:
    # what gets print when calling the category directly
    def __str__(self):
        name = self.name
        voices = ""
        for voice in self.ledger:
            # i'm sure there's a better way to round a number to two decimals
            # here I use partition, which handily takes care of integer values by placing the result in the first part of the tuple
            amount = voice["amount"]
            numbers = str(amount).partition('.')
            decimals = f"{numbers[0]}.{numbers[2].ljust(2, '0')}"
            description = voice["description"]
            voices += f"{description[:23].ljust(23)}{decimals[:7].rjust(7, ' ')}\n"

        total = str(self.get_balance())

        return f"{name.center(30, '*')}\n{voices}Total: {total}"

    def __init__(self, name):
        self.name = name
        # instance variable
        self.ledger = []

    # operations available on each instance
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        self.ledger.append({"amount": amount * -1, "description": description})

    def get_balance(self):
        balance = 0
        for voice in self.ledger:
            balance += voice["amount"]
        return balance

    def transfer(self, amount, category):
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
