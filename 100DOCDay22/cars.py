from turtle import Turtle
import random

COLORS = ['red','blue', 'green', 'yellow', 'purple']
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE


    def spawn_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-200, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.back(self.move_speed)
    
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
