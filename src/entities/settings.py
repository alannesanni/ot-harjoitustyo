class Settings:
    """Luokka, joka ylläpitää pelin muutettavia asetuksia.
    """

    def __init__(self):
        """Luokan konstruktori, joka asettaa pelin oletusasetukset.

        Args:
            mover: Tapa, jolla lautaa liikutetaan
            ball_color: Pallon väri
            paddle_color: Laudan väri
            username: Pelaajan käyttäjänimi
            ball_direction_x: pallon x suunta
            ball_direction_y: pallon y suunta
            paddle_width: laudan leveys
        """
        self.mover = "keyboard"
        self.ball_color = (200, 200, 200)
        self.paddle_color = (200, 200, 200)
        self.username = ""
        self.level = "medium"
        self.ball_direction_x = 13
        self.ball_direction_y = 5
        self.paddle_width = 120

    def change_level(self, level):
        """Vaihtaa pelin vaikeustasoa

        Args:
            level: vaikeustaso, jolle halutaan vaihtaa
        """
        if level == "easy":
            self.set_level(12, 4, 200)

        if level == "medium":
            self.set_level(13, 5, 120)

        if level == "hard":
            self.set_level(17, 7, 70)

    def set_level(self, ball_x_dir, ball_y_dir, paddle_width):
        """Asettaa halutut arvot asetuksiin.

        Args:
            x: Pallon x-akselilla kulkema matka
            y: Pallon y-akselilla kulkema matka
            w: Laudan leveys
        """
        self.ball_direction_x = ball_x_dir
        self.ball_direction_y = ball_y_dir
        self.paddle_width = paddle_width
