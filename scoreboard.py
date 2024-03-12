from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.level = 0
        self.pu()
        self.goto(-280, 250)
        self.show_scoreboard()

    def show_scoreboard(self):
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.clear()

        self.level += 1
        self.show_scoreboard()

    def gameover(self):
        t = Turtle()
        t.pu()
        t.ht()
        t.color("white")
        t.goto(0, 0)
        t.write("Game Over!", move=False, align="Center", font=FONT)
