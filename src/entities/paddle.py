import pygame
class Paddle:
    def __init__(self, color, x, y, width, height):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.mode= "still"
    
    def get_coordinate(self, letter):
        if letter == "x":
            return self.x
        elif letter == "y":
            return self.y
        else:
            return "wrong letter"

    def move(self):
        if self.mode == "left":
            self.x -= 10

        elif self.mode == "right":
            self.x += 10

        else:
            self.x = self.x

        if self.x <= 0:
            self.x = 0

        elif self.x >= 580:
            self.x = 580
