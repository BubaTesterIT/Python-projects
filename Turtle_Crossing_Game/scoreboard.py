from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):

        self.write(f"Level:{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER :(", align=ALIGNMENT, font=FONT)


