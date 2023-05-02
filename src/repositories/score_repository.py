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
        """Luo tietokantaan oikean taulun, jos tietokanta on tyhjä.
        """
        try:
            self.create_table()
        except sqlite3.OperationalError:
            pass

    def create_table(self):
        """Luo tietokantaan tulokset taulun.
        """
        self.database_connection.execute(
            "CREATE TABLE Scores (id INTEGER PRIMARY KEY, username TEXT, score INTEGER);")

    def add_score(self, name, score):
        """Lisää tulkset tauluun tuloksen.

        Args:
            name: pelaajan käyttäjänimi
            score: pelaajan tulos
        """
        self.database_connection.execute(
            "INSERT INTO Scores (username, score) VALUES (?,?);", (name, score))
        self.database_connection.commit()

    def get_all(self):
        """Hakee tietokannasta kaikki tulokset lisäysjärjestyksessä.

        Returns:
            lista kaikista tuloksista
        """
        get_all = "SELECT username, score FROM Scores ORDER BY score;"
        return self.database_connection.execute(get_all).fetchall()

    def get_top_5(self):
        """Hakee tietokannasta viisi parasta tulosta.

        Returns:
            lista viidestä parhaasta tuloksesta ja käyttäjänimistä parhaimmasta huonoimpaan
        """
        get_5 = "SELECT username, score FROM Scores ORDER BY score DESC LIMIT 5;"
        return self.database_connection.execute(get_5).fetchall()
