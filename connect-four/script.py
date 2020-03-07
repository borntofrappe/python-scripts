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

    def matches_four(self, row, column, player):
        # build a string describing the current row + current column + diagonals
        match = ''

        # row
        c_min = max(0, column - 3)
        c_max = min(self.columns, column + 3)

        # diagonals
        north_east = ''
        south_east = ''
        counter = c_min - column

        for c in range(c_max - c_min):
            match += self.grid[row][c + c_min]

            # diagonals
            if row - counter >= 0 and row - counter < self.rows:
                north_east += self.grid[row - counter][c + c_min]
            if row + counter >= 0 and row + counter < self.rows:
                south_east += self.grid[row + counter][c + c_min]
            counter += 1

        # add the diagonals
        match += ' '
        match += north_east
        match += ' '
        match += south_east
        match += ' '

        # column
        r_min = max(0, row - 3)
        r_max = min(self.rows, row + 3)
        for r in range(r_max - r_min):
            match += self.grid[r + r_min][column]
        match += ' '

        # try to find four of the same value in the made up string
        try:
            match.index(player * 4)
        except ValueError:
            return False
        else:
            return True

    def add_to_column(self, column, input):
        grid_transposed = [[self.grid[r][c]
                            for r in range(self.rows)] for c in range(self.columns)]

        try:
            grid_column = list(reversed(grid_transposed[column]))
            index = grid_column.index(" ")
        except (IndexError, ValueError):
            return False
        else:
            row = len(self.grid) - 1 - index
            self.grid[row][column] = input
            return (row, column)


def highlight_message(message):
    print()
    print("*" * len(message))
    print(message)
    print("*" * len(message))
    print()


def run_game():
    highlight_message("*** Connect Four ***")

    columns = 6
    rows = 6
    grid = Grid(columns, rows)

    print(grid)
    print()

    player = "R"
    while True:
        print(f"Player: {player}")
        column = input("Select column: ")

        if column.lower().rstrip() == "q":
            break

        try:
            c = int(column)
        except ValueError:
            highlight_message("**Enter a number**")
        else:
            cell = grid.add_to_column(c, player)
            if cell:
                print()
                print(grid)
                print()

                row, column = cell
                if grid.matches_four(row, column, player):
                    highlight_message(f"** Player {player} wins! **")
                    break

                if player == "R":
                    player = "T"
                else:
                    player = "R"
            else:
                highlight_message(f"**Column unavailable**")


run_game()
