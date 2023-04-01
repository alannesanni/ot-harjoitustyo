import pygame
class Paddle:
    def __init__(self, screen, color, x, y, width, height):
        self.screen = screen
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.mode= "still"
    

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        if self.mode == "left":
            self.x -= 10

        elif self.mode == "right":
            self.x += 10

        if self.x <= 0:
            self.x = 0

        elif self.x >= 580:
            self.x = 580
