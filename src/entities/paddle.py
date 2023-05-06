class Paddle:
    """Luokka, jonka avulla ylläpidetään laudan koordinaatteja ja liikkumisen tilaa.

    Attributes:
        color: Laudan väri
        x_coord: Laudan x-koordinaatti
        y_coord: Laudan y-koordinaatti
        width: Laudan leveys
        height: Laudan korkeus
    """

    def __init__(self, color, x_coord, y_coord, height, settings):
        """Luokan konstruktori, joka luo uuden laudan.

        Args:
            color: Laudan väri
            x_coord: Laudan x-koordinaatti
            y_coord: Laudan y-koordinaatti
            width: Laudan leveys
            height: Laudan korkeus
            mode: Laudan liikkumisen tila
        """
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.settings = settings
        self.width = settings.paddle_width
        self.height = height
        self.mode = "still"

    def get_coordinate(self, letter):
        """Kertoo laudan sen hetkisen sijainnin.

        Args:
            letter: Halutun koordinaatin kirjain

        Returns:
            Kysytyn koordinaatin numeron, jos kirjain on x tai y, muuten "wrong letter"
        """
        if letter == "y":
            return self.y_coord
        if letter == "x":
            return self.x_coord
        return "wrong letter"

    def move(self):
        """Muuttaa laudan x-koordinaattia sen mukaan, mika laudan liikkumisen tila on.
        """
        if self.mode == "left":
            self.x_coord -= 10

        elif self.mode == "right":
            self.x_coord += 10

        else:
            self.x_coord = self.x_coord

        if self.x_coord <= 0:
            self.x_coord = 0

        elif self.x_coord >= 700-self.settings.paddle_width:
            self.x_coord = 700-self.settings.paddle_width
