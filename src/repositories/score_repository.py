import sqlite3


class ScoreDatabase:
    """Luokka, joka vastaa tietojen tallennuksesta.

    Attributes:
        connection: yhteys haluttuun tietokantaan
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka alustaa yhteyden tietokantaan.

        Args:
            connection: yhteys haluttuun tietokantaan
        """
        self.database_connection = connection

    def create_database(self):
        """Luo tietokantaan oikeat taulut, jos tietokanta on tyhjä.
        """
        try:
            self.create_table()
        except sqlite3.OperationalError:
            pass

    def create_table(self):
        """Luo tietokantaan eri vaikeustasoille omat taulut.
        """
        self.database_connection.execute(
            "CREATE TABLE EasyScores (id INTEGER PRIMARY KEY, username TEXT, score INTEGER);")
        self.database_connection.execute(
            "CREATE TABLE MediumScores (id INTEGER PRIMARY KEY, username TEXT, score INTEGER);")
        self.database_connection.execute(
            "CREATE TABLE HardScores (id INTEGER PRIMARY KEY, username TEXT, score INTEGER);")

    def add_score(self, name, score, level):
        """Lisää oikeaan tulokset tauluun tuloksen.

        Args:
            name: pelaajan käyttäjänimi
            score: pelaajan tulos
            level: mihin tauluun tulos lisätään
        """
        if level == "easy":
            self.database_connection.execute(
                "INSERT INTO EasyScores (username, score) VALUES (?,?);", (name, score))
        if level == "medium":
            self.database_connection.execute(
                "INSERT INTO MediumScores (username, score) VALUES (?,?);", (name, score))
        if level == "hard":
            self.database_connection.execute(
                "INSERT INTO HardScores (username, score) VALUES (?,?);", (name, score))

        self.database_connection.commit()

    def get_all(self, level):
        """Hakee tietokannasta kaikki tulokset lisäysjärjestyksessä.

        Args:
            level: kertoo mistä taulusta tulokset haetaan     

        Returns:
            lista kaikista tuloksista
        """

        if level == "easy":
            get_all = "SELECT username, score FROM EasyScores ORDER BY score;"
        if level == "medium":
            get_all = "SELECT username, score FROM MediumScores ORDER BY score;"

        if level == "hard":
            get_all = "SELECT username, score FROM HardScores ORDER BY score;"

        return self.database_connection.execute(get_all).fetchall()



    def get_top_5(self, level):
        """Hakee tietokannasta viisi parasta tulosta.

        Args:
            level: kertoo mistä taulusta tulokset haetaan     

        Returns:
            lista viidestä parhaasta tuloksesta ja käyttäjänimistä parhaimmasta huonoimpaan
        """
        if level == "easy":
            get_5 = "SELECT username, score FROM EasyScores ORDER BY score DESC, id LIMIT 5;"
        if level == "medium":
            get_5 = "SELECT username, score FROM MediumScores ORDER BY score DESC, id LIMIT 5;"
        if level == "hard":
            get_5 = "SELECT username, score FROM HardScores ORDER BY score DESC, id LIMIT 5;"

        return self.database_connection.execute(get_5).fetchall()
