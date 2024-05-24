from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.turn = 3

    def write_score(self):
        self.goto(300, -280)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 10, "normal"))

    def write_turns(self):
        self.goto(-350, -280)
        self.write(self.turn, align="center", font=("Courier", 15, "bold"))

    def update_score(self):
        self.clear()
        if self.turn < 0:
            self.turn = 0
        self.write_score()
        self.write_turns()

    def point(self):
        self.score = self.score + 30

    def high_point(self):
        self.score = self.score + 100

    def killed(self):
        self.turn -= 1

    def end_game(self):
        self.goto(0, -15)
        self.write(f'Your score: {self.score}\nPress ↑ to restart game', align="center", font=("Courier", 20, "normal"))
