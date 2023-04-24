import pygame


class Start:
    def __init__(self, screen):

        self.screen = screen
        self.font = pygame.font.SysFont("arial", 60, bold=True)
        self.font_medium = pygame.font.SysFont("arial", 30, bold=True)
        self.font_small = pygame.font.SysFont("arial", 20, bold=True)
        self.username = ""
        self.username_rect = pygame.Rect(120,10,140,32)


    def draw_screen(self):
        pygame.display.set_caption("Pong")
        self.screen.fill((0, 0, 0))
        text1 = self.font.render("Pong", 0, (200, 200, 200))
        text2 = self.font_medium.render("write username and press enter to start", 0, (200, 200, 200))
        text3 = self.font_small.render("username:", 0, (200,200,200))
        username_text = self.font_small.render(self.username, 0, (200,200,200))
        screen_width = self.screen.get_width()
        text1_width = text1.get_width()
        text2_width = text2.get_width()
        pygame.draw.rect(self.screen,(200,200,200), self.username_rect, 2)
        self.screen.blit(text1, ((screen_width//2)-(text1_width//2), 150))
        self.screen.blit(text2, ((screen_width//2)-(text2_width//2), 250))
        self.screen.blit(text3, (10,10))
        self.screen.blit(username_text, ((self.username_rect.x + 5),self.username_rect.y + 5) )
        self.username_rect.w = max(100, username_text.get_width() + 10)
        pygame.display.flip()

    def loop(self):
        while True:
            self.draw_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_RETURN:
                        if self.username!="":
                            return
                    elif event.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    else:
                        self.username += event.unicode