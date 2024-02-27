from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score}", font= FONT)

    def increase_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font= ("Courier", 40, "normal"))

