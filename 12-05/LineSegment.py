
class LineSegment:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def __str__(self):
        return f"Segment: ({self.x1}, {self.y1}) - ({self.x2}, {self.y2})"

    def is_horizontal_or_vertical(self):
        """Calculates whether a line is strictly horizontal or vertical."""
        return self.x1 == self.x2 or self.y1 == self.y2

    def get_max_number(self):
        return max([self.x1, self.x2, self.y1, self.y2])
