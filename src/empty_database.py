from repositories.database_connection import get_database_connection


def empty_db():
    connection = get_database_connection()
    connection.execute("DROP TABLE IF EXISTS Scores")
    print("Database is now empty.")


if __name__ == "__main__":
    empty_db()
