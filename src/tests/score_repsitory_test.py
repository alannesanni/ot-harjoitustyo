import unittest
from empty_database import empty_db
from entities.settings import Settings
from repositories.score_repository import ScoreDatabase
from repositories.database_connection import get_database_connection_test

class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        connection_test = get_database_connection_test()
        connection_test.execute("DROP TABLE IF EXISTS Scores")

        self.settings=Settings()
        self.settings.mover="mouse"
        self.settings.ball_color=(100,100,100)
        self.settings.paddle_color=(10,10,10)
        self.settings.username="test"

    def test_empty_database(self):
        self.assertEqual(empty_db(), None)

    def test_add_score(self):
        connection=get_database_connection_test()
        ScoreDatabase(connection).create_database()
        ScoreDatabase(connection).add_score(self.settings.username, 1)
        all_list=ScoreDatabase(connection).get_all()
        self.assertEqual(all_list, [("test", 1)])

    def test_get_top_5(self):
        connection=get_database_connection_test()
        ScoreDatabase(connection).create_database()
        ScoreDatabase(connection).add_score(self.settings.username, 1)
        ScoreDatabase(connection).add_score("test2", 2)
        ScoreDatabase(connection).add_score("test3", 3)
        ScoreDatabase(connection).add_score("test4", 4)
        ScoreDatabase(connection).add_score("test5", 5)
        ScoreDatabase(connection).add_score("test0", 0)
        top_list=ScoreDatabase(connection).get_top_5()
        self.assertEqual(top_list, [("test5", 5), ("test4", 4), ("test3", 3), ("test2", 2), ("test", 1)])

    def test_create_table_error(self):
        connection=get_database_connection_test()
        ScoreDatabase(connection).create_database()
        x=ScoreDatabase(connection).create_database()
        self.assertEqual(x, None)

