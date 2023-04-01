import pygame
from entities.pong import Pong
from entities.paddle import Paddle

def main():
    pygame.init()
    Pong().loop()

if __name__ == "__main__":
    main()