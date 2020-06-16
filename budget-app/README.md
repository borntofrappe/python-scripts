# Budget App

> Third project of five to earn the **Scientific Computing with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

- there are actually two scripts. One created in the end of January 2020, one in June 2020 as I reviewed the project. The two differ since the project was updated with additional requirements, and since I've learned more about the Python language

## Assignment

This project allows to practice with Object Oriented Programming (OOP) in the context of the Python language.

It requires to complete a `Category` class, as well as a `create_spend_chart` function.

### Category

There are plenty of rules regarding the `Category` class, especially regarding how each instance object is supposed to look when printed as a string.

Putting the `__str__` method on the back burner for a moment, here the rules describing the attributes and methods of the class.

#### Attributes

Each instance is initialized with a string specifying the name.

```py
food = Category("Food")
```

Therefore, specify a field for the name of the category.

```py
def __init__(self, name):
    self.name = name
```

`self.ledger` is added as a list and an instance variable.

```py
def __init__(self, name):
    self.name = name
    self.ledger = []
```

The idea is to append to the ledger the deposit/withdraw/transfer operations later enacted on the category.

#### Methods

Let me describe the methods in a different order than the assignment. In order of usefulness, so to speak:

- `get_balance` tallies the amounts, and returns the balance

  ```py
  def get_balance(self):
      balance = 0
      for voice in self.ledger:
          balance += voice["amount"]
      return round(balance, 2)
  ```

  `round` allows to consider up to 2 decimal digits

- `check_funds` describes whether an input amount is available

  ```py
  def check_funds(self, amount):
      balance = self.get_balance()
      return balance >= amount
  ```

- `deposit` creates a voice in the ledger

  ```py
  def deposit(self, amount, description=""):
      voice = {
          "amount": amount,
          "description": description
      }
      self.ledger.append(voice)
  ```

  If no description is given, use an empty string

- `withdraw` checks if the funds allow to withdraw the input amount, and if so creates a matching entry in the ledger

  ```py
  def withdraw(self, amount, description=""):
      if not self.check_funds(amount):
          return False

      voice = {
          "amount": amount * -1,
          "description": description
      }
      self.ledger.append(voice)
      return True
  ```

- `transfer` checks if funds allow for the transfer of the input amount, and then fires a withdraw/deposit operation considering a destination category

  ```py
  def transfer(self, amount, destination):
    if not self.check_funds(amount):
        return False

    description_source = "Transfer to " + destination.name
    self.withdraw(amount, description_source)

    description_destination = "Transfer from " + self.name
    destination.deposit(amount, description_destination)

    return True
  ```

  <!-- ### create_spend_chart -->
