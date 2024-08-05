from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
GAMEOVERFONT = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.pendown()
        self.color("white")
        self.points = 0

        self.write(f"score: {self.points}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("game over", move=False, align=ALIGNMENT, font=GAMEOVERFONT)
    def refresh(self):
        self.points+=1
        self.clear()
        self.write(f"score: {self.points}", move=False, align=ALIGNMENT, font=FONT)
