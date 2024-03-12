from turtle import Turtle

START = (0, -280)
MOVE = 10
FINISH = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('green')
        self.pu()
        self.shape("turtle")
        self.reset_player()

    def reset_player(self):
        self.setheading(90)
        self.goto(START)

    def move(self):
        self.forward(MOVE)
