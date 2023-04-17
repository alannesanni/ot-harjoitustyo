import pygame


class Start:
    def __init__(self, screen):

        self.screen = screen
        self.font = pygame.font.SysFont("arial", 60, bold=True)

    def draw_screen(self):
        pygame.display.set_caption("Pong")
        self.screen.fill((0, 0, 0))
        text1 = self.font.render("Pong", 0, (200, 200, 200))
        text2 = self.font.render("Press enter to start", 0, (200, 200, 200))
        screen_width = self.screen.get_width()
        text1_width = text1.get_width()
        text2_width = text2.get_width()
        self.screen.blit(text1, ((screen_width//2)-(text1_width//2), 150))
        self.screen.blit(text2, ((screen_width//2)-(text2_width//2), 250))
        pygame.display.flip()
        self.loop()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
