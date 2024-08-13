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

        self.has_walls = {
            "top": True,
            "left": True,
            "right": True,
            "bottom": True,
        }

        self.win = window
        self.visited = False


    def draw(self):
        for wall in self.has_walls:
            if self.has_walls[wall]:
               self.win.draw_line(self.walls[wall])


    def draw_move(self, to_cell, undo=False):
        from_center = (self.x + self.width // 2, self.y + self.height // 2)
        to_center = (to_cell.x + to_cell.width // 2, to_cell.y + to_cell.height // 2)
        line = Line(Point(from_center[0], from_center[1]), Point(to_center[0], to_center[1]))
        color = "red"
        if undo:
            color = "gray"
        self.win.draw_line(line, color)


