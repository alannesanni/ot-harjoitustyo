class Ball:
    """Luokka, jonka avulla ylläpidetään pallon koordinaatteja ja suuntaa.

    Attributes:
        color: Pallon väri
        x_coord: Pallon x-koordinaatti
        y_coord: Pallon y-koordinaatti
        radius: Pallon säde
        settings: Käytettävät asetukset
    """

    def __init__(self, color, x_coord, y_coord, radius, settings):
        """Luokan konstruktori, joka luo uuden pallon.

        Args:
            color: Pallon väri
            x_coord: Pallon x-koordinaatti
            y_coord: Pallon y-koordinaatti
            radius: Pallon säde
            settings: Asetukset, joista haetaan pallon suunnat
        """
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.radius = radius
        self.settings = settings

    def get_coordinate(self, letter):
        """Kertoo pallon sen hetkisen sijainnin

        Args:
            letter: Halutun koordinaatin kirjain

        Returns:
            Kysytyn koordinaatin numeron, jos kirjain on x tai y, muuten "wrong letter"
        """
        if letter == "x":
            return self.x_coord
        if letter == "y":
            return self.y_coord
        return "wrong letter"

    def move(self):
        """Liikuttaa palloa yhden askeleen x- ja y-akselilla
        """
        self.x_coord += self.settings.ball_direction_x
        self.y_coord += self.settings.ball_direction_y

    def paddle_collision(self):
        """Vaihtaa y-akselin suuntaa
        """
        self.settings.ball_direction_y = -self.settings.ball_direction_y

    def paddle_side_collision(self):
        """Vaihtaa x-akselin suuntaa
        """
        self.settings.ball_direction_x = -self.settings.ball_direction_x

    def side_wall_collision(self):
        """Vaihtaa x-akselin suuntaa
        """
        self.settings.ball_direction_x = -self.settings.ball_direction_x

    def top_wall_collision(self):
        """Vaihtaa y-akselin suuntaa
        """
        self.settings.ball_direction_y = -self.settings.ball_direction_y
