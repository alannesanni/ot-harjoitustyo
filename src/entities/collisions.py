class Collisions:
    def ball_and_paddle(self, ball, paddle):
        if ball.x_coord + 10 > paddle.x_coord and ball.x_coord < paddle.x_coord + paddle.width:
            if ball.y_coord + 10 >= paddle.y_coord:
                return True
        return False

    def ball_and_paddle_side(self, ball, paddle):
        # right
        if paddle.x_coord+paddle.width-15 <= ball.x_coord-10 <= paddle.x_coord + paddle.width+15:
            if ball.y_coord + 10 >= paddle.y_coord:
                return True
        # left
        if paddle.x_coord-15 <= ball.x_coord+10 <= paddle.x_coord+15:
            if ball.y_coord + 10 >= paddle.y_coord:
                return True

        return False

    def ball_and_side(self, ball):
        # right
        if ball.x_coord + 10 >= 700:
            return True
        # left
        if ball.x_coord - 10 <= 0:
            return True
        return False

    def ball_and_top(self, ball):
        if ball.y_coord - 10 <= 0:
            return True
        return False
