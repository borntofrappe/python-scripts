class Cell:
    def __str__(self):
        column = self.column
        row = self.row
        walls = []
        for wall in self.walls:
            if(self.walls[wall]):
                walls.append(wall)
        return f'Column: {column}\nRow: {row}\nWalls: {walls}\n'

    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.walls = {
            "north": True,
            "east": True,
            "south": True,
            "west": True
        }

    def open_wall(self, direction):
        self.walls[direction] = False
