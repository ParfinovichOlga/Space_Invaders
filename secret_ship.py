from turtle import Turtle

START_POINT = (-1432, 270)


class SecretShip(Turtle):
    def __init__(self, shape):
        super().__init__()
        self.penup()
        self.shape(shape)
        self.goto(START_POINT[0], START_POINT[1])
        self.x_move = 1
        self.hideturtle()

    def move(self):
        self.showturtle()
        if self.xcor() < 2422:
            new_x = self.xcor() + self.x_move
            self.goto(new_x, self.ycor())
        else:
            self.goto(START_POINT)

    def killed(self):
        self.hideturtle()
        self.goto(START_POINT)
        self.showturtle()
