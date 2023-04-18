class Paddle:
    def __init__(self, color, x_coord, y_coord, width, height):
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.mode = "still"

    def get_coordinate(self, letter):
        if letter == "y":
            return self.y_coord
        if letter == "x":
            return self.x_coord
        return "wrong letter"

    def move(self):
        if self.mode == "left":
            self.x_coord -= 10

        elif self.mode == "right":
            self.x_coord += 10

        else:
            self.x_coord = self.x_coord

        if self.x_coord <= 0:
            self.x_coord = 0

        elif self.x_coord >= 580:
            self.x_coord = 580
