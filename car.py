from turtle import Turtle
import random

# colors to be used in designing the block cars
COLOR_LIST = ["red", "green", "grey", "orange", "pink", "black", "blue", "purple"]

# speed details for the cars
SPEED_TIME = 0.1
CAR_SPEED = 5
STARTING_POSITION_X = 280
SPEED_INCREASE = 0.7


class Car:

    # created an empty list for or class objects
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.speed_time = SPEED_TIME

    # this method creates and multiplies the cars only when the chance of the random number is 1
    # in this case prevents several cars to populate the screen when the method is called
    def car_multiplying(self):
        car_multiplier_chance = random.randint(1, 6)
        if car_multiplier_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.y_pos = random.randint(-240, 240)
            new_car.x_pos = STARTING_POSITION_X
            new_car.color(random.choice(COLOR_LIST))
            new_car.goto(new_car.x_pos, new_car.y_pos)
            self.car_list.append(new_car)

    # move car when called
    def move_car(self):
        for cars in self.car_list:
            cars.backward(CAR_SPEED)

    # increase the speed of the car
    def increase_speed(self):
        self.speed_time *= SPEED_INCREASE
