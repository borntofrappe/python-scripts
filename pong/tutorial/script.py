"""
Pong

following this tutorial
https://www.youtube.com/watch?v=XGf2GcyHPhc&t=79s
"""

# using the turtle module
import turtle

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


def make_turtle(x, y, w=1, h=1):
    paddle = turtle.Turtle()
    # speed animation, max speed
    paddle.speed(0)
    paddle.shape('square')
    paddle.color(color)
    # stretch size
    paddle.shapesize(stretch_wid=w, stretch_len=h)
    # don't draw lines
    paddle.penup()
    # position to the left
    paddle.goto(x, y)

    return paddle


paddle_a = make_turtle(-width / 2 + padding, 0, 5, 1)
paddle_b = make_turtle(width / 2 - padding, 0, 5, 1)
ball = make_turtle(0, 0)

paddle_dy = 20
ball.dx = 0.5
ball.dy = 0.5

score_a = 0
score_b = 0

pen = make_turtle(0, height / 2 - 30)
pen.hideturtle()
pen.goto(0, height / 2 - 30)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center",
          font=("Fira Code", 12, "normal"))


def paddle_up(paddle):
    y = paddle.ycor()
    y += paddle_dy
    paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    y -= paddle_dy
    paddle.sety(y)


# keyboard binding
# listen
window.listen()
# react
window.onkeypress(lambda: paddle_up(paddle_a), 'w')
window.onkeypress(lambda: paddle_down(paddle_a), 's')

window.onkeypress(lambda: paddle_up(paddle_b), '8')
window.onkeypress(lambda: paddle_down(paddle_b), '5')


def quit_game():
    window.bye()


window.onkey(quit_game, 'q')
window.onkey(quit_game, 'Q')

# game loop
while True:
    window.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with floor/ceiling
    if abs(ball.ycor()) > height / 2:
        ball.dy *= -1

    # collision with sides
    if abs(ball.xcor()) > width / 2:
        pen.clear()
        if(ball.xcor() > 0):
            score_a += 1
        else:
            score_b += 1
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center",
                  font=("Fira Code", 12, "normal"))

        ball.dx *= -1
        ball.setx(0)
        ball.sety(0)

    # collision with paddles
    if ball.xcor() > width / 2 - padding * 2 and ball.ycor() < paddle_b.ycor() and ball.ycor() > paddle_b.ycor() - 70:
        ball.setx(width / 2 - padding * 2)
        ball.dx *= -1

    if ball.xcor() < -width / 2 + padding * 2 and ball.ycor() < paddle_a.ycor() and ball.ycor() > paddle_a.ycor() - 70:
        ball.setx(-width / 2 + padding * 2)
        ball.dx *= -1
