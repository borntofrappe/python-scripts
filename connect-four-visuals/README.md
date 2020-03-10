# Connect Four Visuals

> Match shapes of the same color

## Links

- [python script](https://github.com/borntofrappe/python-scripts/tree/master/connect-four) creating the connect-four game in the terminal. See [the matching REPL](https://repl.it/@borntofrappe/connect-four) for a live demo.

- [Tutorial](https://youtu.be/XGf2GcyHPhc?t=5705) on the [freecodecamp YouTube channel](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) inspiring the project.

  Inspiring, but once again not driving the project. This is a follow up to the mentioned python script, and I plan to try my best at developing the game before reviewing the video.

## Setup

Starting with a bit of setup, create a dictionary to describe the main variables of the window.

```py
game = {
    "caption": "Connect Four",
    "width": 500,
    "height": 400,
    "fill": (10, 10, 10),
}
```

In terms of modules, the script uses `pygame`, and also the `sys`, to quit the program following a selection of events.

```py
import pygame
import sys
```

In terms of logic, it is scoped to a dedicated function.

```py
def run_game():
```

Which sets up the window and then a loop for the game loop.

For the window, a few pygame specific methods create a screen with the hard-coded values.

```py
pygame.init()
pygame.display.set_caption(game["caption"])
screen = pygame.display.set_mode((game["width"], game["height"]))
```

In a game loop, the screen is updated with the matching method.

```py
def run_game():
  # setup

  while True:
      # draw
      screen.fill(game["fill"])
      #update
      pygame.display.update()
```

Before moving on to drawing circles, I choose to bind a couple of events to quit the game.

```py
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        sys.exit()

  # draw and update
```

## Circle

In terms of visual, the game relies heavily on circles:

- a circle to represent the player selection

- a grid of circles to describe the grid of the connect four game

The first one is supposed to move horizontally, and above the latter structure. The circles of this last structure however, are not meant to move. As always, however, one step at a time.

```py
class Circle:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r
```

Set up with three values describing the position and size of the shape, the class draws a circle with the `pygame.draw.circle` function.

```py
def draw(self, screen):
  pygame.draw.circle(screen, (180, 180, 180), (self.cx, self.cy), self.r)
```

Just remember to:

1. initialize the circle in the `run_game` function

   ```py
   def run_game():
     circle = Circle(100, 100, 20)
   ```

1. draw the shape _after_ the fill of the window.

   ```py
   while True:
     circle.draw(screen)

   ```

The coordinates is a topic of future sections, but first, a word on the radius: to avoid any cropping, consider the space that would be occupied by the grid of circles. With given columns and rows + 1. This to account for the extra row.

```py
rows = 5
columns = 5

r = min(int(game["width"] / (columns * 2)), min(int(game["height"] / ((rows + 1) * 2))))
```

## Circles

The movable circle is position at the top of the screen, repeating the radius for all three values.

```py
circle_input = Circle(r, r, r)
```

This ensures the shape is positioned in the top left corner.

Since the shape is supposed to move following the cursor, the class is expanded with a setter function.

```py
def set_cx(self, cx):
  self.cx = cx
```

Setter function which is then invoked in the game loop, and following the `MOUSEMOTION` event.

```py
if event.type == pygame.MOUSEMOTION:
```

pygame gives the coordinate of the cursor through the `get_pos` function. It returns a tuple of integers, but I'm only interested in the horizontal dimension.

```py
if event.type == pygame.MOUSEMOTION:
  cx = pygame.mouse.get_pos()[0]
  circle_input.set_cx(cx)
```

To avoid cropping, you can also update the coordinate in a safe range. Say `[r, width - r]`.

```py
if event.type == pygame.MOUSEMOTION:
  cx = pygame.mouse.get_pos()[0]
  if cx > r and cx < game["width"] - r:
    circle_input.set_cx(cx)
```

While the circle moves horizontally, it is also necessary to change its vertical coordinate.

```py
def set_cy(self, cy):
  self.cy = cy
```

I haven't worked with the mouse object before, so I'll start with a hard-coded measure to have the circle positioned at the bottom of the screen.

```py
if event.type == pygame.MOUSEBUTTONDOWN:
    circle_input.set_cy(game["height"] - r)
```

This raises an interesting point however. Once positioned at the bottom of the grid, the circle is no longer supposed to move horizontally. Here's an idea though. Instead of adding a boolean to move the circle conditionally, and since the game is supposed to ask for input more than once, it might actually be more efficient to just create a new instance of the class, and position it where desired.

Create a list for the circles eventually plotted in the grid.

```py
circles = []
```

When the cursor is clicked, append a new instance at the bottom of the window, and considering the horizontal coordinate of the input.

```py
if event.type == pygame.MOUSEBUTTONDOWN:
    cx = circle_input.cx
    cy = game["height" - r]
    circle = Circle(cx, cy, r)
    circles.append(circle)
```

Then loop through the list and draw the immovable shapes.

```py
for circle in circles:
  circle.draw(screen)
```

It works, but following the example of a setter function, it might actually be better to have a dedicated method returning the `cx` coordinate of the circle.

```py
def get_cx(self):
  return self.cx
```

Before moving on to the grid of circles, in which these shapes are then supposed to be slotted, a word on the color. It didn't occur to me until now, but the `Circle` class should also have a fourth variable describing the color. In the game function then, this color should be flipped for each new click event.

I considered a couple of solutions, for instance describing the colors in the `game` dictionary, but decided instead to add the color and possible colors in the `Circle` class itself.

```py
class Circle:
    def __init__(self, cx, cy, r, color, colors=[(180, 30, 30), (180, 180, 30)]):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.color = color
        self.colors = colors
```

The idea is to provide `colors` as a list of two tuples, with two color combinations (see default value). Then and with a toggle function, the value is updated picking between the alternative hue.

```py
def toggle_color(self):
  if self.color == self.colors[0]:
    self.color = self.colors[1]
  else:
    self.color = self.colors[0]
```

It is actually elegant how these values and functions are used in the `run_game` function.

Set up the desired values (the default was included mostly to illustrate the point of the class).

```py
def run_game():
  # previous code

  colors = [(180, 30, 30), (180, 180, 30)]

```

Initialize the input circle with one of the two.

```py
def run_game():
  # previous code
  colors = [(180, 30, 30), (180, 180, 30)]

  circle_input = Circle(r, r, r, colors[0], colors)
```

When the mouse is pressed, retrieve the color of the input circle, and use it for the new shape in the `circles` list.

This means the class should also have a `get_color` method, returning the matching value.

```py
def get_color(self):
  return self.color
```

Back in the function, and following the `MOUSEBUTTONDOWN` event, include the additional arguments.

```py
if event.type == pygame.MOUSEBUTTONDOWN:
  cx = circle_input.get_cx()
  color = circle_input.get_color()
  cy = game["height"] - r

  circle = Circle(cx, cy, r, color, colors)
```

And toggle the color of the movable shape.

```py
if event.type == pygame.MOUSEBUTTONDOWN:
  cx = circle_input.get_cx()
  color = circle_input.get_color()
  cy = game["height"] - r

  circle = Circle(cx, cy, r, color, colors)
  circle_input.toggle_color()
```

It is perhaps superfluous, but the colors can also be retrieved setting up an additional method.

```py
def get_colors(self):
  return self.colors
```

I say superfluous since the list of tuples is set up earlier in the function.

## Grid

Picking up from [the previous project](https://github.com/borntofrappe/python-scripts/tree/master/connect-four) creating a game of connect four in the terminal, I can actually use most of the code developed in that script.

In the terminal you end up using two letters to describe the cells, `R` and `T`, and I can actually retain the logic in this more visual take on the game. The issue becomes then how to reconcile the ASCII grid to the circles on screen.

First, set up the grid.

```py
grid = Grid(columns, rows)
```

In the game loop then, loop through the grid and draw one circle for each cell. This is actually where I realized that the `circles` list is unnecessary. Consider in pseudo code: loop through the grid:

```py
for cell in grid:
```

Draw a circle with a default color:

```py
for cell in grid:
  color = (50, 50, 50)
  pygame.draw.circle(screen, color, ...)
```

Change the color depending on the cell's own value

```py
for cell in grid:
  color = (50, 50, 50)
  if cell == "R":
    color = (180, 30, 30)
  elif cell == "Y":

  pygame.draw.circle(screen, color, ...)
```

I ended up using `R` and `Y` to match the red and yellow colors, but the substance remains the same. This also fixes the nagging issue of drawing the un-colored circles. There's no need to duplicate the grid to show the underlying structure.

There are few more considerations in the coordinates of the circle, but let me elaborate more on this approach. The loop takes care of drawing the circle, but following the `MOUSEBUTTONDOWN` event, we need a way to update the specific cell with the desired letter. Luckily, the `add_to_column` function is already equipped to return the cell for a selected column. All that is required is figuring out _where_ that column is.

## Draw Grid

The `Grid` class is expanded with another method, `get_grid`, which returns a flattened version of the 2D list. The idea is to have, for each cell, a dictionary describing the row, column, and character value.

```py
cell = {
  "value": "R",
  "column": 0,
  "row": 1
}
```

To this end, I loop through the rows and column appending the desired values to a list.

```py
grid = []
for row in range(self.rows):
    for column in range(self.columns):
      cell = {
          "value": self.grid[row][column],
          "column": column,
          "row": row
      }
      grid.append(cell)
```

Which is then returned.

```py
return grid
```

In the game loop, I then draw the cells with the desired color (currently the default one).

```py
for cell in grid.get_grid():
  color = (40, 40, 40)
  if cell["value"] == "R":
    color = colors[0]
  elif cell["value"] == "Y":
    color = colors[1]

  pygame.draw.circle(screen, color, (r, r), r)
```

The circles are drawn, but every shape is positioned in the top left corner, at the coordinates `(r, r)`.

This is where a bit of adjustment is required. To draw the grid, you can use the value saved under the `row` and `column` key.

```py
cx = cell["column"] * (r * 2)
cy = cell["row"] * (r * 2)
pygame.draw.circle(screen, color, (cx, cy), r)
```

Radius times two to neatly separate the circles diameter by diameter.

This works, but crops the grid on the left and top of the screen. Moreover, the first row overlaps with the input circle.

First, to avoid cropping, add the measure of the radius to both variables.

```py
cx = cell["column"] * (r * 2) + r
cy = cell["row"] * (r * 2) + r
```

This for the same reason `circle_input` is initialized with the `(r, r)` coordinates. `pygame.draw.circle` uses the values for the _center_ of the shape.

For the row then, consider the number of the row plus one. Plus one to skip the row occupied by the input itself.

```py
cy = (cell["row"] + 1) * (r * 2) + r
```

## Offset Grid

The grid is successfully drawn with the circles one next to the other. Unfortunately, it doesn't work for every grid. It works perfectly when the grid has `n` columns and `n - 1` rows, since the space is fully occupied by the grid and the extra row for the input. For other combinations however, the grid occupies a smaller area.

One solution to this problem is finding the extra width or height, and add that measure to the grid as to center the structure on screen. I previously considered offsetting the circles, similarly to how you justify the text of a paragraph, but I'd rather offset the entire grid and keep the circles close to one another.

For the extra width and height:

1. consider the space occupied by the columns and row of circles with a radius `r`

   ```py
   grid_width = columns * (r * 2)
   grid_height = row * (r * 2)
   ```

1. subtract the measure from the width and height of the screen.

   ```py
   offset_x = game["width"] - grid_width
   offset_y = game["height"] - grid_height
   ```

1. halve the measure to keep as much space left and right of the grid. This making sure to return an integer value, with the `//` double slash operator or the `int()` function.

   ```py
   offset_x = (game["width"] - grid_width) // 2
   offset_y = int((game["height"] - grid_height) / 2)
   ```

   Just pick one.

1. add the measure to the `cx` and `cy` coordinates.

   ```py
   cx = cell["column"] * (r * 2) + r + offset_x
   cy = cell["column"] * (r * 2) + r + offset_y
   ```

It works, almost. The grid is cropped at the bottom, with only half of the last row visible on the screen. This is because the height doesn't take into consideration, yet, that the first row is already occupied by the input circle.

```diff
- offset_y = int((game["height"] - grid_height) / 2)
+ offset_y = int((game["height"] - (r * 2) - grid_height) / 2)
```

Cool. One last touch though. The grid is now centered, in both dimensions. If you'd want to position the structure at the bottom of the screen, you'd have to modify the vertical offset.

```diff
- offset_y = int((game["height"] - (r * 2) - grid_height) / 2)
+ offset_y = int((game["height"] - (r * 2) - grid_height))
```

A matter of preference.

## Add to column

The grid is drawn and centered, but currently doesn't change in color. This is fixed in the `if` statement reacting to the `MOUSEBUTTONDOWN` event.

Previously, I added a circle to a list, using the coordinate of the input circle. Here, we need instead to retrieve the column matching the coordinate. The `add_to_column` function developed in the [previous script]() already takes care of adding a specific letter to the grid, if possible. This means much of the hard work is already done in the `Grid` class.

- initialize a variable for the player

  ```py
  player = "R"
  ```

- in the game loop, retrieve the horizontal coordinate of the input circle.

  ```py
  cx = circle_input.get_cx()
  ```

  It is actually equivalent to use the mouse object and the `get_pos()` function, since the shape matches the cursor in value.

- if the coordinate falls within the range described by the grid (consider the horizontal offset)

  ```py
  if cx > offset_x // 2 and cx < game["width"] - offset_x // 2:
  ```

- compute the column considering the diameter of the circles themselves

  ```py
  column = (cx - offset_x) // (r * 2)
  ```

  The offset is removed to consider only the space occupied by the grid.

Luckily, the `add_to_column` function is already equipped to add the letter to the column. Moreover, it returns the coordinates of this cell, which can be then used to find a possible match.

```py
cell = grid.add_to_column(column, player)
if cell:
  # consider a match
```

The logic is copy-pasted from the previous project. Find a possible match:

```py
column, row = cell
if grid.matches_four(column, row, player):
  # game over
  # do something
```

Past the game over check, update the player and toggle the appearance of the input circle.

```py
if player == "R":
  player = "Y"
else:
  player = "R"

circle_input.toggle_color()
```

## Game over

Instead of adding text describing the winning player, I opted to add a boolean describing a `game_over` state.

Set to false in the `run_game` function, it is flipped to true in the `if` statement describing the match.

```py
column, row = cell
if grid.matches_four(column, row, player):
  game_over = True
```

And it is then used at the root of the `MOUSEBUTTONDOWN` event.

```py
if event.type == pygame.MOUSEBUTTONDOWN:
  if game_over:
    grid.clear()
    game_over = False

  else:
    # play
```

The `grid.clear()` function re-initializes the grid so that every cell is stripped of its existing values. This allows to play the game from the beginning.

## Player & color

There might be a better way to combine the player and color values, but I opted to use a dictionary using the player as the key, the tuples as the values.

```py
player = "R"
colors = {
    "R": (180, 30, 30),
    "Y": (180, 180, 30)
}
```

The circle input is always initialized with a list of colors.

```py
circle_input = Circle(r, r, r, colors[player], [colors["R"], colors["Y"]])
```

And the circlea are drawn using the color matching the value of the individual cell.

```py
color = (40, 40, 40)
  if cell["value"] != " ":
    color = colors[cell["value"]]
```

## Color

Thinking it through, I decided to ditch the `player` variable, and focus on the color instead. This required a few updates all throughout the script, but honestly, I think it was worth it.

First off, update the `Circle` class with a getter function for the list of colors.

```py
def get_colors(self):
  return self.colors
```

In the grid class, include two new variables in `color_default` and `colors`. The first one is used to initialize the grid with a default tuple. The second one is used to alternate between values.

the color of the individual circle as well as its possible color values. Instead of initializing the grid with empty spaces then, use the tuple for

```py
def __init__(self, columns, rows, color_default, colors):
  self.columns = columns
  self.rows = rows
  self.color = color
  self.colors = colors
  self.grid = [[color_default for c in range(columns)] for r in range(rows)]
```

Since the grid contains a tuple, a few more adjustments are required elsewhere in the class.

- in the `__str__` function, since I plan to keep the ASCII structure, use the value of the individual cells to populate the grid with `R` and `Y` characters.

  ```py
  for row in self.grid:
    grid += "|"
    for cell in row:
        char = " "
        if cell == self.colors[0]:
            char = "R"
        elif cell == self.colors[1]:
            char = "Y"
        grid += char.center(spaces, " ") + "|"
    grid += "\n"
  ```

- in the `get_grid` function, but this is more of an aesthetic change, populate the grid using a key of `color` instead of `value`

  ```diff
  cell = {
  -  "value": self.grid[row][column],
  +  "color": self.grid[row][column],
  }
  ```

- in the `clear` function, reinitialize the grid with the default value

  ```diff
  - self.grid = [[" " for c in range(self.columns)] for r in range(self.rows)]
  + self.grid = [[self.color_default for c in range(self.columns)] for r in range(self.rows)]
  ```

- in the `matches_four` function, and this is likely the biggest change, update the arguments to receive a color.

  When checking the row, diagonals and column then, convert the tuples to strings.

  ```diff
  - match += self.grid[row][c + c_min]
  + match += str(self.grid[row][c + c_min])
  ```

There might be other changes in the class, but they relate mostly to update the label `player` to be `color`, and to wrap the tuples in the `str` function when comparing the color values.

With the updated class, the `run_game` function can make due without a `player` variable.

- initialize the grid with the defaul color and list of possible color values

```py
color_default = (40, 40, 40)
grid = Grid(columns, rows, color_default, colors)
```

When drawing the cells, simply use the `color` property from the dictionary describing the cell.

```py
for cell in grid.get_grid():
    color = cell["color"]
```

When modifying the grid following the `MOUSEBUTTONDOWN` event, add the tuple describing the input circle instead of the previous characters.

```py
color = circle_input.get_color()
cell = grid.add_to_column(column, color)
```

As mentioned at the beginning of the section, it takes a few adjustments to reach this point, but we now have a grid populated by tuples, and these tuples are directly used to color the different shapes.

## Circle

A minor tweak to the syntax: since there is just one instance of the `Circle` class, I decided to rename `circle_input` as simply `circle`.

## Game over/2

To highlight that one of the two colors reached a match, I finally decided to update the `clear` method with an optional argument.

```py
if grid.matches_four(column, row, color):
  grid.clear(keep=color)
```

The idea is to clear the grid of any color, except the one specified in the function call. This means that, when a game over is detected, the grid can be cleared of the losing hue, highlighting the winning set.

```py
def clear(self, keep=""):
  for row in range(self.rows):
    for column in range(self.columns):
      if self.grid[row][column] != keep:
        self.grid[row][column] = self.color_default
```

I decided to use a [keyword argument](https://docs.python.org/3/glossary.html#term-parameter) more out of novelty than practical considerations. It does explain the purpose of the additional value with more clarity though.

## Bug Report

Testing the project with different values for the rows and columns, more specifically when there were more rows than columns, I found a bug in the `if` statement checking the horizontal coordinate of the input circle.

```py
if cx > offset_x // 2 and cx < game["width"] - offset_x // 2:
  # add to column
```

Here I check if the coordinate falls in the grid, but I failed to account that `offset_x` already considers half of the space around the grid.

```diff
-  if cx > offset_x // 2 and cx < game["width"] - offset_x // 2:
+ if cx > offset_x + r and cx < game["width"] - offset_x:
```

Halving the measure again would result in a quirky bug, whereby clicking the cursor just before the grid would highlight column `-1`, and pick the last column of the grid. Clicking just after the column would highlight column `columns + 1` and do nothing instead (see the `try` block in the `add_to_column` function).
