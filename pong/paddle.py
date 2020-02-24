"""
ball class

set up a turtle in the form of a rectangle, moved up and down
"""
import turtle


class Paddle(turtle.Turtle):
    def __init__(self, x, y, w=5, h=1):
        super().__init__()
        self.speed(0)
        self.shape('square')
        self.shapesize(stretch_wid=w, stretch_len=h)
        self.penup()
        self.goto(x, y)

    def move_up(self, dy=20):
        self.sety(self.ycor() + dy)

    def move_down(self, dy=-20):
        self.sety(self.ycor() + dy)
