import pygame
import sys
from random import randint


class Snake():
    def __init__(self, columns, rows, w, h):
        self.x = randint(0, columns - 1)
        self.y = randint(0, rows - 1)
        self.w = w
        self.h = h
        self.is_moving = False
        self.direction = (1, 0)
        self.color = (60, 200, 60)

    def draw(self, screen):
        x = self.x * self.w
        y = self.y * self.h
        pygame.draw.rect(screen, self.color, (x, y, self.w, self.h))

    def move(self, x, y):
        self.x = x
        self.y = y

    def overlaps(self, entity):
        return self.x == entity.x and self.y == entity.y

    def set_direction(self, x, y):
        self.direction = (x, y)


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

    def overlaps(self, entity):
        return self.x == entity.x and self.y == entity.y


class Fruit():
    def __init__(self, columns, rows, w, h):
        self.x = randint(0, columns - 1)
        self.y = randint(0, rows - 1)
        self.w = w
        self.h = h
        self.color = (200, 50, 50)

    def draw(self, screen):
        x = self.x * self.w
        y = self.y * self.h
        pygame.draw.rect(screen, self.color, (x, y, self.w, self.h))


def draw_grid(screen, width, height, columns, rows):
    stroke_width = 1
    w = width // columns
    h = height // rows
    for column in range(columns):
        x = column * w
        pygame.draw.rect(screen, (200, 200, 200),
                         (x, 0, w, height), stroke_width)
    for row in range(rows):
        y = row * h
        pygame.draw.rect(screen, (200, 200, 200),
                         (0, y, width, h), stroke_width)


def run_game():
    pygame.init()
    width = 500
    height = 500
    columns = 20
    rows = 20

    w = width // columns
    h = height // rows

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake = Snake(columns, rows, w, h)
    fruit = Fruit(columns, rows, w, h)
    appendages = []

    while True:
        pygame.time.delay(100)
        clock.tick(10)
        screen.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_RIGHT:
                    snake.is_moving = True
                    snake.set_direction(1, 0)
                if event.key == pygame.K_LEFT:
                    snake.is_moving = True
                    snake.set_direction(-1, 0)
                if event.key == pygame.K_UP:
                    snake.is_moving = True
                    snake.set_direction(0, -1)
                if event.key == pygame.K_DOWN:
                    snake.is_moving = True
                    snake.set_direction(0, 1)

                if event.key == pygame.K_SPACE:
                    snake.is_moving = False

                if event.key == pygame.K_n:
                    fruit = Fruit(columns, rows, w, h)

        if snake.overlaps(fruit):
            fruit = Fruit(columns, rows, w, h)
            if len(appendages) == 0:
                appendage = Appendage(snake.x, snake.y, w, h)
                appendages.append(appendage)
            else:
                appendage = Appendage(
                    appendages[len(appendages) - 1].x, appendages[len(appendages) - 1].y, w, h)
                appendages.append(appendage)

        if snake.is_moving:
            if len(appendages) > 0:
                for i in range(len(appendages) - 1, 0, -1):
                    appendages[i].move(appendages[i - 1].x,
                                       appendages[i - 1].y)
                appendages[0].move(snake.x, snake.y)

            x = snake.x + snake.direction[0]
            y = snake.y + snake.direction[1]
            if x > columns - 1:
                x = 0
            if x < 0:
                x = columns - 1
            if y > rows - 1:
                y = 0
            if y < 0:
                y = rows - 1
            snake.move(x, y)

        for appendage in appendages:
            if snake.overlaps(appendage):
                snake.is_moving = False
                appendages.clear()
            if appendage.overlaps(fruit):
                fruit = Fruit(columns, rows, w, h)

        draw_grid(screen, width, height, columns, rows)
        fruit.draw(screen)
        snake.draw(screen)
        for appendage in appendages:
            appendage.draw(screen)

        pygame.display.flip()


run_game()
