class Ball:
    def __init__(self, color, x_coord, y_coord, radius):
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.radius = radius
        self.direction_x = 13
        self.direction_y = 5

    def get_coordinate(self, letter):
        if letter == "x":
            return self.x_coord
        if letter == "y":
            return self.y_coord
        return "wrong letter"

    def move(self):
        self.x_coord += self.direction_x
        self.y_coord += self.direction_y

    def paddle_collision(self):
        self.direction_y = -self.direction_y

    def paddle_side_collision(self):
        self.direction_x = -self.direction_x

    def side_wall_collision(self):
        self.direction_x = -self.direction_x

    def top_wall_collision(self):
        self.direction_y = -self.direction_y
