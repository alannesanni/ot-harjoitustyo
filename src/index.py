import pygame
from entities.pong import Pong
from entities.settings import Settings
from ui.gameover import GameOver
from ui.start import Start
from repositories.score_repository import ScoreDatabase
from repositories.database_connection import get_database_connection


def main():
    """Funktio, joka hallitsee sitä, mikä funktio näkyy milloinkin.
    """
    pygame.init()
    width = 700
    height = 500
    settings = Settings()
    connection = get_database_connection()
    ScoreDatabase(connection).create_database()
    while True:
        screen = pygame.display.set_mode((width, height))
        pong = Pong(screen, settings)
        start = Start(screen, settings)
        gameover = GameOver(pong, screen, connection, settings)
        start.loop()
        pong.loop()
        ScoreDatabase(connection).add_score(
            settings.username, pong.score.points, settings.level)
        gameover.loop()


if __name__ == "__main__":
    main()
