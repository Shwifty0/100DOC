from turtle import Turtle
STARTING_POSTIONS = [(0, 0),(-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.__init__()
        
    def create_snake(self):
        for position in STARTING_POSTIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)