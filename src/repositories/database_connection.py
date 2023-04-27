import sqlite3


def get_database_connection():
    connection = sqlite3.connect("highscore.db")
    print(connection)
    return connection

def get_database_connection_test():
    connection = sqlite3.connect("highscore_test.db")
    print(connection)
    return connection
