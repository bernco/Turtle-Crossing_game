from turtle import Turtle
import random

COLOR_LIST = ["red", "green", "grey", "orange", "pink", "black", "blue", "purple"]

SPEED_TIME = 0.1
CAR_SPEED = -5
STARTING_POSITION_X = 280


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.speed_time = SPEED_TIME
        self.y_pos = random.randint(-240, 240)
        self.x_pos = STARTING_POSITION_X

    def car_multiplying(self):
        # self.color(random.choice(COLOR_LIST))
        self.goto(self.x_pos, self.y_pos)
        # self.forward(CAR_SPEED)

    def move_car(self):
        self.forward(CAR_SPEED)
