# Connect Four Visuals

> Match shapes of the same color

## Links

- [python script](https://github.com/borntofrappe/python-scripts/tree/master/connect-four) creating the connect-four game in the terminal console. See [the matching REPL](https://repl.it/@borntofrappe/connect-four) for a live demo.

- [Tutorial](https://youtu.be/XGf2GcyHPhc?t=5705) on the [freecodecamp YouTube channel](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) inspiring the project.

  Inspiring, but once again not driving the project. This is a follow up to the mentioned python script, and I plan to try my best at developing the game before reviewing the video.

## Setup

Starting with a bit of setup, create a dictionary to describe the main variables of the window.

```py
game = {
    "caption": "Connect Four",
    "width": 500,
    "height": 400,
    "fill": (20, 20, 20),
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
