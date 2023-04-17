import sys
import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from entities.collisions import Collisions
from entities.score import Score


class Pong:
    def __init__(self, screen):
        pygame.display.set_caption("Pong")
        self.width = 700
        self.height = 500
        # self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen = screen
        self.paddle_x = 5
        self.paddle_y = 480
        self.paddle_color = (200, 200, 200)
        self.paddle = Paddle(
            self.paddle_color, self.paddle_x, self.paddle_y, 120, 20)
        self.ball_color = (200, 200, 200)
        self.ball_x = 350
        self.ball_y = 250
        self.ball = Ball(self.ball_color, self.ball_x, self.ball_y, 10)
        self.collision = Collisions()
        self.score = Score()
        self.font = pygame.font.SysFont("arial", 60, bold=True)

    def loop(self):
        clock = pygame.time.Clock()
        while True:
            if self.ball_y >= 500:
                break
            self.draw_screen()
            self.paddle.move()
            self.ball.move()
            self.ball_x = self.ball.get_coordinate("x")
            self.ball_y = self.ball.get_coordinate("y")
            self.paddle_x = self.paddle.get_coordinate("x")
            self.draw_paddle()
            self.draw_ball()

            # collisions
            if self.collision.ball_and_paddle(self.ball, self.paddle):
                self.ball.paddle_collision()
                self.score.add_point()

            if self.collision.ball_and_paddle_side(self.ball, self.paddle):
                self.ball.paddle_side_collision()
                self.score.add_point()

            if self.collision.ball_and_side(self.ball):
                self.ball.side_wall_collision()

            if self.collision.ball_and_top(self.ball):
                self.ball.top_wall_collision()

            self.events()
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

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.paddle_color,
                         (self.paddle_x, self.paddle_y, 120, 20))

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.ball_color,
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
