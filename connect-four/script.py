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


columns = 5
rows = 4
grid = Grid(columns, rows)
print(grid)
