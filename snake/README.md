# [Snake](https://repl.it/@borntofrappe/snake)

> notes jotted down developing the project, without much rhyme, but hopefully enough reason

## Screen

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

## Grid

Draw the grid using a hard coded number of columns and rows. Here I use a function to which I pass the surface on which to draw, plus the values to create the grid in the game's window.

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

In `run_game()` then.

```py
while True:
    draw_grid(screen, width, height, columns, rows)
```

## Time

[The video tutorial](https://youtu.be/XGf2GcyHPhc?t=2937) actually introduces a very useful technique with the `delay` function and `Clock` class. This is to slow down the rate at which the screen is updated. To test these new features of the pygame library, draw a square which is updated at every iteration to move horizontally.

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

In the game loop then draw the snake.

```py
while True:
    x += dx
    if x >= width:
        x = 0
    draw_snake(screen, x, 0, w, h)
```

Notice how the coordinate is set back to `0` when reaching the width. It works, extremely fast, but the shape draw in the previous iteration is kept. This is because I forgot to add the `screen.fill()` function in the game loop, and the background is drawn once.

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

## DeprecationWarning

A word of warning from the console: the coordinate `x` seems to actually describe a float. This is because `width / columns` provides a float, and this value is added to `x`. To fix this, use integer division instead.

```py
dx = width // columns
```

## Snake

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

Instead of updating the position arbitrarily and at every frame, update the x or y coordinate according to the key selected by the player. I ended up using a tuple to describe the x and y increase at every iteration.

```py
class Snake():
    def __init__(self, x, y, w, h):
        self.is_moving = False
        self.direction = (1, 0)
```

The boolean allows to have the snake move only after a specific action is taken. `direction` dictates the increase through `1`, `0` and `-1` values. For the `x` and `y` coordinate respectively.

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

# Fruit

A class to describe the objects picked up by the snake.

First off, I decided to set up a variable describing the width of the grid's stroke. It became rather inconvenient to leave the hard coded `2` around the script. I'm still figuring out the best way to avoid cropping the edges, but this makes for more readable code.

```py
stroke_width = 2

class Snake():
    def __init__(self, x, y, w, h):
        self.x = x + stroke_width
        self.y = y + stroke_width
        self.w = w - stroke_width
        self.h = h - stroke_width
        # ...
```

For the fruit, the class is similar to the snake, but uses the `randint` function from the `random` module, to position the square somewhere on the grid.

```py
class Fruit():
    def __init__(self, columns, rows, w, h):
        self.w = w - stroke_width
        self.h = h - stroke_width
        self.x = randint(0, columns) * w + stroke_width
        self.y = randint(0, rows) * h + stroke_width
        self.color = (180, 40, 40)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
```

In the `run_game` function then.

```py
def run_game():
    fruit = Fruit(columns, rows, w, h)

while True:
    fruit.draw(screen)
    snake.draw(screen)
```

The fruit is drawn before the snake to have this last one on top, were the two overlap.

I thought of adding a list for the pieces of fruits, but using a single variable might be feasible. Testing with an arbitrary key.

```py
if event.key == pygame.K_n:
    fruit = Fruit(columns, rows, w, h)
```

The red square is repositioned elsewhere on the grid. As long as there is supposed to be a single piece, a variable will suffice.

## Overlap

I thought of rewriting the classes to have `x` and `y` refer to the columns and rows instead of actual coordinates, but let's stick with the values for the time being.

In the game loop.

```py
if snake.overlaps(fruit):
    fruit = Fruit(columns, rows, w, h)
```

In the snake class.

```py
class Snake():
    def overlaps(self, fruit):
        return self.x == fruit.x and self.y == fruit.y
```

It works, but requires a few adjustments. For starters, using the `stroke_width` only when the shapes are initialized produces the wrong coordinates when the snake crosses the window's edges.

```diff
if x > width:
-    x = 0
+    x = stroke_width
```

The biggest hassle however, is that the piece of fruit is not always displayed. This is because it can be positioned to the right and bottom of the grid.

```diff
- self.x = randint(0, columns) * w + stroke_width
+ self.x = randint(0, columns - 1) * w + stroke_width
```

Using `x` and `y` relative to the grid might be a good idea.

## Grid x and y

I decided to update the `x` and `y` values with the suggested dimensions of the grid. It required a bit of find and replace, but essentially it boils down to:

- remove `dx` and `dy`

- define `x` as `randint(0, columns - 1)`, `y` as `randint(0, rows - 1)`

- draw the snake considering the coordinates, but also the size of the columns and rows. Coincidentally, the width/height of the snake.

```py
def draw(self, screen):
    x = self.x * self.w
    y = self.y * self.h
    pygame.draw.rect(screen, self.color, (x, y, self.w, self.h))
```

## stroke_width

In trying to center the rectangles in the squares of the grid, I decided to ditch the `draw.line` function and instead repeat the rectangular shape.

This means the grid lines are thicker, but at least the shapes don't stretch/overlap the edges of the grid cells.

```py
def draw_grid(screen, width, height, columns, rows):
    stroke_width = 1
    w = width // columns
    h = height // rows
    for column in range(columns):
        x = column * w
        pygame.draw.rect(screen, (200, 200, 200),
                         (x, 0, w, height), stroke_width)
    # similar considerations for the rows

```

## set_direction

Almost forgot. Instead of assigning a tuple on the `direction` of the snake directly, I created a setter function.

```py
def set_direction(self, x, y):
    self.direction = (x, y)
```

## Appendage(s)

The challenge in how to have successive shapes move where the previous one was. To this end, I use a list to store the different parts of the snake.

I created a separate class for this collection, but I might go back and revisit the code's structure.

```py
class Appendage():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = (40, 150, 40)

    def draw(self, screen):
        x = self.x * self.w
        y = self.y * self.h
        pygame.draw.rect(screen, self.color, (x, y, self.w, self.h))

    def move(self, x, y):
        self.x = x
        self.y = y
```

Similar to the snake, it is set up with a width, height, and a definite position. Unlike the snake however, it is not supposed tp move on its own. so there's no boolean dictating whether or not it should move, or the tuple describing the direction.

In `run_game` set up a list to collect the different parts.

```py
def run_game():
    appendages = []
```

When the snake overlaps with the fruit then, create a new instance of the appendage class. First off, using the coordinates of the snake.

```py
if snake.overlaps(fruit):
    appendage = Appendage(snake.x, snake.y, w, h)
    appendages.append(appendage)
```

To show the shape, draw the objects using the familiar `draw` function.

```py
fruit.draw(screen)
snake.draw(screen)
for appendage in appendages:
    appendage.draw(screen)
```

To actually move them however, update the block where the snake's movement is described.

```py
if snake.overlaps(fruit):
    # add appendage

if snake.is_moving:
    # update appendage
    # update snake
```

The position of the block, and the order of the update functions, matters a lot. This is because I want to:

- create the appendage

- update the position of the appendages on the basis of the snake

- update the snake on the basis of the chosen direction

In that specific order.

```py
if snake.is_moving:
    if len(appendages) > 0:
        appendage[0].move(snake.x, snake.y)

    # update snake
```

This works, but only for the first appendage. For later appendages, restructure the code to refer not to the snake, but previous instances of the appendage class.

In the overlapping if statement.

```py
if snake.overlaps(fruit):
    fruit = Fruit(columns, rows, w, h)
    # refer to the snake
    if len(appendages) == 0:
        appendage = Appendage(snake.x, snake.y, w, h)
        appendages.append(appendage)
    # refer to previous appendages
    else:
        appendage = Appendage(
            appendages[len(appendages) - 1].x, appendages[len(appendages) - 1].y, w, h)
        appendages.append(appendage)
```

In the moving if statement.

```py
if snake.is_moving:
    if len(appendages) > 0:
        for i in range(len(appendages) - 1, 0, -1):
            appendages[i].move(appendages[i - 1].x,
                                appendages[i - 1].y)
        appendages[0].move(snake.x, snake.y)

    # update snake
```

Traverse the list backwards, again because order matters. Looping in ascending order would mean you'd overwrite the coordinates and end up with the appendages on top of each other.

## Overlap/2

The game ends if the snake overlaps with an appendage. The `overlaps()` function actually helps. I updated the name of the input argument, but it's fundamentally the same.

```py
def overlaps(self, entity):
    return self.x == entity.x and self.y == entity.y
```

Later in the game loop.

```py
for appendage in appendages:
    if snake.overlaps(appendage):
        snake.is_moving = False
        appendages.clear()
```

Stop the snake and for good measure remove the existing appendages.

Surprisingly enough, it all works.

## Overlap/3

Testing the game, I realized there is a situation in which the appendages overlap with the fruit, hiding it from view. Instead of creating modifying the fruit class to initialize the shape where the snake is not, I can actually detect the overlap and add a new instance.

```py
for appendage in appendages:
    if appendage.overlaps(fruit):
        fruit = Fruit(columns, rows, w, h)
```

Just need to specify the function on the appendage class. This might warrant a whole discussion on the classes, their structure and possible inheritance.
