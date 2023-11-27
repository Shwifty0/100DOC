from turtle import Turtle

class Player_Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.seth(90)
        self.penup()
        self.sety(-270)

    def up(self):
        self.fd(10)

    def down(self):
        self.back(10)

    def left(self):
        new_x = self.xcor() - 10
        self.setx(new_x)

    def right(self):
        new_x = self.xcor() + 10
        self.setx(new_x)
    
    def is_at_finish(self):
        if self.ycor() > 250:
            return True
        else:
            return False
        
    def reset_pos(self):
        self.penup()
        self.sety(-270)