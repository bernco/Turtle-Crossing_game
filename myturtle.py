from turtle import Turtle

# constants to be used
START_POSITION = 0, -280
FORWARD_PACE = 10


# MyTurtle inherits from the Turtle class
class MyTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.seth(90)
        self.go_to_start()

    # moves the turtle up when called
    def move_up(self):
        self.forward(FORWARD_PACE)

    # sends the turtle back to initial start position
    def go_to_start(self):
        self.goto(START_POSITION)
