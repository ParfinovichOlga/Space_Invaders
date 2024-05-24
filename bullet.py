from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.y_move = 20
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=0.1, stretch_wid=0.4)

    def fire(self):
        self.showturtle()
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def spent(self, b):
        b.reset()
        b. hideturtle()
        del b

    def attact(self):
        self.showturtle()
        new_y = self.ycor() - 5
        self.goto(self.xcor(), new_y)
