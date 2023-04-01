import pygame
from entities.paddle import Paddle

class Pong:
    def __init__(self):
        self.width=700
        self.height=500
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.paddle=Paddle(self.screen, (200,200,200), 5,480,120,20)
        self.loop()

    def loop(self):
        clock = pygame.time.Clock()
        while True:
            self.draw_screen()
            self.paddle.move()
            self.paddle.show()
            self.events()
            clock.tick(50)
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.paddle.mode = "left"
                if event.key == pygame.K_RIGHT:
                    self.paddle.mode = "right"

            if event.type == pygame.KEYUP:
                self.paddle.mode = "still"

    def draw_screen(self):
        self.screen.fill((0,0,0))
        self.paddle.show()
        pygame.display.flip()
