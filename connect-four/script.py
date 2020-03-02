class Grid:
    def __str__(self):
        grid = self.grid
        grid_transposed = [[row[i] for row in grid] for i in range(len(grid))]
        output = ""
        for row in grid_transposed:
            output += "|"
            for cell in row:
                output = output + str(cell).center(3, " ") + "|"
            output += "\n"

        output += " "
        for x in range(self.columns):
            output += str(x).center(4, " ")
        return output

    def make_grid(self, columns, rows):
        return [[" " for x in range(columns)] for y in range(rows)]

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = self.make_grid(self.columns, self.rows)

    def empty_grid(self):
        self.grid = self.make_grid(self.columns, self.rows)

    def select_column(self, x, player="R"):
        column = self.grid[x]
        try:
            index = list(reversed(column)).index(" ")
            column[len(column) - index - 1] = player
        except ValueError:
            print("Not found")


columns = 5
rows = 5
grid = Grid(columns, rows)

players = ["R", "Y"]
are_playing = True
player = "R"
while(are_playing):
    print(grid)
    print()
    print("Player: " + player)
    selection = input("Select column: ").rstrip()
    if(selection == "q"):
        are_playing = False
        break
    print()
    grid.select_column(int(selection), player)

    if player == "R":
        player = "Y"
    else:
        player = "R"
