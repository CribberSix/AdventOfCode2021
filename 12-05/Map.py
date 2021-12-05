from LineSegment import LineSegment


class Map:

    def __init__(self, length_of_map):
        """Create a square 2D list(s) as a map to keep track of lines."""
        self.map = [[0 for _ in range(length_of_map+1)] for _ in range(length_of_map+1)]

    def mark_line(self, line: LineSegment) -> None:
        """
        Increment all positions of a line on the map by 1.

        :param line: LineSegment along which the positions have to be incremented.
        :return: None
        """

        if line.is_horizontal_or_vertical():
            # rearrange numbers if necessary to be able to create a range
            lower_x, higher_x = (line.x1, line.x2) if line.x1 < line.x2 else (line.x2, line.x1)
            lower_y, higher_y = (line.y1, line.y2) if line.y1 < line.y2 else (line.y2, line.y1)
            for x in range(lower_x, higher_x + 1):
                for y in range(lower_y, higher_y + 1):
                    self.map[x][y] += 1
        else:
            # switch lines so we go from four to two cases which we need to encode.
            if line.x1 > line.x2:
                line.x1, line.x2 = line.x2, line.x1
                line.y1, line.y2 = line.y2, line.y1
            # Going right downwards: (x+1, y+1)
            if line.x1 < line.x2 and line.y1 < line.y2:
                for i, _ in enumerate(range(line.x1, line.x2+1)):
                    self.map[line.x1 + i][line.y1 + i] += 1
            # Going right upwards: (x+1, y-1)
            elif line.x1 < line.x2 and line.y1 > line.y2:
                for i, _ in enumerate(range(line.x1, line.x2+1)):
                    self.map[line.x1 + i][line.y1 + (i*-1)] += 1

    def count_at_least_two_overlaps(self) -> int:
        """Calculate the number of positions with at least two lines going through them."""
        count = 0
        for row in self.map:
            for element in row:
                if element >= 2:
                    count += 1
        return count
