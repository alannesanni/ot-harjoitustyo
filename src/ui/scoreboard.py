from repositories.score_repository import ScoreDatabase
import pygame

class ScoreBoard:
    def __init__(self, screen, database):
        self.screen=screen
        self.font = pygame.font.SysFont("arial", 30, bold=True)
        self.db=database
        self.top_list=self.db.get_top_5()

    def draw_screen(self):
        y_coord=100
        rank = 1
        pygame.display.set_caption("Pong")
        self.screen.fill((0, 0, 0))
        highscores_text = self.font.render(
            "Highscores: ", 0, (200, 200, 200))
        self.screen.blit(
            highscores_text, (50, 50))
        info_text = self.font.render("enter: back   |   esc: quit", 0, (200,200,200))
        self.screen.blit(info_text, (20,450) )
        for i in self.top_list:
            score_text=self.font.render(f"{rank}.  {i[0]}  {i[1]}", 0, (200, 200, 200))
            self.screen.blit(score_text, (50, y_coord))
            y_coord+=40
            rank+=1
        pygame.display.flip()

    def loop(self):
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
