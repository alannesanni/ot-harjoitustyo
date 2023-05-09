import pygame
from datetime import datetime

GREY = (80, 80, 80)


class Date:
    """Luokka, jonka avulla voidaan lisätä näytölle sen hetkinen aika.
    """
    
    def draw_date(self, screen):
        """Piirtää näytölle ajan oikeaan alakulmaan.

        Args:
            screen: näyttö, jolle aika piirretään
        """
        font = pygame.font.SysFont("arial", 15)
        date = datetime.now().strftime("%H:%M %d/%m/%Y")
        date_text = font.render(date, 0, GREY)
        size = font.size(date)
        screen.blit(date_text, (700-size[0], 500-size[1]))
