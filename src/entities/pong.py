import sys
import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from entities.collisions import Collisions
from entities.score import Score

WHITE=(200,200,200)

class Pong:
    def __init__(self, screen):
        pygame.display.set_caption("Pong")
        self.screen = screen
        self.paddle_x = 5
        self.paddle_y = 480
        self.paddle = Paddle(
            WHITE, self.paddle_x, self.paddle_y, 120, 20)
        self.ball_x = 350
        self.ball_y = 150
        self.ball = Ball(WHITE, self.ball_x, self.ball_y, 10)
        self.collision = Collisions()
        self.score = Score()
        self.font = pygame.font.SysFont("arial", 60, bold=True)

    def loop(self):
        clock = pygame.time.Clock()
        while True:
            if self.ball_y >= 500:
                break
            self.draw_screen()
            self.ball.move()
            self.paddle.move()
            self.ball_x = self.ball.get_coordinate("x")
            self.ball_y = self.ball.get_coordinate("y")
            self.paddle_x = self.paddle.get_coordinate("x")
            self.draw_paddle()
            self.draw_ball()

            self.events()
            self.check_collisions()

            clock.tick(30)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.paddle.mode = "left"

                if event.key == pygame.K_RIGHT:
                    self.paddle.mode = "right"

            if event.type == pygame.KEYUP:
                self.paddle.mode = "still"

    def check_collisions(self):
        if self.collision.ball_and_paddle(self.ball, self.paddle):
            self.ball.paddle_collision()
            self.score.add_point()
        if self.collision.ball_and_paddle_side(self.ball, self.paddle):
            self.ball.paddle_side_collision()
            self.score.add_point()
            for _ in range(4):
                self.ball.move()
                self.ball_x = self.ball.get_coordinate("x")
                self.ball_y = self.ball.get_coordinate("y")
                self.draw_ball()

        if self.collision.ball_and_side(self.ball):
            self.ball.side_wall_collision()

        if self.collision.ball_and_top(self.ball):
            self.ball.top_wall_collision()


    def draw_paddle(self):
        pygame.draw.rect(self.screen, WHITE,
                         (self.paddle_x, self.paddle_y, 120, 20))

    def draw_ball(self):
        pygame.draw.circle(self.screen, WHITE,
                           (self.ball_x, self.ball_y), 10)

    def draw_score(self):
        points_text = self.font.render(
            str(self.score.points), 0, (200, 200, 200))
        self.screen.blit(points_text, (10, 10))

    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        self.draw_score()
        self.draw_paddle()
        self.draw_ball()
        pygame.display.flip()
