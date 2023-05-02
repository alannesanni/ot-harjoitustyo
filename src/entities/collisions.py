class Collisions:
    """Luokka, joka tarkistaa töymäykset

    Attributes:
        ball: Pallo
        paddle: Lauta
    """

    def ball_and_paddle(self, ball, paddle):
        """Tarkistaa törmääkö pallo laudan päälle.

        Args:
            ball: Pallo
            paddle: Lauta

        Returns:
            True, jos pallo ja lauta törmäävät, muuten False
        """
        if ball.x_coord + 10 > paddle.x_coord and ball.x_coord < paddle.x_coord + paddle.width:
            if ball.y_coord + 10 >= paddle.y_coord:
                return True
        return False

    def ball_and_paddle_side(self, ball, paddle):
        """Tarkistaa törmääkö pallo laudan jompaan kumpaan sivuun.

        Args:
            ball: Pallo
            paddle: Lauta

        Returns:
            True, jos pallo törmää laudan sivuun, muuten False
        """
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
        """Tarkistaa törmääkö pallo ruudun sivuseiniin.

        Args:
            ball: Pallo

        Returns:
            True, jos pallo törmää jompaan kumpaan sivuseinään, muuten False
        """
        # left
        if ball.x_coord - 10 <= 0:
            return True
         # right
        if ball.x_coord + 10 >= 700:
            return True
        return False

    def ball_and_top(self, ball):
        """Tarkistaa törmääkö pallo ruudun yläseinään.

        Args:
            ball: Pallo

        Returns:
            True, jos pallo törmää yläseinään, muuten False
        """
        if ball.y_coord - 10 <= 0:
            return True
        return False
