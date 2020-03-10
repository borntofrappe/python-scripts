import pygame
import sys

# game setup
game = {
    "caption": "Connect Four",
    "width": 500,
    "height": 500,
    "fill": (10, 10, 10)
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

    def get_colors(self):
        return self.colors

    def toggle_color(self):
        if self.color == self.colors[0]:
            self.color = self.colors[1]
        else:
            self.color = self.colors[0]


"""
Grid class
developed for playing connect four in the terminal
the logic to show the grid with ASCII characters is preserved for debugging
"""


class Grid:
    def __str__(self):
        # ! prefer an odd number
        spaces = 3
        grid = ""
        # pipes
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

        # dashes
        grid += " " + ("-" * spaces + " ") * self.columns

        # nums
        grid += "\n "
        for c in range(self.columns):
            grid += str(c).center(spaces + 1, " ")
        return grid

    def __init__(self, columns, rows, color_default, colors):
        self.columns = columns
        self.rows = rows
        self.color_default = color_default
        self.colors = colors
        self.grid = [[color_default for c in range(
            columns)] for r in range(rows)]

    def get_grid(self):
        grid = []
        for row in range(self.rows):
            for column in range(self.columns):
                cell = {
                    "color": self.grid[row][column],
                    "column": column,
                    "row": row
                }
                grid.append(cell)
        return grid

    def clear(self):
        self.grid = [[self.color_default for c in range(self.columns)]
                     for r in range(self.rows)]

    def matches_four(self, column, row, color):
        # build a string describing the current row + current column + diagonals
        match = ''

        # row
        c_min = max(0, column - 4)
        c_max = min(self.columns, column + 4)

        # diagonals
        c_gap = c_min - column
        north_east = ''
        south_east = ''

        for c in range(c_max - c_min):
            match += str(self.grid[row][c + c_min])

            # diagonals
            if row - c_gap >= 0 and row - c_gap < self.rows:
                north_east += str(self.grid[row - c_gap][c + c_min])
            if row + c_gap >= 0 and row + c_gap < self.rows:
                south_east += str(self.grid[row + c_gap][c + c_min])
            c_gap += 1

        # diagonals/2
        match += ' '
        match += north_east
        match += ' '
        match += south_east
        match += ' '

        # column
        r_min = max(0, row - 4)
        r_max = min(self.rows, row + 4)
        for r in range(r_max - r_min):
            match += str(self.grid[r + r_min][column])
        match += ' '

        # try to find four of the same value in the made up string
        try:
            match.index(str(color) * 4)
        except ValueError:
            return False
        else:
            return True

    def add_to_column(self, column, color):
        grid_transposed = [[self.grid[r][c]
                            for r in range(self.rows)] for c in range(self.columns)]

        try:
            grid_column = list(reversed(grid_transposed[column]))
            index = grid_column.index(self.color_default)
        except (IndexError, ValueError):
            return False
        else:
            row = len(self.grid) - 1 - index
            self.grid[row][column] = color
            return (column, row)


def run_game():
    pygame.init()
    pygame.display.set_caption(game["caption"])
    screen = pygame.display.set_mode((game["width"], game["height"]))

    # grid setup
    columns = 7
    rows = 6

    # r to fit the desired number of rows and columns
    rx = int(game["width"] / (columns * 2))
    ry = int(game["height"] / ((rows + 1) * 2))
    r = min(rx, ry)

    grid_width = columns * (r * 2)
    grid_height = rows * (r * 2)
    offset_x = int((game["width"] - grid_width) / 2)
    offset_y = int((game["height"] - (r * 2) - grid_height))

    # colors
    colors = [(180, 30, 30), (180, 180, 30)]

    # circle hovering on the grid
    circle = Circle(r, r, r, colors[0], colors)

    # grid
    color_default = (40, 40, 40)
    grid = Grid(columns, rows, color_default, colors)

    game_over = False

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
                    circle.set_cx(cx)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    grid.clear()
                    game_over = False
                else:
                    cx = circle.get_cx()
                    if cx > offset_x // 2 and cx < game["width"] - offset_x // 2:
                        column = (cx - offset_x) // (r * 2)
                        color = circle.get_color()
                        cell = grid.add_to_column(column, color)
                        if cell:
                            column, row = cell
                            if grid.matches_four(column, row, color):
                                # debugging
                                print(grid)
                                game_over = True

                            circle.toggle_color()

        # draw
        screen.fill(game["fill"])
        circle.draw(screen)

        for cell in grid.get_grid():
            color = cell["color"]
            cx = cell["column"] * (r * 2) + r + offset_x
            cy = (cell["row"] + 1) * (r * 2) + r + offset_y

            pygame.draw.circle(screen, color, (cx, cy), r)

        # update
        pygame.display.update()


run_game()
