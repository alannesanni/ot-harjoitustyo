import unittest
from entities.pong import Pong
from entities.paddle import Paddle
from entities.ball import Ball
from entities.score import Score
from entities.collisions import Collisions


class TestPong(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle((200, 200, 200), 5, 480, 120, 20)
        self.ball = Ball((200, 200, 200), 100, 100, 10)
        self.score = Score()
        self.collisions = Collisions()

    # Paddle tests:
    def test_paddle_still(self):
        self.paddle.mode = "still"
        self.paddle.move()
        self.assertEqual(self.paddle.x_coord, 5)

    def test_paddle_moves_right(self):
        self.paddle.mode = "right"
        self.paddle.move()
        self.assertEqual(self.paddle.x_coord, 15)

    def test_paddle_moves_left(self):
        self.paddle.x_coord = 200
        self.paddle.mode = "left"
        self.paddle.move()
        self.assertEqual(self.paddle.x_coord, 190)

    def test_paddle_hits_wall_right(self):
        self.paddle.x_coord = 575
        self.paddle.mode = "right"
        self.paddle.move()
        self.assertEqual(self.paddle.x_coord, 580)

    def test_paddle_hits_wall_left(self):
        self.paddle.mode = "left"
        self.paddle.move()
        self.assertEqual(self.paddle.x_coord, 0)

    def test_paddle_get_coordinate(self):
        x = self.paddle.get_coordinate("x")
        y = self.paddle.get_coordinate("y")
        z = self.paddle.get_coordinate("z")

        self.assertEqual(x, 5)
        self.assertEqual(y, 480)
        self.assertEqual(z, "wrong letter")

    # Ball tests:
    def test_move(self):
        self.ball.move()
        self.assertEqual(self.ball.x_coord, 113)
        self.assertEqual(self.ball.y_coord, 105)

    def test_ball_paddle_collision(self):
        self.ball.paddle_collision()
        self.assertEqual(self.ball.direction_y, -5)

    def test_ball_paddle_side_collision(self):
        self.ball.paddle_side_collision()
        self.assertEqual(self.ball.direction_x, -13)

    def test_ball_side_wall_collision(self):
        self.ball.side_wall_collision()
        self.assertEqual(self.ball.direction_x, -13)

    def test_ball_top_wall_collision(self):
        self.ball.top_wall_collision()
        self.assertEqual(self.ball.direction_y, -5)

    def test_ball_get_coordinate(self):
        x = self.ball.get_coordinate("x")
        y = self.ball.get_coordinate("y")
        z = self.ball.get_coordinate("z")

        self.assertEqual(x, 100)
        self.assertEqual(y, 100)
        self.assertEqual(z, "wrong letter")

    # Collisions tests:
    def test_collisions_ball_and_paddle_true(self):
        self.ball.x_coord = 250
        self.ball.y_coord = 475
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle(self.ball, self.paddle)
        self.assertEqual(boolean, True)

    def test_collisions_ball_and_paddle_fasle_1(self):
        self.ball.x_coord = 400
        self.ball.y_coord = 100
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle(self.ball, self.paddle)
        self.assertEqual(boolean, False)

    def test_collisions_ball_and_paddle_fasle_2(self):
        self.ball.x_coord = 250
        self.ball.y_coord = 100
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle(self.ball, self.paddle)
        self.assertEqual(boolean, False)

    def test_collisions_ball_and_paddle_left_side_true(self):
        self.ball.x_coord = 200
        self.ball.y_coord = 475
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle_side(self.ball, self.paddle)
        self.assertEqual(boolean, True)

    def test_collisions_ball_and_paddle_right_side_true(self):
        self.ball.x_coord = 330
        self.ball.y_coord = 475
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle_side(self.ball, self.paddle)
        self.assertEqual(boolean, True)

    def test_collisions_ball_and_paddle_right_side_fasle_1(self):
        self.ball.x_coord = 330
        self.ball.y_coord = 100
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle_side(self.ball, self.paddle)
        self.assertEqual(boolean, False)

    def test_collisions_ball_and_paddle_right_side_fasle_2(self):
        self.ball.x_coord = 450
        self.ball.y_coord = 100
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle_side(self.ball, self.paddle)
        self.assertEqual(boolean, False)

    def test_collisions_ball_and_paddle_left_side_fasle_1(self):
        self.ball.x_coord = 200
        self.ball.y_coord = 100
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle_side(self.ball, self.paddle)
        self.assertEqual(boolean, False)

    def test_collisions_ball_and_paddle_left_side_fasle_2(self):
        self.ball.x_coord = 400
        self.ball.y_coord = 100
        self.paddle.x_coord = 200
        self.paddle.y_coord = 480
        boolean = self.collisions.ball_and_paddle_side(self.ball, self.paddle)
        self.assertEqual(boolean, False)

    def test_collisions_ball_and__left_side_true(self):
        self.ball.x_coord = 10
        self.ball.y_coord = 300
        boolean = self.collisions.ball_and_side(self.ball)
        self.assertEqual(boolean, True)

    def test_collisions_ball_and_right_side_true(self):
        self.ball.x_coord = 700
        self.ball.y_coord = 300
        boolean = self.collisions.ball_and_side(self.ball)
        self.assertEqual(boolean, True)

    def test_collisions_ball_and_side_fasle(self):
        self.ball.x_coord = 250
        self.ball.y_coord = 300
        boolean = self.collisions.ball_and_side(self.ball)
        self.assertEqual(boolean, False)

    def test_collisions_ball_and_top_true(self):
        self.ball.x_coord = 700
        self.ball.y_coord = 10
        boolean = self.collisions.ball_and_top(self.ball)
        self.assertEqual(boolean, True)

    def test_collisions_ball_and_top_fasle(self):
        self.ball.x_coord = 250
        self.ball.y_coord = 300
        boolean = self.collisions.ball_and_top(self.ball)
        self.assertEqual(boolean, False)

    # Score tests:
    def test_score_add_point(self):
        self.score.add_point()
        self.assertEqual(self.score.points, 1)
