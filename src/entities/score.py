class Score:
    """Luokka, joka vastaa pisteiden laskusta.

    Attributes: 
            points: Pisteiden määrä
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden pistelaskurin
        """
        self.points = 0

    def add_point(self):
        """Kasvattaa pisteiden määrää yhdellä.
        """
        self.points += 1
