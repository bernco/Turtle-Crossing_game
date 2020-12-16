from turtle import Screen
from myturtle import MyTurtle
from car import Car
import time

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.title("Bernco Turtle Racing")

game_screen.tracer(0)

my_turtle = MyTurtle()
my_car = Car()

game_screen.listen()
game_screen.onkeypress(key="Up", fun=my_turtle.move_up)

game_is_on = True


while game_is_on:

    time.sleep(my_car.speed_time)
    for _ in range(6):
        my_car.move_car()
        my_car.car_multiplying()
    game_screen.update()

game_screen.exitonclick()
