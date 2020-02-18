from maze import Maze

# suggested range [1, 10]
# it works with 1 as well :p
size = 5
maze = Maze(size)
print("Here's your grid:\n")
print(maze)
print("\nHere's your maze:\n")
maze.binary_tree()
print(maze)
maze.write_file()
