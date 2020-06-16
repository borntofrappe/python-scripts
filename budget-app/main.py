import budget

food = budget.Category("Food")
business = budget.Category("Business")
entertainment = budget.Category("Entertainment")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(budget.create_spend_chart([business, food, entertainment]))
