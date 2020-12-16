from turtle import Turtle

# define constants
FONT = ("Arial", 14, "bold")
ALIGNMENT = "center"
GAME_OVER_FONT = ("Arial", 40, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.pu()
        self.hideturtle()
        self.goto(-200, 270)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    # increase level of the score board
    def increase_level(self):
        self.clear()
        self.level += 1
        self.goto(-200, 270)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    # resets the turtle to the beginning
    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
