from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.update()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")


game_is_on = True
while game_is_on:
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        snake.extend()
    screen.update()
    time.sleep(0.1)

    if snake.head.xcor()>275 or snake.head.xcor()<-275 or snake.head.ycor()>275 or snake.head.ycor()<-275:
        game_is_on = False

    for i in snake.segments[1:]:
        if snake.head.distance(i)<10:
            game_is_on = False

score.game_over()









screen.exitonclick()
