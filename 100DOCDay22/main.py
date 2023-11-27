from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create a paddle that can be moved using left and right keys
paddle_one = Paddle(position=(-380, 0))
paddle_two = Paddle(position=(380, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkeypress(paddle_one.move_up, 'Up')
screen.onkeypress(paddle_one.move_down, 'Down')
screen.onkeypress(paddle_two.move_up, 'w')
screen.onkeypress(paddle_two.move_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    print(ball.move_speed)
    screen.update()
    ball.move()
    
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(paddle_two) < 50 and ball.xcor() > 355 or ball.distance(paddle_one) < 50 and ball.xcor() > -355:
        ball.bounce_x()
        
    if ball.xcor() > 375:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -375:
        ball.reset_position()
        score.r_point()
# Keep track of scores 










screen.exitonclick()