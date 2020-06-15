# [Shape Calculator](https://repl.it/@borntofrappe/fcc-shape-calculator)

> Third project of five to earn the **Scientific Computing with Python** certification on freeCodeCamp.

The note introducing the projects **arithmetic-formatter** and **time-calculator** is repeated here as well.

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

- there are actually two scripts. One created in the end of January 2020, one in June 2020 as I reviewed the project. The two differ since the project was updated with additional requirements

## Assignment

This project allows to practice with Object Oriented Programming (OOP) in the context of the Python language.

- define a class `Rectangle`, with two attributes and a variety of methods (more on this later)

- define a class `Square`, have it inherit the attributes and methods of the `Rectangle` class, but update the syntax according to the specifities of the shape (same width and height for instance).

## Lessons learned

### Class(es)

To inherit a class, you specify the class in between parenthesis.

```py
class Square(Rectangle):
```

However, this is not enough to set up the class, and have it inherit the connected attributes and methods. In the `init` function, call `super()` to have access to the to-be-inherited class.

```py
def __init__(self, side):
    super().__init__(side, side)
```

In this instance it's as if you were calling `Rectangle(side, side)`. The unique value is used for both the width and height.

### Override

When inheriting the methods of the `Rectangle` class, `Square` gains access to `set_width` and `set_height`. These are however improper in the context of a shape where all the sides are meant to have the same length.

To override this default, define the function once more, and with the desire values.

```py
def set_width(self, width):
    self.set_side(width)

def set_height(self, height):
    self.set_side(height)
```

Handily enough, it is possible to benefit from the `set_side` method made available on the new class.

```py
def set_side(self, side):
    self.width = side
    self.height = side
```

### Output

The `get_picture()` method is meant to provide an ASCII visual of the shapes.

```py
rect = Rectangle(2, 3)
rect.get_picture()
"""
**
**
**
"""
```

Previously, I used a loop to describe the rows

```py
output = ""
for i in range(self.height):
    output += "*" * self.width
    output += "\n"
```

But using the multiplication character twice, you can achieve a similar result in a single, if slightly harder to parse, syntax.

```py
output = ("*" * self.width + "\n") * self.height
```

You can even return the value without initializing the `output` variable.
