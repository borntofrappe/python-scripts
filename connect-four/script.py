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
        current_row = self.grid[row]
        for cell in current_row:
            match += cell
        match += ' '

        # column (backwards, but not important)
        current_column = [self.grid[index][column]
                          for index in range(len(self.grid))]
        for cell in current_column:
            match += cell
        match += ' '

        # diagonals
        # ....TODO
        # southwest to northeast
        x = column
        y = self.rows - row - 1

        if x < y:
            y -= x
            x = 0
        else:
            x -= y
            y = 0
        while x < self.columns and y < self.rows:
            match += self.grid[self.rows - y - 1][x]
            x += 1
            y += 1

        match += ' '

        # northeast to southwest
        x = column
        y = self.rows - row - 1

        if x < y:
            x += y
            y = 0
        else:
            y -= x
            x = self.columns - 1
        while x > 0 and y < self.rows:
            match += self.grid[self.rows - y - 1][x]
            x -= 1
            y += 1

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
