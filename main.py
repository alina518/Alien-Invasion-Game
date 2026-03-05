from turtle import Turtle,Screen
from alien import Alien
from tank import Tank
from score import Score
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)

tank=Tank()
alien=Alien()
score=Score()

screen.listen()
screen.onkey(tank.go_left,key='Left')
screen.onkey(tank.go_right,key='Right')
screen.onkey(tank.launch_laser,key='space')
game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    alien.create_alien()
    alien.move()
    tank.move_laser()
    score.update_timer()
    #detect collision with alien
    for falling_alien in alien.all_aliens[:]:
        if tank.laser_state=='firing' and tank.laser.distance(falling_alien)<20:
            falling_alien.hideturtle()
            alien.all_aliens.remove(falling_alien)
            score.increase_score()
            tank.reset_laser()

            alien.increase_speed()
        if score.time_left<=0:
            game_is_on=False
            score.game_over()




screen.exitonclick()
