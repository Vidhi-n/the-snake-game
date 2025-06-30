from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("the snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<20:
        score.increase_score()
        snake.extend(snake.segments[-1].pos())
        food.refresh()

    #detect collision with wall
    if snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.ycor()<-280  :
        game_is_on=False
        score.over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.over()

screen.exitonclick()
