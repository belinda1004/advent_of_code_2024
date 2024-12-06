import time

import input
import input_sample

input = input.input
# input = input_sample.input

map = [list(_) for _ in input.split("\n")[1:-1]]

row = len(map)
col = len(map[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

start_x, start_y = -1, -1
for i in range(row):
    for j in range(col):
        if (map[i][j] == "^"):
            start_x, start_y = i, j
            break
    if start_x != -1:
        break
start_dir = 0

result = 0
for i in range(row):
    for j in range(col):

        if (map[i][j] == "^" or map[i][j] == "#"):
            continue
        # print("obstacle:", i, j)
        map[i][j] = "#"

        x, y, direction, find = start_x, start_y, start_dir, False
        pass_directions = [[[] for _ in range(col)] for _ in range(row)]
        pass_directions[x][y] = [direction]

        while True:
            # print(x, y, direction, map[x][y], pass_directions[x][y])
            if map[x][y] == "#":
                x = x - directions[direction][0]
                y = y - directions[direction][1]
                direction = (direction + 1) % 4
            else:
                x = x + directions[direction][0]
                y = y + directions[direction][1]

            if x < 0 or y < 0 or x >= row or y >= col:
                break

            if direction in pass_directions[x][y]:
                find = True
                # print("bingo!", i , j)
                break
            else:
                pass_directions[x][y].append(direction)
            # print(x,y, pass_directions[x][y])
            # time.sleep(1)


        result += 1 if find else 0
        map[i][j] = "."


print(result)


