# [Budget App](https://repl.it/@borntofrappe/fcc-budget-app)

> Third project of five to earn the **Scientific Computing with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

- there are actually two scripts. One created in the end of January 2020, one in June 2020 as I reviewed the project. The two differ since the project was updated with additional requirements, and since I've learned more about the Python language

## Assignment

This project allows to practice with Object Oriented Programming (OOP) in the context of the Python language.

It requires to complete a `Category` class, as well as a `create_spend_chart` function.

### Category

The category specifies two attributes and a series of methods. Each instance allows to define a budget category, and then enact a series of operations through said methods: deposits, withdraws, transfers. There are also a couple of functions to obtain the total, and check if the category has enough funds, but those methods are relatively easier to parse.

The `__str__` function is perhaps the more convoluted one, but the goal is to format the budget category with a definite format.

```code
*******Title*********
initial deposi 100.25
entry decscrip -50.00
decscription     2.54
Total: 52.79
```

### create_spend_chart

The function takes as input a list of categories, and produces a bar chart with ASCII characters. To detail the height of the bars, compute the total expenditure, and then the percentage of each individual category.

The rest is a tedious exercise in formatting the string with whitespace, `-` dash and `|` pipe characters.
