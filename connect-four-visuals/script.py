import pygame
import sys

game = {
    "caption": "Connect Four",
    "width": 500,
    "height": 400,
    "fill": (25, 20, 22),
}


class Circle:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r

    def draw(self, screen):
        pygame.draw.circle(screen, (180, 180, 180), (self.cx, self.cy), self.r)

    def set_cx(self, cx):
        self.cx = cx

    def set_cy(self, cy):
        self.cy = cy

    def get_cx(self):
        return self.cx


def run_game():
    pygame.init()
    pygame.display.set_caption(game["caption"])
    screen = pygame.display.set_mode((game["width"], game["height"]))

    size = min(game["width"], game["height"])
    rows = 6
    columns = 6

    r = (size) // (rows * 2 + 1)
    circle_input = Circle(r, r, r)
    circles = []

    while True:
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
                circle = Circle(cx, cy, r)
                circles.append(circle)

            screen.fill(game["fill"])
            circle_input.draw(screen)
            for circle in circles:
                circle.draw(screen)

            pygame.display.update()


run_game()
