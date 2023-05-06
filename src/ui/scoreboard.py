from repositories.score_repository import ScoreDatabase
import pygame


class ScoreBoard:
    """Luokka, joka vastaa tulostaulun käyttöliittymästä.

    Attributes:
        screen: Näyttö, jolle grafiikat piirretään
        database_connection: Luo yhteyden tietokantaan
    """

    def __init__(self, screen, database_connection, settings):
        """Luokan konstruktori joka alustaa käytetyt atribuutit

        Args:
            screen: Näyttö, jolle grafiikat piirretään
            font: Fontti, jota piirtämisessä käytetään
            db_connection: Luo yhteyden tietokantaan
            top_list: Hakee listaan tietokannasta viisi parasta tulosta
        """
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 30, bold=True)
        self.db_connection = database_connection
        self.settings = settings
        self.top_list = ScoreDatabase(
            self.db_connection).get_top_5(self.settings.level)

    def draw_screen(self):
        """Piirtää näytölle tulostaulun grafiikat.
        """
        y_coord = 100
        rank = 0
        pygame.display.set_caption("Pong")
        self.screen.fill((0, 0, 0))
        highscores_text = self.font.render(
            "Highscores: ", 0, (200, 200, 200))
        self.screen.blit(
            highscores_text, (50, 50))
        info_text = self.font.render(
            "enter: back   |   esc: quit", 0, (200, 200, 200))
        self.screen.blit(info_text, (20, 450))
        previous = "first"
        for i in self.top_list:
            if i[1] != previous[1] or previous == "first":
                rank += 1
            score_text = self.font.render(
                f"{rank}.  {i[0]}  {i[1]}", 0, (200, 200, 200))
            self.screen.blit(score_text, (50, y_coord))
            y_coord += 40

            previous = i
        pygame.display.flip()

    def loop(self):
        """Tulostaulun näytön silmukka, joka reagoi käyttäjän syötteisiin.
        """
        self.draw_screen()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_RETURN:
                        return
