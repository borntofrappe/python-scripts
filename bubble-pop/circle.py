class Circle:
    def __init__(self, x, y, r=20, w=5):
        self.x = int(x - r / 2)
        self.y = int(y - r)
        self.r = r
        self.w = w
        self.color = (20, 20, 40)
        self.is_moving = False
        self.dx = 1

    def move(self):
        self.is_moving = True

    def stop(self):
        self.is_moving = False

    def update(self):
        self.x += self.dx

    def move_right(self):
        self.dx = 1

    def move_left(self):
        self.dx = -1

    def move_up(self):
        self.y -= 1
