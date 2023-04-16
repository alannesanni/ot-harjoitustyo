import pygame
from entities.pong import Pong


def main():
    pygame.init()
    Pong().loop()


if __name__ == "__main__":
    main()
