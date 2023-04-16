class Collisions:
    def ball_and_paddle(self, ball, paddle):
        if ball.x + 10 > paddle.x and ball.x - 10 < paddle.x + paddle.width:
            if ball.y + 10 >= paddle.y:
                return True
        return False
    
    def ball_and_side(self, ball):
        #left
        if ball.x - 10 <=0:
            return True
        #right
        if ball.x + 10 >= 700:
            return True
        return False
    
    def ball_and_top(self, ball):
        #top
        if ball.y - 10 <= 0:
            return True
        return False