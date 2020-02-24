"""
Pong

revision of the project created following this tutorial
https://www.youtube.com/watch?v=XGf2GcyHPhc&t=79s
"""

import turtle
from paddle import Paddle
from ball import Ball

title = "Pong"
width = 750
height = 500
padding = 20
bgcolor = "#FEFEFE"
color = "#333333"

# setup
window = turtle.Screen()
window.title(title)
window.setup(width=width, height=height)
window.bgcolor(bgcolor)

# stops the window from updating
window.tracer(0)

# initialize turtles
paddle_a = Paddle(-width / 2 + padding, 0, 5, 1)
paddle_b = Paddle(width / 2 - padding, 0, 5, 1)
ball = Ball(0, 0)

# score
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0, height / 2 - 30)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center",
          font=("Fira Code", 12, "normal"))


# keyboard binding
# listen
window.listen()
# react
window.onkeypress(paddle_a.move_up, 'w')
window.onkeypress(paddle_a.move_up, 'W')
window.onkeypress(paddle_a.move_down, 's')
window.onkeypress(paddle_a.move_down, 'S')

window.onkeypress(paddle_b.move_up, '8')
window.onkeypress(paddle_b.move_down, '5')


def quit_game():
    window.bye()


window.onkey(quit_game, 'q')
window.onkey(quit_game, 'Q')

# game loop
while True:
    window.update()

    ball.move()

    # collision with walls
    # y
    if abs(ball.ycor()) > height / 2:
        ball.bounce_y()

    # x
    if abs(ball.xcor()) > width / 2:
        pen.clear()
        if(ball.xcor() > 0):
            score_a += 1
        else:
            score_b += 1
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center",
                  font=("Fira Code", 12, "normal"))
        ball.center()

    # collision with paddles
    if ball.xcor() > width / 2 - padding * 2 and ball.ycor() < paddle_b.ycor() and ball.ycor() > paddle_b.ycor() - 70:
        ball.setx(width / 2 - padding * 2)
        ball.bounce_x()

    if ball.xcor() < -width / 2 + padding * 2 and ball.ycor() < paddle_a.ycor() and ball.ycor() > paddle_a.ycor() - 70:
        ball.setx(-width / 2 + padding * 2)
        ball.bounce_x()
