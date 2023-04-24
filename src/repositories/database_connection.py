import sqlite3

def get_database_connection():
    connection = sqlite3.connect("highscore.db")
    return connection


