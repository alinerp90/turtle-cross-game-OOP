import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

'''
Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.
'''

STARTING_POSITION = (0, -280)

# screen set up
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# score set up
scoreboard = Scoreboard()

# player set up
player = Player()

# car set up
car = CarManager()

# keyboard set up
screen.listen()
screen.onkey(player.move, "Up")



# game brain
game_is_on = True
count = 0
divisor = 6

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car_move()
    # Create a car every 5 loops
    count += 1
    if count % divisor == 0:
        car.create_cars()
    # detect collision with car
    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        player.goto(STARTING_POSITION)
        scoreboard.increase_score()
        car.level_up()
        if scoreboard.score < 5:
            divisor -= 1


screen.exitonclick()