# Snake

> notes jotted down developing the project
>
> in increments

## Getting started

Begin by import `pygame` and `sys`. This last one to close the window when a particular key is pressed.

```py
import pygame
import sys

def run_game():
    pygame.init()
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    screen.fill((20, 20, 20))
    pygame.display.set_caption("Snake")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    sys.exit()

        pygame.display.flip()


run_game()
```

## Draw Grid

From here draw the grid using a hard coded number of columns and rows.

```py
def draw_grid(screen, width, height, columns, rows):
    w = width / columns
    h = height / rows
    for column in range(columns):
        x = column * w - 2
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, height), 2)
    for row in range(rows):
        y = row * h - 2
        pygame.draw.line(screen, (200, 200, 200), (0, y), (width, y), 2)
```

Notice the number of arguments behind the [draw line function](https://www.pygame.org/docs/ref/draw.html#pygame.draw.line).

In `run_game()` then, we call the function passing the necessary arguments. The screen is of particular interest, as it refers to the surface in which to draw.

```py
while True:
    draw_grid(screen, width, height, columns, rows)
```

## Time

[The video tutorial](https://youtu.be/XGf2GcyHPhc?t=2937) actually introduces a very useful technique with the `delay` function and `Clock` class. This is to slow down the rate at which the screen is re-drawn. To test these new features of the pygame library, let's draw a square which is updated at every iteration to move horizontally.

```py
def draw_snake(screen, x, y, w, h):
    pygame.draw.rect(screen, (40, 150, 40), (x, y, w, h))
```

Interestingly enough, [`pygame.draw.rect()`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect) uses the surface, the color and a [`Rect` object](https://www.pygame.org/docs/ref/rect.html#pygame.Rect)

This will be refined, but just to see the influence of the timing syntax, set up a variable to keep track of the horizontal position.

```py
def run_game():
    x = 0
    w = width / columns - 2
    h = height / rows - 2
    dx = width / columns
    dy = height / rows
```

`-2` to accommodate for the width of the line.

The in the game loop draw the snake.

```py
while True:
    x += dx
    if x >= width:
        x = 0
    draw_snake(screen, x, 0, w, h)
```

Notice how the coordinate is set back to `0` when reaching the width. It works, extremely fast, but the shape draw in the previous iteration is kept. This is becaused I failed to add the `screen.fill()` function in the game loop, and the background is drawn once.

```py
while True:
    screen.fill((20, 20, 20))
    x += dx
    if x >= width:
        x = 0
    draw_snake(screen, x, 0, w, h)
```

Incredibly fast again, but at least avoiding duplicates. To slow down, the aforementioned syntax:

- pygame.time.delay()

- clock.tick()

The [Clock object](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock) seems particularly useful, and the [`tick` function](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick) specifies the number of frames at which to limit the game. `clock.tick(10)` means the game won't run faster than 10 frames per second.

[`time.delay`](https://www.pygame.org/docs/ref/time.html#pygame.time.delay) seems to literally delay the action, by the number of milliseconds specified in between parenthesis.

```py
while True:
    pygame.time.delay(100)
    clock.tick(10)
    screen.fill((20, 20, 20))
```

## an Integer is required

A word of warning from the console: the coordinate `x` seems to actually describe a float. This is because `width / columns` provides a float, and this value is added to `x`. To fix this, use integer division instead.

```py
dx = width // columns
```

## Snake Class

Now that it works, it's better to rewrite the code to have a class for the snake.

```py
class Snake():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = (40, 150, 40)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

    def move(self, x, y):
        self.x = x
        self.y = y
```

Pretty clear at this point.

In the function we initialize the object and then draw the shape using `snake.draw()`

```py
def run_game():
    snake = Snake(0, 0, w, h)
    while True:
        snake.draw(screen)
```

## Direction

Instead of updating the position arbitrarily however, update the x or y coordinate according to the key selected by the player. I ended up using a tuple to describe the x and y increase at every iteration.

```py
class Snake():
    def __init__(self, x, y, w, h):
        self.is_moving = False
        self.direction = (1, 0)
```

The boolean allows to have the snake move following one of the arrow keys. `direction` dictates the increase through `1`, `0` and `-1` values. For the `x` and `y` coordinate respectively.

In the game loop specify the tuple matching the direction:

```py
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
        snake.is_moving = True
        snake.direction = (1, 0)
    if event.key == pygame.K_LEFT:
        snake.is_moving = True
        snake.direction = (-1, 0)
    if event.key == pygame.K_UP:
        snake.is_moving = True
        snake.direction = (0, -1)
    if event.key == pygame.K_DOWN:
        snake.is_moving = True
        snake.direction = (0, 1)
```

Seems a tad redundant to set the boolean to `True` every time.

Before drawing the snake then, update its position as long as the boolean dictates it so, and using the values described by the tuple.

```py
if snake.is_moving:
    x = snake.x + snake.direction[0] * dx
    y = snake.y + snake.direction[1] * dy
    if x > width:
        x = 0
    if x < 0:
        x = width - dx
    if y > width:
        y = 0
    if y < 0:
        y = height - dy
    snake.move(x, y)
```

...continues

<!-- ## COMING SOON -->
