from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from blocks import Blocks
# from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("blue")
screen.setup(width=500, height=700)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -300))
blocks = Blocks()
ball = Ball((0, -270))
blocks.create_blocks()
for block in blocks.all_blocks:
    block.goto()
# scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

#
#
game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    ball.move()


    # Detect collision with wall
    if ball.xcor() > 220 or ball.xcor() < -220:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 45 and ball.ycor() < -260:
        ball.bounce_x()
    # Detect collision with blocks
    for block in blocks.all_blocks:
        if ball.distance(block) < 40:
            ball.bounce_x()
            # block.reset()
            # block.penup()
            # block.hideturtle()
            # blocks.remove_blocks(block)

screen.exitonclick()
