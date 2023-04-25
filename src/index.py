import pygame
from entities.pong import Pong
from ui.gameover import GameOver
from ui.start import Start
from repositories.score_repository import ScoreDatabase
from repositories.database_connection import get_database_connection


def main():
    pygame.init()
    width = 700
    height = 500
    connection = get_database_connection()
    ScoreDatabase(connection).create_database()
    while True:
        screen = pygame.display.set_mode((width, height))
        pong = Pong(screen)
        start = Start(screen)
        gameover = GameOver(pong, screen, connection)
        start.loop()
        pong.loop()
        ScoreDatabase(connection).add_score(start.username, pong.score.points)
        gameover.loop()


if __name__ == "__main__":
    main()
