import pygame
from entities.pong import Pong
from ui.gameover import GameOver
from ui.start import Start


def main():
    pygame.init()
    width = 700
    height = 500
    screen = pygame.display.set_mode((width, height))
    pong=Pong(screen)

    Start(screen).draw_screen()
    pong.loop()
    GameOver(pong, screen).draw_screen()


if __name__ == "__main__":
    main()
