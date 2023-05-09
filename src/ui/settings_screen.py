import pygame
from ui.button import Button
from ui.date import Date
RED = (255, 20, 20)
WHITE = (200, 200, 200)
PINK = (255, 151, 231)
YELLOW = (250, 238, 108)
BLACK = (0, 0, 0)


class SettingsScreen:
    """Luokka, joka vastaa asetukset näytöstä.

    Attributes:
        screen: näyttö, johon grafiikat piirretään
        settings: asetukset, joita näytössä voi muokata
    """

    def __init__(self, screen, settings):
        """Luokan konstuktori, joka alustaa näytön, fontit ja painikkeet.

        Args:
            screen: näyttö, johon grafiikat piirretään
            settings: asetukset, joita näytössä voi muokata
        """
        self.screen = screen
        self.settings = settings
        self.font_medium = pygame.font.SysFont("arial", 30, bold=True)
        self.font_small = pygame.font.SysFont("arial", 20, bold=True)
        self.button_mouse = Button(
            self.screen, 400, 150, 150, 50, WHITE)
        self.button_keyboard = Button(
            self.screen, 200, 150, 150, 50, WHITE)
        self.ball_color_1 = Button(
            self.screen, 300, 300, 40, 40, WHITE)
        self.ball_color_2 = Button(
            self.screen, 400, 300, 40, 40, PINK)
        self.ball_color_3 = Button(
            self.screen, 500, 300, 40, 40, YELLOW)
        self.paddle_color_1 = Button(
            self.screen, 300, 400, 40, 40, WHITE)
        self.paddle_color_2 = Button(
            self.screen, 400, 400, 40, 40, PINK)
        self.paddle_color_3 = Button(
            self.screen, 500, 400, 40, 40, YELLOW)

    def draw_screen(self):
        """Piirtää ruudulle oikeat grafiikat.
        """
        pygame.display.set_caption("Pong")
        mouse_text = self.font_small.render("mouse", 0, BLACK)
        keyboard_text = self.font_small.render("keyboard", 0, BLACK)
        back_text = self.font_small.render("enter: back", 0, WHITE)
        self.screen.fill(BLACK)
        settings_text = self.font_medium.render(
            "Choose settings :", 0, WHITE)
        ball_color_text = self.font_medium.render(
            "Ball color:", 0, WHITE)
        paddle_color_text = self.font_medium.render(
            "Paddle color:", 0, WHITE)
        self.screen.blit(settings_text, (50, 50))
        self.screen.blit(ball_color_text, (50, 300))
        self.screen.blit(paddle_color_text, (50, 400))
        self.screen.blit(back_text, (10, 470))
        self.button_keyboard.draw_button()
        self.button_mouse.draw_button()
        self.ball_color_1.draw_button()
        self.ball_color_2.draw_button()
        self.ball_color_3.draw_button()
        self.paddle_color_1.draw_button()
        self.paddle_color_2.draw_button()
        self.paddle_color_3.draw_button()
        self.screen.blit(keyboard_text, (235, 160))
        self.screen.blit(mouse_text, (445, 160))
        if self.settings.mover == "keyboard":
            pygame.draw.rect(self.screen, RED, (200, 150, 150, 50), 5)
        else:
            pygame.draw.rect(self.screen, RED, (400, 150, 150, 50), 5)
        if self.settings.paddle_color == WHITE:
            pygame.draw.rect(self.screen, RED, (300, 400, 40, 40), 5)
        elif self.settings.paddle_color == PINK:
            pygame.draw.rect(self.screen, RED, (400, 400, 40, 40), 5)
        else:
            pygame.draw.rect(self.screen, RED, (500, 400, 40, 40), 5)
        if self.settings.ball_color == WHITE:
            pygame.draw.rect(self.screen, RED, (300, 300, 40, 40), 5)
        elif self.settings.ball_color == PINK:
            pygame.draw.rect(self.screen, RED, (400, 300, 40, 40), 5)
        else:
            pygame.draw.rect(self.screen, RED, (500, 300, 40, 40), 5)
        Date().draw_date(self.screen)
        pygame.display.flip()

    def loop(self):
        """Asetukset-näkymän silmukka, joka reagoi käyttäjän syötteisiin ja muokkaa asetukset-luokkaa sen mukaan, mitä painiketta painetaan.
        """
        while True:
            self.draw_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_RETURN:
                        return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_keyboard.chech_if_button_pressed():
                        self.settings.mover = "keyboard"
                    if self.button_mouse.chech_if_button_pressed():
                        self.settings.mover = "mouse"
                    if self.ball_color_1.chech_if_button_pressed():
                        self.settings.ball_color = (200, 200, 200)
                    if self.ball_color_2.chech_if_button_pressed():
                        self.settings.ball_color = (255, 151, 231)
                    if self.ball_color_3.chech_if_button_pressed():
                        self.settings.ball_color = (250, 238, 108)
                    if self.paddle_color_1.chech_if_button_pressed():
                        self.settings.paddle_color = (200, 200, 200)
                    if self.paddle_color_2.chech_if_button_pressed():
                        self.settings.paddle_color = (255, 151, 231)
                    if self.paddle_color_3.chech_if_button_pressed():
                        self.settings.paddle_color = (250, 238, 108)
