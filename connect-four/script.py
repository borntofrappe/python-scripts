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

    def matches_four(self):
        return False

    def add_to_column(self, column, input):
        grid_transposed = [[self.grid[r][c]
                            for r in range(self.rows)] for c in range(self.columns)]

        try:
            grid_column = list(reversed(grid_transposed[column]))
            index = grid_column.index(" ")
        except (IndexError, ValueError):
            return False
        else:
            self.grid[len(self.grid) - 1 - index][column] = input
            return True


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
            if grid.add_to_column(c, player):
                print()
                print(grid)
                print()

                if grid.matches_four():
                    highlight_message(f"** ! Player {player} wins! **")
                    break

                if player == "R":
                    player = "T"
                else:
                    player = "R"
            else:
                highlight_message(f"**Column unavailable**")


run_game()
