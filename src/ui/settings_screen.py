import pygame
from ui.button import Button
RED=(255,20,20)
class SettingsScreen:
    """Luokka, joka vastaa asetukset näytöstä.

    Attributes:
        screen: näyttö, johon grafiikat piirretään
        settings: asetukset, joita näytössä voi muokata
    """
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings=settings
        self.font_medium = pygame.font.SysFont("arial", 30, bold=True)
        self.font_small = pygame.font.SysFont("arial", 20, bold=True)
        self.button_mouse=Button(self.screen, 400, 150, 150, 50, (200,200,200))
        self.button_keyboard=Button(self.screen, 200, 150, 150, 50, (200,200,200))
        self.ball_color_1=Button(self.screen, 300, 300, 40, 40, (200,200,200))
        self.ball_color_2=Button(self.screen, 400, 300, 40, 40, (255, 151, 231))
        self.ball_color_3=Button(self.screen, 500, 300, 40, 40, (250, 238, 108))
        self.paddle_color_1=Button(self.screen, 300, 400, 40, 40, (200,200,200))
        self.paddle_color_2=Button(self.screen, 400, 400, 40, 40, (255, 151, 231))
        self.paddle_color_3=Button(self.screen, 500, 400, 40, 40, (250, 238, 108))
    
    def draw_screen(self):
        pygame.display.set_caption("Pong")
        mouse_text=self.font_small.render("mouse", 0, (0,0,0))
        keyboard_text=self.font_small.render("keyboard", 0, (0,0,0))
        self.screen.fill((0, 0, 0))
        ball_color_text=self.font_medium.render("Ball color:", 0, (200,200,200))
        paddle_color_text=self.font_medium.render("Paddle color:", 0, (200,200,200))
        self.screen.blit(ball_color_text, (50,300))
        self.screen.blit(paddle_color_text, (50,400))
        self.button_keyboard.draw_button()
        self.button_mouse.draw_button()
        self.ball_color_1.draw_button()
        self.ball_color_2.draw_button()
        self.ball_color_3.draw_button()
        self.paddle_color_1.draw_button()
        self.paddle_color_2.draw_button()
        self.paddle_color_3.draw_button()
        self.screen.blit(keyboard_text, (235,160))
        self.screen.blit(mouse_text, (445,160))
        if self.settings.mover=="keyboard":
            pygame.draw.rect(self.screen, RED, (200,150,150,50), 5)
        else:
            pygame.draw.rect(self.screen, RED, (400,150,150,50), 5)
        if self.settings.paddle_color==(200,200,200):
            pygame.draw.rect(self.screen, RED, (300, 400, 40, 40), 5)
        elif self.settings.paddle_color==(255, 151, 231):
            pygame.draw.rect(self.screen, RED, (400, 400, 40, 40), 5)
        else:
            pygame.draw.rect(self.screen, RED, (500, 400, 40, 40), 5)
        if self.settings.ball_color==(200,200,200):
            pygame.draw.rect(self.screen, RED, (300, 300, 40, 40), 5)
        elif self.settings.ball_color==(255, 151, 231):
            pygame.draw.rect(self.screen, RED, (400, 300, 40, 40), 5)
        else:
            pygame.draw.rect(self.screen, RED, (500, 300, 40, 40), 5)
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
                        return
    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_keyboard.chech_if_button_pressed():
                        self.settings.mover="keyboard"
                    if self.button_mouse.chech_if_button_pressed():
                        self.settings.mover="mouse"
                    if self.ball_color_1.chech_if_button_pressed():
                        self.settings.ball_color=(200,200,200)
                    if self.ball_color_2.chech_if_button_pressed():
                        self.settings.ball_color=(255, 151, 231)
                    if self.ball_color_3.chech_if_button_pressed():
                        self.settings.ball_color=(250, 238, 108)
                    if self.paddle_color_1.chech_if_button_pressed():
                        self.settings.paddle_color=(200,200,200)
                    if self.paddle_color_2.chech_if_button_pressed():
                        self.settings.paddle_color=(255, 151, 231)
                    if self.paddle_color_3.chech_if_button_pressed():
                        self.settings.paddle_color=(250, 238, 108)