from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "pink", "blue", "purple"]
START = 5
MOVE = 10
FINISH = 300


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.cars_list = []

    def cars(self, y_line):
        car = Turtle()
        car.pu()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2)
        car.goto(300 - START, y_line)
        self.cars_list.append(car)

    def move(self):
        for car in self.cars_list:
            car.goto(car.xcor() - MOVE, car.ycor())

    def create_cars(self):
        for y in range(-240, 240, 20):
            if random.random() > 0.99:
                self.cars(y_line=y)
