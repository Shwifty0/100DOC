from turtle import Turtle
LEVEL = 0
LEVEL_INCREASE = 1
class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = LEVEL
        self.ht()
        self.penup()
        self.goto(-280, 270)
        self.color('white')
        self.write(f'Level {self.level}', font=('Courier', '20', 'bold'))
    
    def update_level(self):
        self.clear()
        self.level += LEVEL_INCREASE
        self.write(f'Level {self.level}', font=('Courier', '20', 'bold'))
    
    def game_over(self):
        self.clear()
        self.penup()
        self.goto(-90, 0)
        self.ht()
        self.color('white')
        self.write(f'GAME OVER', font=('Courier', '25', 'bold'))