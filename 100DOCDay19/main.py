from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fd():
    tim.forward(10)

def move_bd():
    tim.back(10)    

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkeypress(key='w', fun=move_fd) # We can pass functions as arguments in another function (we don't use parenthesis when doing this)
screen.onkeypress(key='s', fun=move_bd)
screen.onkeypress(key='a', fun=move_left)
screen.onkeypress(key='d', fun=move_right)
screen.onkeypress(key='c', fun=clear_screen)

screen.exitonclick()