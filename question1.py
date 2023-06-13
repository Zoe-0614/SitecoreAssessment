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



# Create individual figures
point1 = Point(2, 3)
point2 = Point(5, 7)
line = Line(point1, point2)
circle = Circle(point1, 4)
print(point1.x, point1.y)
print(point2.x, point2.y)
print(line.start_point.x, line.start_point.y, line.end_point.x, line.end_point.y)
print(circle.center.x, circle.center.y, circle.radius)

# Move and rotate individual figures
point1.move(1, 2)
print(point1.x, point1.y)
print(point2.x, point2.y)
line.rotate(45)
circle.move(-3, -1)
print(point1.x, point1.y)
print(point2.x, point2.y)
print(line.start_point.x, line.start_point.y, line.end_point.x, line.end_point.y)
print(circle.center.x, circle.center.y, circle.radius)

# Create an aggregation and add figures to it
aggregation = Aggregation()
aggregation.add_figure(point1)
aggregation.add_figure(point2)
aggregation.add_figure(circle)
print(aggregation.figures[0].x, aggregation.figures[0].y)
print(aggregation.figures[1].x, aggregation.figures[1].y)
print(aggregation.figures[2].center.x, aggregation.figures[2].center.y, aggregation.figures[2].radius)

# Move and rotate the aggregation (affects all figures)
aggregation.move(3, 4)
aggregation.rotate(90)
print(aggregation.figures[0].x, aggregation.figures[0].y)
print(aggregation.figures[1].x, aggregation.figures[1].y)
print(aggregation.figures[2].center.x, aggregation.figures[2].center.y, aggregation.figures[2].radius)
