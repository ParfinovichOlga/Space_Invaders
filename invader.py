from turtle import Turtle
from bullet import Bullet
import random

START_POINT = (-280, 240)
NUMBER_INVADERS = 11


class Invader:
    def __init__(self, invaders_shape):
        self.group = []
        self.start_x = START_POINT[0]
        self.start_y = START_POINT[1]
        self.shift = 50
        self.move_x = 1
        self.move_y = 0
        self.create_group(invaders_shape)
        self.bullets = []
        self.fire()

    def create_group(self, inv_shape):
        for shape in inv_shape:
            for invader in range(NUMBER_INVADERS):
                invader = Turtle(shape=shape)
                invader.penup()
                invader.goto(self.start_x, self.start_y)
                self.group.append(invader)
                self.start_x += self.shift
            self.start_y -= self.shift/1.5
            self.start_x = START_POINT[0]
        self.start_x = START_POINT[0]
        self.start_y = START_POINT[1]

    def move(self):
        for invader in self.group:
            new_x = invader.xcor() - self.move_x
            new_y = invader.ycor() - self.move_y
            if new_x > 364 or new_x < -364:
                self.move_x = self.move_x * -1
                self.move_y += 0.01
            invader.goto(new_x, new_y)

    def killed(self, inv):
        self.group.remove(inv)
        inv.reset()
        inv.hideturtle()
        del inv

    def fire(self):
        self.bullets.clear()
        for invader in random.choices(self.group, k=5):
            bullet = Bullet(invader.position())
            bullet.color('green')
            self.bullets.append(bullet)

    def increase_speed(self):
        if self.move_x < 1.3:
            self.move_x *= 1.05
