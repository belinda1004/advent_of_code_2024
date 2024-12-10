
import input

input = input.input
# input = """
# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """


def safe_int_conversion(s):
    try:
        return int(s)
    except ValueError:
        return 100

map = [[safe_int_conversion(_) for _ in line] for line in input.split("\n")[1:-1]]
rows = len(map)
cols = len(map[0])
neighbours = [[[] for _ in range(cols)] for _ in range(rows)]
ratings =  [[-1 for _ in range(cols)] for _ in range(rows)]

directions = [(0,1), (1,0), (0,-1), (-1,0)]
trailheads = []


for i in range(rows):
    for j in range(cols):
        if map[i][j] == 0:
            trailheads.append((i,j))
        if map[i][j] == 9:
            ratings[i][j] = 1
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            if 0 <= x < rows and 0 <= y < cols and map[x][y] == map[i][j] + 1:
                neighbours[i][j].append((x,y))

def get_rating(node):
    x, y = node
    if ratings[x][y] != -1:
        return ratings[x][y]
    rating = 0
    for neighbour in neighbours[x][y]:
        rating += get_rating(neighbour)
    return rating

for i in range(rows):
    for j in range(cols):
        ratings[i][j] = get_rating((i,j))

sum = 0
for trailhead in trailheads:
    sum += ratings[trailhead[0]][trailhead[1]]
print(sum)

