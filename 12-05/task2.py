from LineSegment import LineSegment
from Map import Map

# Parse data
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.readlines()  # lines as list-items
data = [x[:-1].split(" -> ") for x in data]

# create segments
segments = []
for row in data:
    x1 = row[0].split(",")[0]
    y1 = row[0].split(",")[1]
    x2 = row[1].split(",")[0]
    y2 = row[1].split(",")[1]
    segments.append(LineSegment(x1, y1, x2, y2))

# create the map
max_index = max([s.get_max_number() for s in segments])
ocean_floor = Map(length_of_map=max_index)

# Map the ocean floor based on the segments
for segment in segments:
    ocean_floor.mark_line(segment)

overlaps = ocean_floor.count_at_least_two_overlaps()
print(overlaps)
