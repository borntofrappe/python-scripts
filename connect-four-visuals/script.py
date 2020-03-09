import pygame
import sys

# game setup
game = {
    "caption": "Connect Four",
    "width": 500,
    "height": 400,
    "fill": (20, 20, 20)
}

"""
Circle class
both for the input circle and the circles displayed in the grid below
"""


class Circle:
    def __init__(self, cx, cy, r, color, colors=[(180, 30, 30), (180, 180, 30)]):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.color = color
        self.colors = colors

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.cx, self.cy), self.r)

    def set_cx(self, cx):
        self.cx = cx

    def set_cy(self, cy):
        self.cy = cy

    def get_cx(self):
        return self.cx

    def get_color(self):
        return self.color

    def toggle_color(self):
        if self.color == self.colors[0]:
            self.color = self.colors[1]
        else:
            self.color = self.colors[0]


def run_game():
    pygame.init()
    pygame.display.set_caption(game["caption"])
    screen = pygame.display.set_mode((game["width"], game["height"]))

    # grid setup
    rows = 6
    columns = 6

    # r to fit the desired number of rows and columns
    size = min(game["width"], game["height"])
    r = min(int(game["width"] / (columns * 2)),
            int(game["height"] / ((rows + 1) * 2)))

    # colors
    colors = [(180, 30, 30), (180, 180, 30)]

    # circle hovering on the grid
    circle_input = Circle(r, r, r, colors[0], colors)

    # list of circles
    circles = []

    while True:
        # key binding
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:
                cx = pygame.mouse.get_pos()[0]
                if cx > r and cx < game["width"] - r:
                    circle_input.set_cx(cx)

            if event.type == pygame.MOUSEBUTTONDOWN:
                cx = circle_input.get_cx()
                cy = game["height"] - r
                color = circle_input.get_color()
                circle = Circle(cx, cy, r, color, colors)
                circles.append(circle)

                circle_input.toggle_color()

        # draw
        screen.fill(game["fill"])
        circle_input.draw(screen)
        for circle in circles:
            circle.draw(screen)

        # update
        pygame.display.update()


run_game()
