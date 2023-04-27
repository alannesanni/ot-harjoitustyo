class Score:
    """Luokka, joka vastaa pisteiden laskusta.
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden pistelaskurin

        Args:
            points: Pisteiden määrä
        """
        self.points = 0

    def add_point(self):
        """Kasvattaa pisteiden määrää yhdellä.
        """
        self.points += 1
