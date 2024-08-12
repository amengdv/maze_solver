class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, x, y, width, height, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walls = {
                "top" : Line(Point(self.x, self.y), Point(self.x + self.width, self.y)),
                "left" : Line(Point(self.x, self.y), Point(self.x, self.y + self.height)),
                "right" : Line(Point(self.x + self.width, self.y), Point(self.x + self.width, self.y + self.height)),
                "bottom" : Line(Point(self.x, self.y + self.height), Point(self.x + self.width, self.y + self.height)),
        }

        self.win = window


    def draw(self, walls=["top", "left", "right", "bottom"]):
        for wall in walls:
            self.win.draw_line(self.walls[wall])


