import sys
from random import randint
import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from entities.collisions import ball_and_paddle, ball_and_paddle_side, ball_and_side, ball_and_top
from entities.score import Score


WHITE = (200, 200, 200)
BLACK = (0, 0, 0)


class Pong:
    """Luokka, joka vastaa pelilogiikasta ja pelinäytön käyttöliittymästä

    Attributes:
            screen: Näyttö, jolle grafiikat piirretään
            settings: Peliin määritellyt asetukset
    """

    def __init__(self, screen, settings):
        """Luokan konstruktori, joka luo uuden pelin.

        Args:
            screen: Näyttö, jolle grafiikat piirretään
            settings: Peliin määritellyt asetukset
            paddle_x: Laudan aloitus x-koordinaatti, päivittyy pelin kuluessa
            paddle_y: Laudan y-koordinaatti
            paddle: Paddle-luokan avulla luotu lauta
            ball_x: Pallon aloitus x-koordinaatti, päivittyy pelin kuluessa
            ball_y: Pallon aloitus y-koordinaatti, päivittyy pelin kuluessa
            ball: Ball-luokan avulla luotu pallo
            score: Yhdistää mukaan Score-luokan

        """
        pygame.display.set_caption("Pong")
        self.screen = screen
        self.settings = settings
        self.paddle_x = 5
        self.paddle_y = 480
        self.paddle = Paddle(
            self.settings.paddle_color, self.paddle_x, self.paddle_y, 20, self.settings)
        self.ball_x = randint(15, 650)
        self.ball_y = randint(15, 50)
        self.ball = Ball(self.settings.ball_color,
                         self.ball_x, self.ball_y, 10, self.settings)
        self.score = Score()

    def loop(self):
        """Pelilogiikan pääsilmukka, joka kutsuu näytön piirto funktiota,
        päivittää pallon ja laudan koordinaatit ja tarkistaa törmäykset.
        """
        clock = pygame.time.Clock()

        while True:
            if self.ball_y >= 500:
                break
            self.paddle.move()
            self.ball.move()
            self.ball_x = self.ball.get_coordinate("x")
            self.ball_y = self.ball.get_coordinate("y")
            self.paddle_x = self.paddle.get_coordinate("x")
            self.check_collisions()
            self.draw_screen()
            self.events()
            clock.tick(30)

    def events(self):
        """Tarkistaa käyttäjältä tulevat syötteet ja toimii niille määritellyn ohjeen mukaisesti.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if self.settings.mover == "mouse":
                mouse_position = pygame.mouse.get_pos()
                if mouse_position[0] < self.paddle_x:
                    self.paddle.mode = "left"
                if mouse_position[0] > self.paddle_x+self.settings.paddle_width:
                    self.paddle.mode = "right"
                if self.paddle_x < mouse_position[0] < self.paddle_x+self.settings.paddle_width:
                    self.paddle.mode = "still"

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.paddle.mode = "left"

                    if event.key == pygame.K_RIGHT:
                        self.paddle.mode = "right"

                if event.type == pygame.KEYUP:
                    self.paddle.mode = "still"

    def check_collisions(self):
        """Tarkistaa pallon törmäykset ja muuttaa pallon suuntaa niiden mukaan. 
        Jos törmätään laudan sivuun, niin siirtää palloa sen hetkiseen suuntaan muutaman kerran,
        jotta vältetään bugi, jossa pallo jumittuu laudan sisälle.
        """
        if ball_and_paddle(self.ball, self.paddle):
            self.ball.paddle_collision()
            self.score.add_point()
        if ball_and_paddle_side(self.ball, self.paddle):
            self.ball.paddle_side_collision()
            self.score.add_point()
            for _ in range(4):
                self.ball.move()
                self.ball_x = self.ball.get_coordinate("x")
                self.ball_y = self.ball.get_coordinate("y")
                self.draw_ball()

        if ball_and_side(self.ball):
            self.ball.side_wall_collision()

        if ball_and_top(self.ball):
            self.ball.top_wall_collision()

    def draw_paddle(self):
        """Piirtää laudan ruudulle sen hetkisten koordinaattien mukaan.
        """
        pygame.draw.rect(self.screen, self.settings.paddle_color,
                         (self.paddle_x, self.paddle_y, self.settings.paddle_width, 20))

    def draw_ball(self):
        """Piirtää pallon ruudulle sen hetkisten koordinaattien mukaan.
        """
        pygame.draw.circle(self.screen, self.settings.ball_color,
                           (self.ball_x, self.ball_y), 10)

    def draw_score(self):
        """Piirtää pisteiden määrän ruudun vasempaan yläreunaan.
        """
        font = pygame.font.SysFont("arial", 60, bold=True)
        points_text = font.render(
            str(self.score.points), 0, WHITE)
        self.screen.blit(points_text, (20, 5))

    def draw_screen(self):
        """Piirtää näytölle pisteet, laudan ja pallon.
        """
        self.screen.fill(BLACK)
        self.draw_score()
        self.draw_paddle()
        self.draw_ball()
        pygame.display.flip()
