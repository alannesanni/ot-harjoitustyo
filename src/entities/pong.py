import pygame
from entities.paddle import Paddle

class Pong:
    def __init__(self):
        self.width=700
        self.height=500
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.paddle_x=5
        self.paddle_y=480
        self.paddle_color=(200,200,200)
        self.paddle=Paddle(self.paddle_color, self.paddle_x, self.paddle_y,120,20)
        self.loop()

    def loop(self):
        clock = pygame.time.Clock()
        while True:
            self.draw_screen()
            self.paddle.move()
            self.paddle_x=self.paddle.get_coordinate("x")
            self.draw_paddle()
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

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.paddle_color, (self.paddle_x, self.paddle_y, 120, 20))
    
    def draw_screen(self):
        self.screen.fill((0,0,0))
        self.draw_paddle()
        pygame.display.flip()
