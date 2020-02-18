from cell import Cell
from random import choice


class Maze:
    def __str__(self):
        return self.format_maze()

    def __init__(self, size):
        self.size = size
        maze = []
        for i in range(size ** 2):
            column = i % size
            row = i // size
            cell = Cell(column, row)
            maze.append(cell)
        self.maze = maze

    def binary_tree(self):
        maze = self.maze
        size = self.size
        if(len(maze) > 0):
            for cell in maze:
                # !! this would not work
                ## column = cell["column"]
                # research what it means that the object is not _subscriptable_
                column = cell.column
                row = cell.row
                neighbors = []
                if(row > 0):
                    neighbors.append((column, row - 1))
                if(column < size - 1):
                    neighbors.append((column + 1, row))

                if(len(neighbors) > 0):
                    neighbor = choice(neighbors)
                    c, r = neighbor
                    index = c + r * size
                    if(r < row):
                        cell.open_wall("north")
                        maze[index].open_wall("south")
                    else:
                        cell.open_wall("east")
                        maze[index].open_wall("west")
        self.maze = maze

    def format_maze(self):
        # dashes as in the number of dashes - separating the edges horizontally
        # +---+
        # pipe as in the number of pipes | separating vertically
        # +
        # |
        # +
        # be sure to account for contiguous cells
        dashes = 3
        pipes = 1
        size = self.size
        maze = self.maze

        row_edges = (['+'] + [' '] * dashes) * size + ['+']
        # + 2 to consider the edges
        row_empty = [' '] * (dashes + 2) * size

        grid = [row_edges]
        for i in range(size):
            # copy the lists otherwise you'd modify every sequence
            for pipe in range(pipes):
                grid.append(row_empty.copy())
            grid.append(row_edges.copy())

        for cell in maze:
            column = cell.column
            row = cell.row
            c = column * (dashes + 1)
            r = row * (pipes + 1)
            walls = cell.walls
            if(walls["north"]):
                grid[r][c + 1: c + 1 + dashes] = ["-"] * (dashes)
            if(walls["west"]):
                for pipe in range(pipes):
                    grid[r + 1 + pipe][c] = "|"
            if(walls["east"]):
                for pipe in range(pipes):
                    grid[r + 1 + pipe][c + 1 + dashes] = "|"
            if(walls["south"]):
                grid[r + pipes + 1][c + 1: c + 1 + dashes] = ["-"] * (dashes)

        output = ''
        for row in grid:
            for cell in row:
                output += cell
            output += '\n'

        return output.rstrip()

    def write_file(self):
        path = 'maze.txt'
        with open(path, "w") as file:
            file.write(self.format_maze())

        print(f"\nCheck out {path}\nAnd prepared to be dazzled :)")
