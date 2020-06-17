# [Probability Calculator](https://repl.it/@borntofrappe/fcc-probability-calculator)

> Fifth project of five to earn the **Scientific Computing with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

- there are actually two scripts. One created in the end of January 2020, one in June 2020 as I reviewed the project. The two differ since the project was updated with additional requirements, and since I've learned more about the Python language

## Lessons learned

- accept a variable number of keyword arguments (arguments describing a key=value pair)

  ```py
  class Hat:
      def __init__(self, **kwarg):
          print(kwarg)
  ```

  It provides a dictionary where the keys are the fields, the values their values

- create a random integer to target an item in a list

  ```py
  random_index = random.randrange(len(list))
  ```

  Using `random.randint(a, b)` would actually provide a value greater or equal than `a`, smaller or equal than `b`. You'd need the more convoluted syntax `random.randint(0, len(list) - 1)`
