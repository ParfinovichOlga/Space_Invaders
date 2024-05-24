from turtle import Turtle
from bullet import Bullet


POINT_LEFT_RIGHT = 20


class Player(Turtle):
    def __init__(self, coordinate, ship):
        super().__init__()
        self.shape(ship)
        self.shapesize(4, 4, 2)
        self.color('white')
        self.penup()
        self.goto(coordinate)
        self.bullet = None

    def go_left(self):
        new_x = self.xcor() - POINT_LEFT_RIGHT
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + POINT_LEFT_RIGHT
        self.goto(new_x, self.ycor())

    def fire(self):
        if self.bullet is not None:
            self.bullet.hideturtle()
            del self.bullet
        self.bullet = Bullet(self.position())
        self.bullet.fire()

