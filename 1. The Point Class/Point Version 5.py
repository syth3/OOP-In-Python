class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)


# Constructing a Point
point = Point(3, 5)
print(point.x, point.y)

point2 = Point()
print(point2.x, point2.y)
