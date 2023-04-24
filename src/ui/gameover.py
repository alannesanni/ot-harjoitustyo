import pygame
from ui.scoreboard import ScoreBoard

class GameOver:
    def __init__(self, game, screen, database):
        self.game = game
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 60, bold=True)
        self.font_small = pygame.font.SysFont("arial", 20, bold=True)
        self.database=database

    def draw_screen(self):
        pygame.display.set_caption("Pong")
        self.screen.fill((0, 0, 0))
        end_score = self.font.render(
            "Score: " + str(self.game.score.points), 0, (200, 200, 200))
        game_over = self.font.render("GAME OVER", 0, (200, 200, 200))
        info_text = self.font_small.render("space: highscores   |   enter: new game   |   esc: quit", 0, (200,200,200))
        screen_width = self.screen.get_width()
        end_score_width = end_score.get_width()
        game_over_width = game_over.get_width()
        self.screen.blit(
            game_over, ((screen_width//2)-(game_over_width//2), 150))
        self.screen.blit(
            end_score, ((screen_width//2)-(end_score_width//2), 250))
        self.screen.blit(info_text, (20,450))
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
                    if event.key == pygame.K_SPACE:
                        ScoreBoard(self.screen, self.database).loop()
