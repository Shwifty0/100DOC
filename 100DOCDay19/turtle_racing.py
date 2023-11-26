from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle do you think is going to win?: ')
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

def set_pos(x, y, turtle):
    turtle.penup()
    return turtle.setpos(x, y)

def move_forward(turtle):
    return turtle.forward(random.randint(1, 10))

is_race_on = False
x_cord, y_cord = -230, -120

turtles = []
for i in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[i])
    y_cord += 30
    set_pos(x_cord, y_cord, new_turtle)
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True    

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color.upper()} turtle won!")
            else:
                print(f"You've lost! {winning_color.upper()} turtle won!")
                
        move_forward(turtle=turtle)
    
screen.exitonclick()