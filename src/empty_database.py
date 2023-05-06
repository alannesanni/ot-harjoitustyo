from repositories.database_connection import get_database_connection, get_database_connection_test


def empty_db():
    """Funktio, jonka avulla tietokannan voi tyhjentää. 
    """
    connection = get_database_connection()
    connection_test = get_database_connection_test()
    connection.execute("DROP TABLE IF EXISTS EasyScores")
    connection.execute("DROP TABLE IF EXISTS MediumScores")
    connection.execute("DROP TABLE IF EXISTS HardScores")
    connection_test.execute("DROP TABLE IF EXISTS EasyScores")
    connection_test.execute("DROP TABLE IF EXISTS MediumScores")
    connection_test.execute("DROP TABLE IF EXISTS HardScores")
    print("Database is now empty.")


if __name__ == "__main__":
    empty_db()
