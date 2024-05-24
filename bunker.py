from turtle import Turtle
BUNKER_HEIGHT = 3
BUNKER_WIDTH = 6


class Bunker:
    def __init__(self, coordinates):
        self.reserve = []
        self.shift = 9
        self.start_y = 0
        self.start_x = 0
        self.build_bunker(coordinates)

    def build_bunker(self, positions):
        for position in positions:
            self.start_x = position[0]
            self.start_y = position[1]
            for row in range(BUNKER_HEIGHT):
                for element in range(BUNKER_WIDTH):
                    element = Turtle(shape='square')
                    element.color('white')
                    element.shapesize(0.4, 0.4)
                    element.penup()
                    element.goto(self.start_x, self.start_y)
                    self.reserve.append(element)
                    self.start_x += self.shift
                self.start_y += self.shift
                self.start_x = position[0]

    def element_destroyed(self, area):
        self.reserve.remove(area)
        area.hideturtle()
        del area
