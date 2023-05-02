import pygame
from ui.settings_screen import SettingsScreen


class Start:
    """Luokka, joka vastaa aloitusnäkymän käyttöliittymästä.

    Attributes:
        screen: näyttö, johon grafiikat piirretään
        settings: asetukset, joita pelissä käytetään
    """

    def __init__(self, screen, settings):
        """Luokan konstruktori, joka luo pohjan aloitusnäytölle.

        Args:
            screen: näyttö, johon grafiikat piirretään
            settings: asetukset, joita pelissä käytetään
            font: isoin käytettävä fontti
            font_medium: keskikokoinen fontti
            font_small: pieni fontti
            username_rect: suorakulmio, joka sisään käyttäjänimi kirjoitetaan
            login_fail: pitää kirjaa siitä, onko peli yritetty aloittaa ilman käyttäjänimeä
        """

        self.screen = screen
        self.settings = settings
        self.font = pygame.font.SysFont("arial", 60, bold=True)
        self.font_medium = pygame.font.SysFont("arial", 30, bold=True)
        self.font_small = pygame.font.SysFont("arial", 20, bold=True)
        self.username_rect = pygame.Rect(120, 10, 140, 32)
        self.login_fail = False

    def draw_screen(self):
        """Piiträä ruudulle oikeat grafiikat.
        """
        pygame.display.set_caption("Pong")
        self.screen.fill((0, 0, 0))
        text1 = self.font.render("Pong", 0, (200, 200, 200))
        text2 = self.font_medium.render(
            "write username and press enter to start", 0, (200, 200, 200))
        text3 = self.font_small.render("username:", 0, (200, 200, 200))
        username_text = self.font_small.render(
            self.settings.username, 0, (200, 200, 200))
        screen_width = self.screen.get_width()
        text1_width = text1.get_width()
        text2_width = text2.get_width()
        if self.login_fail == True and self.settings.username == "":
            pygame.draw.rect(self.screen, (255, 20, 20), self.username_rect, 2)
        else:
            pygame.draw.rect(self.screen, (200, 200, 200),
                             self.username_rect, 2)
        self.screen.blit(text1, ((screen_width//2)-(text1_width//2), 150))
        self.screen.blit(text2, ((screen_width//2)-(text2_width//2), 250))
        self.screen.blit(text3, (10, 10))
        self.screen.blit(
            username_text, ((self.username_rect.x + 5), self.username_rect.y + 5))
        self.username_rect.w = max(100, username_text.get_width() + 10)
        settings_text = self.font_small.render("settings", 0, (0, 0, 0))
        pygame.draw.rect(self.screen, (200, 200, 200), (580, 10, 110, 32))
        self.screen.blit(settings_text, (600, 12))
        pygame.display.flip()

    def loop(self):
        """Aloitusruudun silmukka, joka reagoi käyttäjän syötteisiin.
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
                        if self.settings.username != "":
                            return
                        self.login_fail = True
                    elif event.key == pygame.K_BACKSPACE:
                        self.settings.username = self.settings.username[:-1]
                    else:
                        self.settings.username += event.unicode

                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 580 <= mouse[0] <= 690 and 10 <= mouse[1] <= 42:
                        SettingsScreen(self.screen, self.settings).loop()
