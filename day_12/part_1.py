
from collections import defaultdict
import input

# input = """
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
#  """
input = input.input
map = defaultdict(lambda:'!')
for i, line in enumerate(input.split("\n")[1:-1]):
    for j, c in enumerate(line):
        map[(i,j)] = c

not_visited = set(map.keys())

result = 0
# ans2 = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while not_visited:
    start = not_visited.pop()
    ch = map[start]
    stack = [start]
    area, perimeter = 0, 0
    while stack:
        node = stack.pop()
        area += 1
        perimeter += 4

        for d in directions:
            node_ = (node[0] + d[0], node[1] + d[1])
            if map[node_] != ch:
                continue
            perimeter -= 1
            if node_ not in not_visited:
                continue
            not_visited.remove(node_)
            stack.append(node_)

    result += area*perimeter


print(result)