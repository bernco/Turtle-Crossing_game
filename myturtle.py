from turtle import Turtle

START_POSITION = 0, -280
FORWARD_PACE = 10

class MyTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.seth(90)
        self.goto(START_POSITION)

    def move_up(self):
        self.forward(FORWARD_PACE)