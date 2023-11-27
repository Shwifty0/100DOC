from turtle import Screen
from player import Player_Turtle
from cars import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
screen.tracer(0)

p_turtle = Player_Turtle()
cars = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(p_turtle.up, 'Up')
screen.onkeypress(p_turtle.down, 'Down')
screen.onkeypress(p_turtle.left, 'Left')
screen.onkeypress(p_turtle.right, 'Right')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.spawn_car()
    cars.move()
    
    for car in cars.cars:
        if car.distance(p_turtle) < 20:    
            scoreboard.game_over()
            game_is_on = False
            
    
    if p_turtle.is_at_finish():
        cars.increase_speed()
        p_turtle.reset_pos()
        scoreboard.update_level()



screen.exitonclick()