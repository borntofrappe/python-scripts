"""
ball class

set up a turtle in the form of a square, moved in the four directions
"""
import turtle


class Ball(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()

        self.dx = 0.25
        self.dy = 0.25
        self.speed(0)
        self.shape('square')
        self.penup()
        self.goto(x, y)

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_x(self):
        self.dx = self.dx * -1

    def bounce_y(self):
        self.dy = self.dy * -1

    def center(self):
        self.setx(0)
        self.sety(0)
        self.bounce_x()
