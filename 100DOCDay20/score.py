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
        self.clear()       
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)    
        
    def save_score(self):
        with open('high_score.txt', 'w') as f:
                f.write(f"{self.score}")
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score  = self.score
        self.score = 0
        self.update_scoreboard()
    
    def increase_score(self):
        self.score += 1
        self.save_score()
        self.update_scoreboard()