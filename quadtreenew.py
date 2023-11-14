class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary, self.capacity = boundary, capacity
        self.points, self.divided = [], False
        self.x, self.y, self.w, self.h = boundary

    def insert(self, point):
        if not (self.x <= point.x < self.x + self.w and self.y <= point.y < self.y + self.h):
            return False
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        if not self.divided:
            self.divide()
        return (
            self.northwest.insert(point) or
            self.northeast.insert(point) or
            self.southwest.insert(point) or
            self.southeast.insert(point)
        )

    def query(self, range_boundary):
        if not (
            range_boundary[0] < self.x + self.w and range_boundary[2] > self.x and
            range_boundary[1] < self.y + self.h and range_boundary[3] > self.y
        ):
            return []
        result = [point for point in self.points if self.x <= point.x < self.x + self.w and self.y <= point.y < self.y + self.h]
        if self.divided:
            result += (
                self.northwest.query(range_boundary) +
                self.northeast.query(range_boundary) +
                self.southwest.query(range_boundary) +
                self.southeast.query(range_boundary)
            )
        return result

    def divide(self):
        x_half, y_half = self.x + self.w / 2, self.y + self.h / 2
        nw_boundary, ne_boundary, sw_boundary, se_boundary = (
            (self.x, self.y, x_half, y_half),
            (x_half, self.y, self.w - x_half, y_half),
            (self.x, y_half, x_half, self.h - y_half),
            (x_half, y_half, self.w - x_half, self.h - y_half),
        )
        self.northwest, self.northeast, self.southwest, self.southeast = (
            QuadTree(nw_boundary, self.capacity),
            QuadTree(ne_boundary, self.capacity),
            QuadTree(sw_boundary, self.capacity),
            QuadTree(se_boundary, self.capacity),
        )
        self.divided = True

# Example usage:
boundary = (0, 0, 100, 100)  # Quadtree boundary (x, y, width, height)
capacity = 4  # Maximum number of points in each node

quadtree = QuadTree(boundary, capacity)

# Insert some points
points_to_insert = [Point(10, 20), Point(45, 60), Point(70, 80), Point(30, 40), Point(85, 90), Point(5, 5)]
[quadtree.insert(point) for point in points_to_insert]
    
# Query points within a range
query_range = (20, 30, 50, 70)
result = quadtree.query(query_range)

# Print the results
print("Inserted points:", [(point.x, point.y) for point in points_to_insert])
print("Points within the query range:", [(point.x, point.y) for point in result])
