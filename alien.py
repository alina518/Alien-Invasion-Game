from turtle import Turtle
import random
COLORS = [
    "red", "orange", "yellow", "green", "blue", "purple",
    "pink", "cyan", "magenta", "lime", "brown", "gold",
    "salmon", "turquoise", "violet", "indigo", "coral",
    "teal", "maroon", "navy", "olive", "chocolate", "orchid"
]
START_SPEED=5
class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_aliens=[]
        self.alien_speed=START_SPEED
    def create_alien(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            alien=Turtle('turtle')
            alien.penup()
            alien.color(random.choice(COLORS))
            random_x=random.randint(-250,250)
            alien.goto(random_x,300)
            self.all_aliens.append(alien)
    def move(self):
        for alien in self.all_aliens:
            alien.setheading(270)
            alien.forward(self.alien_speed)
    def increase_speed(self):
        self.alien_speed+=2
