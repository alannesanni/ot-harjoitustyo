import pygame


class Button():
    """Luokka, joka vastaa asetukset sivulla olevista painikkeista.

    Attribures:
        screen: Näyttö, jolle painike luodaan
        x_coord: Painikkeen x-koordinaatti
        y_coord: Painikkeen y-koordinaatti
        width: Painikkeen leveys
        height: Painikkeen korkeus
        color: Painikkeen väri
    """

    def __init__(self, screen, x_coord, y_coord, width, height, color):
        """Luokan konstruktori, joka luo uuden painikkeen.

        Args:
        screen: Näyttö, jolle painike luodaan
        x_coord: Painikkeen x-koordinaatti
        y_coord: Painikkeen y-koordinaatti
        width: Painikkeen leveys
        height: Painikkeen korkeus
        color: Painikkeen väri
        """
        self.screen = screen
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.color = color

    def draw_button(self):
        """Piirtää halutun painikkeen näytölle.
        """
        pygame.draw.rect(self.screen, self.color, (self.x_coord,
                         self.y_coord, self.width, self.height))

    def chech_if_button_pressed(self):
        """Tarkistaa onko hiiri painikkeen päällä.

        Returns:
            Jos hiiri on painikkeen päällä, palauttaa True, muuten False.
        """
        mouse = pygame.mouse.get_pos()
        if self.x_coord <= mouse[0] <= self.x_coord+self.width and self.y_coord <= mouse[1] <= self.y_coord+self.height:
            return True
        return False
