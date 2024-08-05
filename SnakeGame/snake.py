STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.adding(position)

    def adding(self,position):
            timmy = Turtle("square")
            timmy.color("white")
            timmy.penup()
            timmy.goto(position)
            self.segments.append(timmy)

    def extend(self):
        self.adding(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
            #self.move()

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
           # self.move()

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
            #self.move()
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
            #self.move()