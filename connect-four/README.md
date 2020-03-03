# Connect Four

A game in which you are tasked to link together shapes of the same color.

## Links

- [Tutorial](https://youtu.be/XGf2GcyHPhc?t=5705) on the [freecodecamp YouTube channel](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) inspiring the project.

  Inspiring, but not driving the project. I plan to review the video _after_ I give the challenge its fair chance, and jot my notes on what I've learned from it.

- [Repl](https://repl.it/@borntofrappe/connect-four) in which the game is played in the terminal. Run the program and then select the column in which to slot the shape.

<!-- - [Repl]() recreating the game with the pygame module -->

## C4 - Terminal

In its first version, the game displays a grid right in the terminal. The idea is to provide a grid with the following format:

```code
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
 --- --- --- --- ---
  0   1   2   3   4
```

Past the grid, the player is tasked to select a column and add a shape of a particular color. `R` for red, `T` for tangerine.

```code
Player: R
Select column: {{ask for input in the [0-4] range}}
```

At each iteration you position a letter at the bottom of the grid.

```code
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   | R |   |
 --- --- --- --- ---
  0   1   2   3   4
```

And toggle the player's choice.

```code
Player: T
Select column: {{ask for input in the [0-4] range}}
```

### Grid

Starting with a class creating and displaying the grid. The idea is to have an object created as follows:

```py
columns = 5
rows = 5
grid = Grid(columns, rows)
```

Therefore.

```py
class Grid:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
```

To create the grid, I would ordinarily use a for loop, but having learned about [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html?highlight=comprehension#list-comprehensions), I decided to give the syntax a try.

### List Comprehension(s)

With a for loop, create a list as follows:

```py
nums = []
for i in range(5):
  nums.append(i)

print(nums) # [0, 1, 2, 3, 4]
```

With a list comprehension, you write the for loop in between brackets, as you assign the value to the variable.

```py
nums = [i for i in range(5)]
print(nums) # [0, 1, 2, 3, 4]
```

The tricky bit is that the grid is better off described as a nested list.

With a for loop.

```py
columns = 4
rows = 3

grid = []
for r in range(rows):
  row = []
  for c in range(columns):
    row.append((r, c))
  grid.append(row)

print(grid)

"""
[
  [(0, 0), (0, 1), (0, 2), (0, 3)],
  [(1, 0), (1, 1), (1, 2), (1, 3)],
  [(2, 0), (2, 1), (2, 2), (2, 3)]
]
"""
```

With a list comprehension:

```py
columns = 4
rows = 3

grid = [[(r, c) for c in range(columns)] for r in range(rows)]
print(grid)
"""
[
  [(0, 0), (0, 1), (0, 2), (0, 3)],
  [(1, 0), (1, 1), (1, 2), (1, 3)],
  [(2, 0), (2, 1), (2, 2), (2, 3)]
]
"""
```

Might need some getting use to it. Consider it in increments.

```py
grid = [r for r in range(rows)]
```

`r` is the value added to the list. In this instance, the integer in the `[0, rows]` range, but the idea is to include another list.

```py
grid = [[] for r in range(rows)]
```

Just not any other list however. A list describing the columns, which itself can be created with a list comprehension.

```py
grid = [[c for c in range(columns)] for r in range(rows)]
```

Instead of adding just the column, finally, you include the tuple specifying the cell's coordinates, `(r, c)`.

Long-winded, but hopefully clear enough.

### Grid/2

Back to the grid, instead of the coordinates, create a grid of empty items.

```py
class Grid:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = [[" " for c in range(columns)] for r in range(rows)]
```

`self.columns` and `self.rows` might be unnecessary, but I'll keep them for the time being.

### **str**

The `print` statement produces whatever is returned in the `__str__` method.

```py
class Grid:
    def __str__(self):
      return "Hello"

    # init

grid = Grid(4, 3)
print(grid)
# Hello
```

To display the desired format, here's what I ended up creating with nested for loops and string concatenation.

```py
class Grid:
  def __str__(self):
    grid = ""
    for row in self.grid:
        # initial pipe
        grid += "|"
        for cell in row:
          # "   |"
          grid += cell.center(3, " ") + "|"
        # new row, new line
        grid += "\n"
    return grid

grid = Grid(4, 3)
print(grid)
"""
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
"""
```

A bit of trial and effort was required.

At the end of the grid, add a new line for the dashes describing the floor, and a new line for the indexes of the columns.

```py
class Grid:
  def __str__(self):
    grid = ""
    # pipes
    for row in self.grid:
        grid += "|"
        for cell in row:
          grid += cell.center(3, " ") + "|"
        grid += "\n"

    # dashes
    grid += " " + "--- " * self.columns

    # nums
    grid += "\n "
    for c in range(self.columns):
      grid += str(c).center(4, " ")
    return grid

    # init

grid = Grid(4, 3)
print(grid)
"""
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
 --- --- --- ---
  0   1   2   3
"""
```

I would add a variable to describe the number of spaces between cells, instead of using hard-coded integers, overall I'm pretty satisfied with the end result.
