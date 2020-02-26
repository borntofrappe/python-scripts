from shapes import Circle

"""
Player class
inherit from Circle and set up the variables to move the shape horizontally

self.bullets limit the number of bullets on the screen
"""


class Player(Circle):
    def __init__(self, x, y, r=20, w=5):
        super().__init__(x, y, r, w)
        self.is_moving = False
        self.dx = 2
        self.bullets = 3

    def move(self):
        self.is_moving = True

    def stop(self):
        self.is_moving = False

    def update(self):
        self.x += self.dx

    def move_right(self):
        self.dx = abs(self.dx)

    def move_left(self):
        self.dx = abs(self.dx) * -1


"""
Bullet class
inherit from Circle to draw a shape moving upwards
"""


class Bullet(Circle):
    def __init__(self, x, y, r=5, w=0):
        super().__init__(x, y, r, w)

    def update(self):
        self.y -= 2


"""
Enemy class
inherit from Circle to create a shape moving horizontally and vertically when the shape hits the screen boundaries
"""


class Enemy(Circle):
    def __init__(self, x, y, r=15, w=5):
        super().__init__(x, y, r, w)
        self.dx = 1
        self.dy = 30

    def bounce(self):
        self.dx *= -1
        self.y += self.dy

    def update(self):
        self.x += self.dx
