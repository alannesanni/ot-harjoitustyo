import sqlite3


def get_database_connection():
    """Funktio, joka luo yhteyden tietokantaan, johon tulokset tallennetaan.

    Returns:
        muodostettu yhteys
    """
    connection = sqlite3.connect("highscore.db")
    print(connection)
    return connection


def get_database_connection_test():
    """Funktio, joka luo yhteyden tietokantaan, jonka avulla koodia testataan.

    Returns:
        muodostettu yhteys
    """
    connection = sqlite3.connect("highscore_test.db")
    print(connection)
    return connection
