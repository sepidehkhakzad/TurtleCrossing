import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)

game_on = True
screen.onkey(player.move, "Up")
screen.listen()

while game_on:
    cars.create_cars()
    cars.move()
    if player.ycor() > 280:
        player.reset_player()
        scoreboard.increase_level()

    for cars1 in cars.cars_list:
        if player.distance(cars1) < 30 and (player.xcor() - cars1.xcor() < -20 or player.xcor() - cars1.xcor() > 10):
            scoreboard.gameover()
            game_on = False

    time.sleep(0.1 - 0.01 * scoreboard.level)
    screen.update()

screen.exitonclick()
