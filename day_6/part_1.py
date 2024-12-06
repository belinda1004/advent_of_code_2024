
import input
import input_sample

input = input.input
# input = input_sample.input

map = [list(_) for _ in input.split("\n")[1:-1]]

row = len(map)
col = len(map[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0

x, y = -1, -1
for i in range(row):
    for j in range(col):
        if (map[i][j] == "^"):
            x, y = i, j
            break
    if x != -1:
        break

while x >= 0 and y >= 0 and x < row and y < col:
    
    if map[x][y] == "#":
        x = x - directions[direction][0]
        y = y - directions[direction][1]
        direction = (direction + 1) % 4
    else:
        map[x][y] = "X"
        x = x + directions[direction][0]
        y = y + directions[direction][1]

result = 0
for i in range(row):
    for j in range(col):
        if map[i][j] == "X":
            result += 1

print(result)


