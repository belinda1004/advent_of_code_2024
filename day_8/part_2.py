from collections import defaultdict
import input
import input_sample

input = input.input
# input = input_sample.input

lines = input.split("\n")[1:-1]

rows = len(lines)
cols = len(lines[0])

points = defaultdict(list)
for i in range(rows):
    for j in range(cols):
        if lines[i][j] != ".":
            points[lines[i][j]].append((i,j))

def find_antinodes(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    x_diff = abs(x1 - x2)
    y_diff = abs(y1 - y2)

    antinodes = {(x1, y1), (x2, y2)}
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if y1 <= y2:
        while x1 - x_diff >= 0 and y1 - y_diff >= 0:
            antinodes.add((x1 - x_diff, y1 - y_diff))
            x1 -= x_diff
            y1 -= y_diff
        while x2 + x_diff < rows and y2 + y_diff < cols:
            antinodes.add((x2 + x_diff, y2 + y_diff))
            x2 += x_diff
            y2 += y_diff
    else:
        while x1 - x_diff >= 0 and y1 + y_diff < cols:
            antinodes.add((x1 - x_diff, y1 + y_diff))
            x1 -= x_diff
            y1 += y_diff
        while x2 + x_diff < rows and y2 - y_diff >= 0:
            antinodes.add((x2 + x_diff, y2 - y_diff))
            x2 += x_diff
            y2 -= y_diff

    return antinodes


result = set()
for point_list in points.values():
    for i in range(len(point_list) - 1):
        for j in range(i + 1, len(point_list)):
            result |= find_antinodes(point_list[i], point_list[j])

print(len(result))
