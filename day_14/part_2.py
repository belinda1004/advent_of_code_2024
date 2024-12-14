
from collections import defaultdict
import input
from time import sleep
from functools import cache

# input = """
# p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3
#  """
input = input.input
# wide, tall = 11, 7
time = 1
WIDE, TALL = 101, 103

input = input.split("\n")[1:-1]
robots = [(tuple(map(int, robot.split(" ")[0].split("=")[1].split(","))),
           tuple(map(int, robot.split(" ")[1].split("=")[1].split(",")))) for robot in input]
# print(robots)

def print_tree(grid):
    for row in grid:
        print("".join(["#" if x else "." for x in row]))
while True:
    grid = [[0 for _ in range(WIDE)] for _ in range(TALL)]
    bad_robot = False
    for i, robot in enumerate(robots):
        x = (robot[0][0] + robot[1][0] * time) % WIDE
        y = (robot[0][1] + robot[1][1] * time) % TALL
        if grid[y][x]:
            bad_robot = True
            break
        grid[y][x] = 1
    if not bad_robot:
        print(time)
        print_tree(grid)
        break
    time += 1