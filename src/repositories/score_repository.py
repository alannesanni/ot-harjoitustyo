import sqlite3
from repositories.database_connection import get_database_connection


class ScoreDatabase:
    def __init__(self):
        self.database = get_database_connection()

    def create_database(self):
        try:
            self.create_table()
        except sqlite3.OperationalError:
            pass

    def create_table(self):
        self.database.execute(
            "CREATE TABLE Scores (id INTEGER PRIMARY KEY, username TEXT, score INTEGER);")

    def add_score(self, name, score):
        self.database.execute(
            "INSERT INTO Scores (username, score) VALUES (?,?);", (name, score))

    def get_top_5(self):
        get_5 = "SELECT username, score FROM Scores ORDER BY score DESC LIMIT 5;"
        return self.database.execute(get_5).fetchall()
