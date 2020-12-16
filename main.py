from turtle import Screen
from myturtle import MyTurtle
from car import Car
from scoreboard import ScoreBoard
import time

# design the screen
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.title("Bernco Turtle Racing")

# Pause the screen animation
game_screen.tracer(0)

# create instances of our classes
my_turtle = MyTurtle()
my_car = Car()
my_scoreboard = ScoreBoard()

# screen should listen to our input from the keyboard
game_screen.listen()
game_screen.onkey(key="Up", fun=my_turtle.move_up)

# to keep the game running
game_is_on = True


while game_is_on:

    # controls the screen delay
    time.sleep(my_car.speed_time)

    # shows animation
    game_screen.update()

    # calling methods from our classes
    my_car.car_multiplying()
    my_car.move_car()
    for cars in my_car.car_list:
        # checks for collision with car
        if my_turtle.distance(cars) < 25:
            my_turtle.go_to_start()
            my_scoreboard.game_over()
            game_is_on = False

        # checks is the player is on the other side
        if my_turtle.ycor() > 280:
            my_scoreboard.increase_level()
            my_car.increase_speed()
            my_turtle.go_to_start()

game_screen.exitonclick()
