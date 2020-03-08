# [Connect Four](https://repl.it/@borntofrappe/connect-four)

> Match cells of the same color in the terminal console

## Links

- [Tutorial](https://youtu.be/XGf2GcyHPhc?t=5705) on the [freecodecamp YouTube channel](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) inspiring the project.

  Inspiring, but not driving the project. I plan to review the video _after_ I give the challenge its fair chance, and jot my notes on what I've learned from it.

- [Repl](https://repl.it/@borntofrappe/connect-four) in which the game is played in the terminal. Run the program and then select the column by entering the matching number.

## Getting Started

The idea is to provide a grid with the following format:

```code
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
 --- --- --- --- ---
  0   1   2   3   4
```

Past the grid, the player is asked to pick a column and add a letter. `R` for red, `T` for tangerine.

```code
Player: R
Select column: {{ask for input in the [0-4] range}}
```

At each iteration, the letter is positioned at the bottom of the grid.

```code
Player: R
Select column: 3

"""
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   | R |   |
 --- --- --- --- ---
  0   1   2   3   4
"""
```

The player's choice is toggled to the other value and the process is repeated.

```code
Player: T
Select column: 3

"""
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   | T |   |
|   |   |   | R |   |
 --- --- --- --- ---
  0   1   2   3   4
```

## Grid

I plan to recreate the grid with a class. The goal is to have an instance of the class as follows:

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

With a for loop, you create a list as follows:

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

The tricky bit for the current game is that the grid is actually a nested list.

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

`r` is the value added to the list. In this instance, the integer in the `[0, rows]` range.

Instead of a single value `r` however, the idea is to include another list.

```py
grid = [[] for r in range(rows)]
```

Just not any other list though. A list describing the columns, which itself can be created with a list comprehension.

```py
grid = [[c for c in range(columns)] for r in range(rows)]
```

Instead of adding just the column, finally, you include the tuple specifying the cell's coordinates, `(r, c)`.

Long-winded, but hopefully clear enough.

## Grid/2

Back to the grid, instead of the coordinates, create a grid of empty items.

```py
class Grid:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = [[" " for c in range(columns)] for r in range(rows)]
```

`self.columns` and `self.rows` might be unnecessary, but I'll keep them for the time being.

## **str**

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

Fait to say that a bit of trial and effort was required.

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

I added a variable to describe the number of spaces between cells, instead of using hard-coded integers, but this covers the grid's output.

## Class methods

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

## List comprehension/2

The documentation for [nested list comprehensions](https://docs.python.org/3/tutorial/datastructures.html?highlight=comprehension#nested-list-comprehensions) actually described something very helpful in this regard: how to _transpose_ a matrix. The idea is to describe a grid through its columns, so to have easier access to the cells in order.

Let me repeat the "for loop" first, "list comprehension" later approach, just to understand the syntax.

With a for loop:

```py
# build grid
rows = 2
columns = 3
grid = [
  [1, 2, 3],
  [4, 5, 6]
]

grid_transposed = []

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

With a list comprehension, it might lead to some head-scratching, but it works as follows:

```py
grid_transposed = [[grid[r][c] for r in range(rows)] for c in range(columns)]
```

## Grid/3

Back once more to the grid, create the transposed structure using the rows and columns saved in the `__init__` method.

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

## reversed

The first, most obvious shortcoming is fixed by considering that the transposed grid reads top to bottom, and the goal is to add the items in reverse order.

To fix this, reverse the column as it is retrieved.

```py
grid_column = list(reversed(grid_transposed[column]))
```

It seems necessary to use the `list` function as `reversed` returns a [reverse iterator](https://docs.python.org/3/library/functions.html#reversed).

This leads to the correct index bottom to top, but it is then necessary to modify the value in the original grid, starting from the end of the grid.

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

## try except

The second issue relates to what happens when you add to a column that is already filled.

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

There are no longer empty spaces, and the `index` function returns a `ValueError`.

A `try...except` block allows to handle this error quite gracefully. The idea is to literally try something, in this instance finding the index of the empty space.

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

### Update

While the code works, it might be easier to read using `try`, `except` _and_ `else` block. Following the `else` statement, include the code which runs after the code that has been tried:

- `try` something

- if there is an error, cover it in the `except` block

- if no error is found, continue in the `else` block

```py
try:
  index = grid_column.index(" ")
except ValueError:
  print("Column unavailable")
else:
  self.grid[len(self.grid) - 1 - index][column] = input
```

Refer to the [docs for error handling](https://docs.python.org/3/tutorial/errors.html) for more information,

## Gameplay

With the grid class "complete", the next step is creating the game, and allowing to fill the grid following user input. I can think of at least another useful method in the class, to dictate whether four values match.

```py
def matches_four(self):
  return False
```

But I'd rather cover the interactions set up when the program is run,

For starters, I created a utility function to display a message almost as a header.

```py
def highlight_message(message):
    print()
    print("*" * len(message))
    print(message)
    print("*" * len(message))
    print()
```

Surrounded by two lines filled with asterisks. For an arbitrary message:

```py
highlight_message("Connect Four")

"""
************
Connect Four
************
"""
```

The game is set up in a function `run_game`, and with the following sequence:

- introduce the game

- set up the grid and display its structure

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

## Game Loop

In the game loop notify the current player and ask for which column to actually fill.

```py
print(f"Player: {player}")
column = input("Select column: ")
```

I decided to add an arbitrary condition to exit the game, by entering the letter `q`, but let's focus on the input itself. The idea is to handle a few errors:

- the input is not a number

- the input doesn't describe a viable column. This either because out of range, or because the column is already filled

The second error is a bit more challenging, so starting with the first.

## try except else

When you coerce a string into a number with the `int` function, you get an error if the input cannot be coerced.

- try

  ```py
  try:
      c = int(column)
  ```

- relate the specific error with the `highlight_message` function

  ```py
  except ValueError:
    highlight_message("**Enter a number**")
  ```

- continue with the input integer.

  ```py
  else:
    # consider column
  ```

### try except else/2

When selecting the column, I already covered a `ValueError`, when the column was already filled and the `.index(" ")` couldn't find the value in the list.

There might be an additional error however, when the selected column is not available at all. Outside of the grid's scope. This error materializes itself with a `IndexError`, and it can be covered in the `except` block by specifying both errors in between parenthesis.

```py
except (IndexError, ValueError):
    # handle errors
```

This error is handled in the `add_to_column` function, but since I plan to notify the user from the game loop, I decided not to include `print` statements in the grid class. Instead, the function is made to return `True` or `False` from the `try`, `except`, `else` block, and an `if` statement in the game loop handles the rest.

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

If `False`, notify the player of the error.

```py
else:
  highlight_message(f"**Column unavailable**")
```

## Victory

In the `matches_four()` function, the idea is to check for a victory after the grid is updated, but before the player is toggled.

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

In the body of the function we check for the matches. I fumbled a little with _how_ to do this, but eventually, I found a rather nifty approach using the `.index()` function.

Here's the idea:

- build a string for the current row, column, diagonals

- find if the string contains four instances of the current player. `RRRR` or `TTTT`

As seen earlier, `.index()` prompts an error if there's no such value, so a `try` `except` `else` block will be enough to cover the rest.

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

Notice I included an additional whitespace character, to avoid finding a match between the row and the column which follows.

For the column, instead of transposing the entire grid, I can build a list using a list comprehension, and the number of rows in the grid itself.

```py
current_column = [self.grid[index][column] for index in range(len(self.grid))]
```

It didn't come immediately, and it helped to build the list with a for loop first.

```py
current_column = []
rows = len(self.grid)
for index in range(rows):
  current_column.append(self.grid[index][column])
```

Either way, the values of the current column are added to the string exactly like with the current row.

```py
for cell in current_column:
    match += cell
match += ' '
```

The most challenging portion then, relates to adding the values for the diagonals.

## Victory/2

I picked up this project a couple of days from the previous update, and I decided to rewrite the way I consider the rows and columns before tackling the diagonals.

It is inefficient to consider the entire row/the entire column. To fix this issue, I use the `min` and `max` function to build a range of the appropriate values.

For the rows, and considering that a match consists of `4` values, consider up to three columns before/after the current one.

```py
c_min = max(0, column - 3)
c_max = min(self.columns, column + 3)
for c in range(c_max - c_min):
    match += self.grid[row][c + c_min]
```

Took me a while to grasp the logic, but divvying up the code with two additional variables helped.

For the column, the logic is repeated considering up to three cells before and after the current row.

```py
r_min = max(0, row - 3)
r_max = min(self.rows, row + 3)
for r in range(r_max - r_min):
  match += self.grid[r + r_min][column]
```

The grid is read top to bottom, but since we use a range, it is unnecessary to flip the dimensions.

Back to the diagonals, and the crux of this project, I actually found a solution in the for loop describing the row. I'll elaborate the idea, and try to describe the approach as clearly as possible.

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

For the approach: initialize three variables:

- `c_gap` to describe the distance from the current column

- `north_east` and `south_east` to store the values in the diagonals. Since the values are considered in the for loop for the row, its characters are included only after the for loop has considered its columns

In the for loop, I'll elaborate for one diagonal, but the logic is eerily similar for the other segment.

Consider if the row `c_gap` away is available. In other words, in the `0`, `self.rows` range.

```py
if row - c_gap >= 0 and row - c_gap < self.rows:
```

Add the value in said row, and in the column already described in the for loop.

```py
north_east += self.grid[row - c_gap][c + c_min]
```

For the other column, instead of subtracting `c_gap`, add the value. I might have flipped `south_east` with `north_east`, but it should make sense considering, one last time, that the grid reads top to bottom, and higher indexes relate to rows lower in the structure.
