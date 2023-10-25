class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadTreeNode:
    def __init__(self, boundary, capacity):
        self.boundary = boundary  # Rectangle boundary of this node
        self.capacity = capacity  # Maximum number of points in a node
        self.points = []  # List of points in this node
        self.is_divided = False  # Indicates if this node has been divided into four children

    def insert(self, point):
        if not self.boundary.contains_point(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.is_divided:
                self.subdivide()
                self.is_divided = True
            return self.insert_into_children(point)

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.width / 2
        h = self.boundary.height / 2

        nw = Rectangle(x, y, w, h)
        ne = Rectangle(x + w, y, w, h)
        sw = Rectangle(x, y + h, w, h)
        se = Rectangle(x + w, y + h, w, h)

        self.children = [
            QuadTreeNode(nw, self.capacity),
            QuadTreeNode(ne, self.capacity),
            QuadTreeNode(sw, self.capacity),
            QuadTreeNode(se, self.capacity)
        ]

    def insert_into_children(self, point):
        for child in self.children:
            if child.insert(point):
                return True
        return False

    def query(self, query_boundary):
        result = []
        if not self.boundary.intersects(query_boundary):
            return result

        for point in self.points:
            if query_boundary.contains_point(point):
                result.append(point)

        if self.is_divided:
            for child in self.children:
                result.extend(child.query(query_boundary))

        return result

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains_point(self, point):
        return (
            self.x <= point.x <= self.x + self.width and
            self.y <= point.y <= self.y + self.height
        )

    def intersects(self, other):
        return not (
            self.x + self.width < other.x or
            other.x + other.width < self.x or
            self.y + self.height < other.y or
            other.y + other.height < self.y
        )

# Example usage:
boundary = Rectangle(0, 0, 400, 400)
quadtree = QuadTreeNode(boundary, 4)

points = [Point(50, 50), Point(100, 100), Point(200, 200), Point(250, 250)]

for point in points:
    quadtree.insert(point)

query_boundary = Rectangle(75, 75, 150, 150)
query_result = quadtree.query(query_boundary)

for point in query_result:
    print(f"Point ({point.x}, {point.y}) is within the query boundary.")
