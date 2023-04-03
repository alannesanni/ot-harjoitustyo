import unittest
from entities.pong import Pong
from entities.paddle import Paddle

class TestPong(unittest.TestCase):
    def setUp(self):
        self.paddle=Paddle((200,200,200),5, 480, 120 ,20)

    def test_paddle_still(self):
        self.paddle.mode="still"
        self.paddle.move()
        self.assertEqual(self.paddle.x, 5)


    def test_paddle_moves_right(self):
        self.paddle.mode="right"
        self.paddle.move()
        self.assertEqual(self.paddle.x, 15)

    def test_paddle_moves_left(self):
        self.paddle.x=200
        self.paddle.mode="left"
        self.paddle.move()
        self.assertEqual(self.paddle.x, 190)

    def test_paddle_hits_wall_right(self):
        self.paddle.x=575
        self.paddle.mode="right"
        self.paddle.move()
        self.assertEqual(self.paddle.x, 580)        

    def test_paddle_hits_wall_left(self):
        self.paddle.mode="left"
        self.paddle.move()
        self.assertEqual(self.paddle.x, 0)

    def test_get_cordinate(self):
        x=self.paddle.get_coordinate("x")
        y=self.paddle.get_coordinate("y")
        z=self.paddle.get_coordinate("z")

        self.assertEqual(x, 5)
        self.assertEqual(y, 480)
        self.assertEqual(z, "wrong letter")