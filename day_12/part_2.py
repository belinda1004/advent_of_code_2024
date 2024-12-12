
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

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while not_visited:
    start = not_visited.pop()
    ch = map[start]
    stack = [start]
    area = 0
    sides = set()
    while stack:
        node = stack.pop()
        area += 1

        for d in directions:
            node_ = (node[0] + d[0], node[1] + d[1])
            if map[node_] != ch:
                sides.add((node, d))
                continue
            if node_ not in not_visited:
                continue
            not_visited.remove(node_)
            stack.append(node_)

    side_adj = 0
    for (node, d) in sides:
        if d == (0, 1):
            d1 = (-1, 0)
        elif d == (0, -1):
            d1 = (1, 0)
        elif d == (-1, 0):
            d1 = (0, -1)
        else:
            d1 = (0, 1)
        if ((node[0] + d1[0], node[1] + d1[1]), d) in sides:
            side_adj -= 1

    result += area*(len(sides) + side_adj)


print(result)