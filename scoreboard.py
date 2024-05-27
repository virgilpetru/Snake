from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0, 270 )
        self.score = 0
        with open("data.txt",mode=("r")) as data:
            self.highscore = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode=("w")) as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


