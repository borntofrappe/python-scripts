class Category:
    def __str__(self):
        output = ""
        output += self.name.center(30, "*")
        for entry in self.ledger:
            amount = round(entry["amount"], 2)
            whole, decimal = str(float(amount)).split(".")
            amount_string = whole + "." + decimal.ljust(2, "0")
            description = entry["description"]
            output = output + "\n" + \
                description[:23].ljust(23, " ") + \
                amount_string[:7].rjust(7, " ")
        output += "\nTotal: " + str(self.get_balance())
        return output

    def __init__(self, name):
        self.ledger = []
        self.name = name

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return round(balance, 2)

    def check_funds(self, amount):
        balance = self.get_balance()
        return balance >= amount

    def deposit(self, amount, description=""):
        entry = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(entry)

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        entry = {
            "amount": amount * -1,
            "description": description
        }
        self.ledger.append(entry)
        return True

    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False

        description_source = "Transfer to " + destination.name
        self.withdraw(amount, description_source)

        description_destination = "Transfer from " + self.name
        destination.deposit(amount, description_destination)

        return True
