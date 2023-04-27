class Ball:
    """Luokka, jonka avulla ylläpidetään pallon koordinaatteja ja suuntaa.

    Attributes:
        color: Pallon väri
        x_coord: Pallon x-koordinaatti
        y_coord: Pallon y-koordinaatti
        radius: Pallon säde
    """
    def __init__(self, color, x_coord, y_coord, radius):
        """Luokan konstruktori, joka luo uuden pallon.

        Args:
            color: Pallon väri
            x_coord: Pallon x-koordinaatti
            y_coord: Pallon y-koordinaatti
            radius: Pallon säde
            direction_x: Pallon x-akselilla kulkema matka ja suunta
            direction_y: Pallon y-alkselilla kulkema matka ja suunta
        """
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.radius = radius
        self.direction_x = 13
        self.direction_y = 5

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
        self.x_coord += self.direction_x
        self.y_coord += self.direction_y

    def paddle_collision(self):
        """Vaihtaa y-akselin suuntaa
        """
        self.direction_y = -self.direction_y

    def paddle_side_collision(self):
        """Vaihtaa x-akselin suuntaa
        """
        self.direction_x = -self.direction_x

    def side_wall_collision(self):
        """Vaihtaa x-akselin suuntaa
        """
        self.direction_x = -self.direction_x

    def top_wall_collision(self):
        """Vaihtaa y-akselin suuntaa
        """
        self.direction_y = -self.direction_y
