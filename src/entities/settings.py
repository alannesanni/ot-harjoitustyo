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
            self.ball_direction_x = 12
            self.ball_direction_y = 4
            self.paddle_width = 200

        if level == "medium":
            self.ball_direction_x = 13
            self.ball_direction_y = 5
            self.paddle_width = 120

        if level == "hard":
            self.ball_direction_x = 17
            self.ball_direction_y = 7
            self.paddle_width = 70
