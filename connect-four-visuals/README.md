# Connect Four Visuals

> Match shapes of the same color

## Links

- [python script](https://github.com/borntofrappe/python-scripts/tree/master/connect-four) creating the connect-four game in the terminal console. See [the matching REPL](https://repl.it/@borntofrappe/connect-four) for a live demo.

- [Tutorial](https://youtu.be/XGf2GcyHPhc?t=5705) on the [freecodecamp YouTube channel](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) inspiring the project.

  Inspiring, but once again not driving the project. This is a follow up to the mentioned python script, and I plan to try my best at developing the game before reviewing the video.

## Setup

First, set up the game loop to show a window with a solid background and a hard-coded title.

```py
import pygame
import sys

game = {
    "caption": "Connect Four",
    "width": 500,
    "height": 400,
    "fill": (25, 20, 22),
}
```

I'm a bit rusty with pygame, so I'll take it one step at a time. In a function eventually describing the game loop.

```py
def run_game():
```

Set up the pygame screen

```py
pygame.init()
pygame.display.set_caption(game["caption"])
screen = pygame.display.set_mode((game["width"], game["height"]))
```

In the game loop then, update the display and fill the screen with the hard-coded tuple.

```py
def run_game():
  # setup

  while True:
      # draw
      screen.fill(game["fill"])
      #update
      pygame.display.update()
```

Before moving on to drawing the grid and game assets, bind a couple of events to quit the game.

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

## Draw

Split the window in two rows:

- input row, displaying a circle which can be moved left and right with the mouse event (and possibly in a future update with the arrow keys as well)

- output row, displaying the grid of circles in which, eventually, the input is supposed to be slotted

This means that, given a grid of `n` rows, the radius of the circle is capped at `height / (n + 1)`.

There might be a better way to add padding, but I'll also add a hard-coded measure to give some space across the height.

A similar reasoning applies to the width, but since the height is smaller in value, it relates more to the position of the circles than their size. Just to be safe however, consider the minimum between the two.

```py
size = min(game["width"], game["height"])
rows = 6
columns = 6
padding = 20

r = (size - padding) // (rows * 2 + 1)
```

I use hard-coded values to just draw the circles, but it might be better to create a class describing the input. As a proof of concept however, I'm only interested in drawing a circle in the top left corner.

```py
cx = r
cy = r

while True:
  # event bindings

  # draw
  screen.fill(game["fill"])
  pygame.draw.circle(screen, (0, 0, 0), (cx + padding // 2, cy + padding // 2), r)

  # update
```

## Circle && Input

Before moving on to draw the grid, I'll start by refactoring the input in a class. This to also incorporate the mouse event to reposition the circle at the top of the window.

```py
class Circle:
  def __init__(self, cx, cy, r):
    self.cx = cx
    self.cy = cy
    self.r = r

  def draw(self, screen, padding):
        pygame.draw.circle(screen, (180, 180, 180), (self.cx + padding // 2, self.cy + padding // 2), self.r)
```

In the `run_game()` function than simply initialize a circle

```py
def run_game():
  circle_input = Circle(r, r, r)
```

And draw the shape using the matching function.

```py
while True:
  circle_input.draw(screen, padding)
```

To reposition the circle, first create a function to set `cx`. This since the input is supposed to move only horizontally.

```py
def set_cx(self, cx):
  self.cx = cx
```

In the game loop then, listen to the `MOUSEMOTION` event

```py
if event.type == pygame.MOUSEMOTION:
```

Retrieve the mouse coordinates with the `get_pos` function. It returns a tuple of integers, but I'm only interested in the horizontal dimension.

```py
cx = pygame.mouse.get_pos()[0]
```

Finally, update the position of the input.

```py
circle_input.set_cx(cx)
```

As a small refinement, the position of the input is can updated in the `[padding // 2 + radius, width - padding // 2 - radius]` range, to avoid cropping the shape.

```py
if cx > padding // 2 + r and cx < game["width"] - padding // 2 - r:
  circle_input.set_cx(cx)
```

It works, but not as intended. This is because the padding is incorporated in the `draw` function, so the horizontal coordinate should keep track of that measure. I mentioned a dislike toward the way I include whitespace, so I'll remove the `padding` variable for the time being.

```py
if cx > r and cx < game["width"] - r:
  circle_input.set_cx(cx)

```

To be honest, it might actually be unnecessary to specify whitespace for the input circle, so this doesn't feel like a downgrade too much.

Back to the logic of the game, the class benefits from a `set_cy` function as well, to position the circle in the grid below.

```py
def set_cy(self, cy):
  self.cy = cy
```

Since I haven't worked with the mouse object before, I'll start with a hard-coded measure to have the circle positioned at the bottom of the screen when the mouse is clicked.

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

It works, but in the spirit of having a setter function, it might actually be better to have a dedicated method returning the `cx` coordinate of the circle.

```py
def get_cx(self):
  return self.cx
```

Up Next: building the eventual grid of inevitable circles
