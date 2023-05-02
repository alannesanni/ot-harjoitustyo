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
        """
        self.mover = "keyboard"
        self.ball_color = (200, 200, 200)
        self.paddle_color = (200, 200, 200)
        self.username = ""
