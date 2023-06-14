import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, angle):
        radians = math.radians(angle)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x = self.x * cos_theta - self.y * sin_theta
        y = self.x * sin_theta + self.y * cos_theta
        self.x = x
        self.y = y

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def move(self, dx, dy):
        self.start_point.move(dx, dy)
        self.end_point.move(dx, dy)

    def rotate(self, angle):
        self.start_point.rotate(angle)
        self.end_point.rotate(angle)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def move(self, dx, dy):
        self.center.move(dx, dy)

    def rotate(self, angle):
        self.center.rotate(angle)

class Aggregation:
    def __init__(self):
        self.figures = []

    def add_figure(self, figure):
        self.figures.append(figure)

    def move(self, dx, dy):
        for figure in self.figures:
            figure.move(dx, dy)

    def rotate(self, angle):
        for figure in self.figures:
            figure.rotate(angle)

