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

```py
def matches_four(self):
  return False
```

For starters, I created a utility function to display a message almost as a header.

```py
def highlight_message(message):
    print()
    print("*" * len(message))
    print(message)
    print("*" * len(message))
    print()
```

For an arbitrary message:

```py
highlight_message("Connect Four")

"""
************
Connect Four
************
"""
```

The game itself, it is set up in a function `run_game`, with the following sequence:

- introduce the game

- set up the grid and display the same

  ```py
  columns = 6
      rows = 6
      grid = Grid(columns, rows)

      print(grid)
      print()
  ```

- initialize a variable to keep track of the player

  ```py
  player = "R"
  ```

  I chose `R` and `T` arbitrarily.

- set up a loop. Almost like a game loop, the idea is to ask for input until the game is complete.

  ```py
  while True:
  ```

### Game Loop

In the game loop notify the current player and ask for which column to actually fill.

```py
print(f"Player: {player}")
column = input("Select column: ")
```

I decided to add an arbitrary condition to exit the game, by entering the letter `q`, but let's focus on the input itself. The idea is to handle a few errors:

- the input is not a number

- the input doesn't describe a viable column. This either because out of range, or because the column is already filled

The second error is a bit more challenging, so starting with the first.

### try except else

When you coerce a string into a number with the `int` function, you get an error if the input cannot be coerced.

The [docs](https://docs.python.org/3/tutorial/errors.html) describe quite a bit about error handling, but here I use a try..except..else sequence.

1. try something

```py
try:
    c = int(column)
```

Handle the specific error

```py
except ValueError:
  highlight_message("**Enter a number**")
```

Continue with the input integer.

```py
else:
  # consider column
```

### try except else/2

When selecting the column:

```py
grid_column = list(reversed(grid_transposed[column]))
index = grid_column.index(" ")
```

There are two possible errors:

1. `IndexError`. This is when the number exceeds the number of columns, and you try to access a column that does not exist

1. `ValueError`. This is when a column is full, and `.index(" ")` doesn't find the value in the list.

Both errors can be considered in a try, except, else block,

```py
try:
    grid_column = list(reversed(grid_transposed[column]))
    index = grid_column.index(" ")
except (IndexError, ValueError):
    # handle error
else:
    # handle success, add the input to the selected column
    self.grid[len(self.grid) - 1 - index][column] = input
```

Since I plan to notify the player from the game loop, I decided to also return a boolean for each of the two routes. This allows to show a message right in the `run_game` function.

- if `add_to_column` returns true, show the grid and update the player

```py
if grid.add_to_column(c, player):
  print()
  print(grid)
  print()

  if player == "R":
      player = "T"
  else:
      player = "R"
```

If `False`, notify the player of the mishap/error.

```py
else:
  highlight_message(f"**Column unavailable**")
```

### Victory

Back to the `matches_four()` function, the idea is to check for a victory after the grid is updated and notified.

```py
if grid.add_to_column(c, player):
  print()
  print(grid)
  print()

  if grid.matches_four():
    # handle victory
    break
```

This allows to describe the winner by referencing the current player.

```py
if grid.matches_four():
  highlight_message(f"Player {player} wins!")
  break
```

To check for a victory, it is actually helpful to know the coordinates of the cell. To this end, instead of returning `True`, `.add_to_column` is updated to return a tuple describing the selected row and column.

```py
row = len(self.grid) - 1 - index
# update grid
self.grid[row][column] = input

# return coordinates
return (row, column)
```

With this information, it is necessary to check the row/column/diagonals including the cell.

```py
cell = grid.add_to_column(c, player)
  if cell:
    row, column = cell
    if grid.matches_four(row, column):
      # handle victory
```

In the body of the function we finally check for the matches. I fumbled a little with _how_ to do this, but eventually, I find a rather nifty approach using the `.index()` function.

Here's the idea:

- build a string for the current row, column, diagonals

- find if the string contains four instances of the current player. `RRRR` or `TTTT`

`.index()` actually prompts an error if there's no such value, so a `try` `except` `else` block is required.

```py
match = ''
# build string

try:
    match.index(player * 4)
except ValueError:
    return False
else:
    return True
```

For the row, it is enough to consider a list from the grid and the given index.

```py
current_row = self.grid[row]
for cell in current_row:
    match += cell
match += ' '
```

Notice I included an additional whitespace character, to avoid finding a match between the row and the column.

For the column, instead of transposing the entire grid, I can build a list using a list comprehension, and the number of rows in the grid itself.

```py
current_column = [self.grid[index][column] for index in range(len(self.grid))]
```

It didn't come immediately, and it helped to build the list with a for loop first.

```py
current_column = []
for index in range(len(self.grid)):
  current_column.append(self.grid[index][column])
```

Either way, the values of the current column are added to the string exactly like with the current row.

```py
for cell in current_column:
    match += cell
match += ' '
```

The most challenging portion then, relates to adding the values for the diagonals.

### Victory/2

I pick up this project a couple of days since the previous update, and I decided to rewrite the way I consider the rows and columns before considering the diagonals. It is inefficient to consider the entire row/the entire column. To tackle this issue, I use the `min` and `max` function to build a range of the appropriate values.

For the rows, and considering that a match consists of `4` values, consider up to three columns before/after the current one.

```py
c_min = max(0, column - 3)
c_max = min(self.columns, column + 3)
for c in range(c_max - c_min):
    match += self.grid[row][c + c_min]
```

Took me a while to grasp the logic, but divvying up the code with two additional variables helped.

For the column, the logic is repeated considering up to three cells before and after the current row. This time, it is also unnecessary to consider that the grid is read top down, as we access the cells based on the given row.

```py
r_min = max(0, row - 3)
r_max = min(self.rows, row + 3)
for r in range(r_max - r_min):
  match += self.grid[r + r_min][column]
```

I forgot to mention however, that after each addition to the `match` string, I still add an empty space to avoid finding a match between in between the row and column.

```py
match += ' '
```

Back to the diagonals, and the crux of this game, I actually found a solution in the for loop describing the row. I'll elaborate the idea, and try to come up with a better explanation in a future update.

The idea is to consider the distance from the current cell, and add the value in the previous/following row on the basis of this very distance.

In this made up example:

```code
x x c x x
```

When you consider the first column, you consider the cell in the row twice above and below the current one.

```code
-2 -1 0 1 2
```

It took me a while, but making sure that such a row is available, it is possible to consider both diagonals by adding or subtracting the distance to the current row.
