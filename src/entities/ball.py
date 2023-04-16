import pygame
class Ball:
    def __init__(self, color, x, y, radius):
        self.color=color
        self.x=x
        self.y=y
        self.radius=radius
        self.direction_x=15
        self.direction_y=5

    def get_coordinate(self, letter):
        if letter == "x":
            return self.x
        elif letter == "y":
            return self.y
        else:
            return "wrong letter"

    def move(self):
        self.x += self.direction_x
        self.y += self.direction_y

    def paddle_collision(self):
        self.direction_y= -self.direction_y

    def side_wall_collision(self):
        self.direction_x = -self.direction_x

    def top_wall_collision(self):
        self.direction_y = -self.direction_y
