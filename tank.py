from turtle import Turtle
positions=[(0,-260),(0,-240),(0,-220)]
length=[4,2,1]
move_dis=10
laser_speed=10
class Tank(Turtle):
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_tank()
        self.laser_state='ready'
        self.create_laser()
    def create_tank(self):
        for i in range(3):
            segment=Turtle('square')
            segment.shapesize(stretch_len=length[i],stretch_wid=1)
            segment.penup()
            segment.goto(positions[i])
            segment.color('white')
            self.segments.append(segment)
    def create_laser(self):
        self.laser=Turtle('square')
        self.laser.shapesize(stretch_wid=2.5,stretch_len=0.1)
        self.laser.color('red')
        self.laser.penup()
        self.laser.hideturtle()
    def update_laser_position(self):
        gun=self.segments[-1]
        self.laser.goto(gun.xcor(),gun.ycor()+20)

    def launch_laser(self):
        if self.laser_state=='ready':
            self.laser_state='firing'
            self.update_laser_position()
            self.laser.showturtle()
    def move_laser(self):
        if self.laser_state=='firing':
            self.laser.sety(self.laser.ycor()+laser_speed)
            if self.laser.ycor()>300:
                self.reset_laser()
    def reset_laser(self):
        self.laser.hideturtle()
        self.laser_state='ready'

    def go_left(self):
        for i in self.segments:
            i.backward(move_dis)

        if self.laser_state=='ready':
            self.update_laser_position()
    def go_right(self):
        for i in self.segments:
            i.forward(move_dis)
        if self.laser_state=='ready':
            self.update_laser_position()
