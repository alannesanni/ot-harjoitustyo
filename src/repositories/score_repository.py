from repositories.database_connection import get_database_connection

class ScoreDatabase:
    def __init__(self):
        self.db = get_database_connection()

    def create_database(self):
        try:
            self.create_table()
        except:
            pass

    def create_table(self):
        self.db.execute("CREATE TABLE Scores (id INTEGER PRIMARY KEY, username TEXT, score INTEGER);")

    def add_score(self, name, score):
        self.db.execute("INSERT INTO Scores (username, score) VALUES (?,?);", (name, score))

    def get_top_5(self):
        return self.db.execute("SELECT username, score FROM Scores ORDER BY score DESC LIMIT 5;").fetchall()
