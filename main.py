from turtle import Screen
from score_board import Score
from paddle import Paddle
from ball import Ball
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.l_go_up,"w")
screen.onkey(l_paddle.l_go_dpwn,"s")
game_is_on=True
while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.move_speed)
    if ball.ycor()>279 or ball.ycor()<-279:
        ball.bounce_y()
    #Detect the collision 

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        
        ball.bounce_x()
    #Detect the ball touches the wall

    if ball.xcor()>390:
        ball.reset()
        score.l_point()

        
    if ball.xcor()<-390:
        ball.reset()
        score.r_point()

screen.exitonclick()