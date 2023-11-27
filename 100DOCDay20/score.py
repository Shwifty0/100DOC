from turtle import Turtle
import os

SCORE = 0
ALIGNMENT = 'center'
FONT = ("Courier", 15, 'bold')
class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = SCORE
        
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.read()) 
        
        self.color("White")
        self.ht()
        self.penup()
        self.sety(270)
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        current_score = self.score        
        self.goto(-100, self.ycor())
        self.write(f"Score: {current_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, self.ycor())
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)    
        
    def save_score(self):
        with open('high_score.txt', 'w') as f:
                f.write(f"{self.score}")
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.save_score()
        self.clear()
        self.update_scoreboard()