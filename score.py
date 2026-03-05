from turtle import Turtle
import time
FONT = ("Courier", 15, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.time_left=30
        self.last_time=time.time()
        self.hideturtle()
        self.penup()
        self.goto(-240,250)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}\nTime: {self.time_left}s', align='center', font=FONT)
    def update_timer(self):
        current_time=time.time()
        if current_time-self.last_time>=1:
            self.time_left-=1
            self.last_time=current_time
            self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over.', align='center', font=FONT)

