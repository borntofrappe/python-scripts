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

### List comprehension

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

### Class methods

The idea is to use a method to add a letter at the bottom of the grid. I would also need a method to empty the grid, but that's easier to implement.

```py
class Grid:
  # re-initialize grid
  def clear(self):
    self.grid = [[" " for c in range(self.columns)] for r in range(self.rows)]

```

For the method adding the letter, a bit more haggling is necessary. The goal is to call this method as follows:

```py
grid.add_to_column(3, "R")
```

And have it fill the column with the specified input. Starting from the bottom, and using the first empty space in the column itself.

```
|   |   |   |   |
|   |   |   |   |
|   |   |   | R |
 --- --- --- ---
  0   1   2   3
```

### List comprehension/2

The documentation for [nested list comprehensions](https://docs.python.org/3/tutorial/datastructures.html?highlight=comprehension#nested-list-comprehensions) actually described something very helpful in this regard: how to _transpose_ a matrix. The idea is to describe a grid through its columns, so to have easier access to the cells in order.

Let me repeat the "for loop" first, "list comprehension" later approach, just to understand the syntax.

With a for loop:

```py
grid = [
  [1, 2, 3],
  [4, 5, 6]
]
grid_transposed = []

rows = len(grid)
columns = len(grid[0])

for c in range(columns):
  column = []
  for r in range(rows):
    column.append(grid[r][c])
  grid_transposed.append(column)

print(grid)
"""
[
  [1, 4],
  [2, 5],
  [3, 6]
]
"""

```

Works well enough, of course assuming the grid can be transposed.

With a list comprehension, it might lead to some head-scratching, but it is as follows:

```py
rows = len(grid)
columns = len(grid[0])

grid_transposed = [[grid[r][c] for r in range(rows)] for c in range(columns)]
```

### Grid/3

Back to the grid, create the transposed grid using the rows and columns saved in the `__init__` method.

```py
def add_to_column(self, column, input):
    grid_transposed = [[self.grid[r][c] for r in range(self.rows)] for c in range(self.columns)]
```

Identify the desired column:

```py
def add_to_column(self, column, input):
    grid_transposed = [[self.grid[r][c] for r in range(self.rows)] for c in range(self.columns)]
    grid_column = grid_transposed[column]
```

The index of the first empty space.

```py
def add_to_column(self, column, input):
    grid_transposed = [[self.grid[r][c] for r in range(self.rows)] for c in range(self.columns)]
    grid_column = grid_transposed[column]
    index = grid_column.index(" ")
```

And modify the value in the original grid.

```py
def add_to_column(self, column, input):
    grid_transposed = [[self.grid[r][c] for r in range(self.rows)] for c in range(self.columns)]
    grid_column = grid_transposed[column]
    index = grid_column.index(" ")
    self.grid[index][column] = input
```

Almost there. The value is added, but not quite where we'd want it.

```py
columns = 5
rows = 4
grid = Grid(columns, rows)
grid.add_to_column(3, "R")
grid.add_to_column(3, "T")
print(grid)

"""
|   |   |   | R |   |
|   |   |   | T |   |
|   |   |   |   |   |
|   |   |   |   |   |
 --- --- --- --- ---
  0   1   2   3   4
"""
```

### reversed

The first, most obvious shortcoming is fixed by considering that the transposed grid reads top to bottom, and the goal is to add the items in reverse order.

To fix this, reverse the column as it is retrieved.

```py
grid_column = list(reversed(grid_transposed[column]))
```

It seems necessary to use the `list` function as `reversed` returns a [reverse iterator](https://docs.python.org/3/library/functions.html#reversed).

This leads to the correct index bottom to top, but it is then necessary to modify the value in the original grid starting from the end of the grid.

```py
self.grid[len(self.grid) - 1 - index][column] = input
```

Definitely not my first try, but it works.

```py
columns = 5
rows = 4
grid = Grid(columns, rows)
grid.add_to_column(3, "R")
grid.add_to_column(3, "T")
print(grid)

"""
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   | T |   |
|   |   |   | R |   |
 --- --- --- --- ---
  0   1   2   3   4
"""
```

### try except

The second issue is what happens when you add to a column that is already filled.

```py
columns = 5
rows = 4
grid = Grid(columns, rows)
grid.add_to_column(3, "R")
grid.add_to_column(3, "T")
grid.add_to_column(3, "T")
grid.add_to_column(3, "T")
grid.add_to_column(3, "T")

# ValueError: ' ' is not in list
```

A `try...except` block allows to handle this error more gracefully. The idea is to literally try something, in this instance finding the index of the empty space.

```py
try:
  index = grid_column.index(" ")
  self.grid[len(self.grid) - 1 - index][column] = input
```

In the `except` statement then the idea is to handle the specific error.

```py
except ValueError:
            print("Column unavailable")
```

### Gameplay

With the grid class "complete", the next step is creating the game, and allowing to fill the grid following user input. I put "complete" between quotes because I can think of at least another useful method in the class, to dictate whether four values match.
