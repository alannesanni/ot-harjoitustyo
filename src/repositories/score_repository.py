import sqlite3


class ScoreDatabase:
    def __init__(self, connection):
        self.database_connection = connection

    def create_database(self):
        try:
            self.create_table()
        except sqlite3.OperationalError:
            pass

    def create_table(self):
        self.database_connection.execute(
            "CREATE TABLE Scores (id INTEGER PRIMARY KEY, username TEXT, score INTEGER);")

    def add_score(self, name, score):
        self.database_connection.execute(
            "INSERT INTO Scores (username, score) VALUES (?,?);", (name, score))
        self.database_connection.commit()

    def get_all(self):
        get_all = "SELECT username, score FROM Scores ORDER BY score DESC LIMIT 5;"
        return self.database_connection.execute(get_all).fetchall()

    def get_top_5(self):
        get_5 = "SELECT username, score FROM Scores ORDER BY score DESC LIMIT 5;"
        return self.database_connection.execute(get_5).fetchall()
