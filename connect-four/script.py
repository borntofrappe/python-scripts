
class Grid:
    def __str__(self):
        # ! prefer an odd number
        spaces = 3
        grid = ""
        # pipes
        for row in self.grid:
            grid += "|"
            for cell in row:
                grid += cell.center(spaces, " ") + "|"
            grid += "\n"

        # dashes
        grid += " " + ("-" * spaces + " ") * self.columns

        # nums
        grid += "\n "
        for c in range(self.columns):
            grid += str(c).center(spaces + 1, " ")
        return grid

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = [[" " for c in range(columns)] for r in range(rows)]

    def clear(self):
        self.grid = [[" " for c in range(self.columns)]
                     for r in range(self.rows)]

    def add_to_column(self, column, input):
        grid_transposed = [[self.grid[r][c]
                            for r in range(self.rows)] for c in range(self.columns)]
        grid_column = list(reversed(grid_transposed[column]))

        try:
            index = grid_column.index(" ")
            self.grid[len(self.grid) - 1 - index][column] = input
        except ValueError:
            print("Column unavailable")


columns = 5
rows = 4
grid = Grid(columns, rows)
grid.add_to_column(3, "R")
grid.add_to_column(3, "T")
grid.add_to_column(3, "T")
grid.add_to_column(3, "T")
grid.add_to_column(3, "T")
grid.add_to_column(3, "T")
print(grid)
