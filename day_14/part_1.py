
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
time = 100
WIDE, TALL = 101, 103

input = input.split("\n")[1:-1]
robots = [(tuple(map(int, robot.split(" ")[0].split("=")[1].split(","))),
           tuple(map(int, robot.split(" ")[1].split("=")[1].split(",")))) for robot in input]
# print(robots)

quadrants = [0] * 4
for i, robot in enumerate(robots):
    x = (robot[0][0] + robot[1][0] * time) % WIDE
    y = (robot[0][1] + robot[1][1] * time) % TALL
    left = x < WIDE // 2
    if WIDE % 2 == 1:
        right = x > WIDE // 2
    else:
        right = x >= WIDE // 2

    top = y < TALL // 2
    if TALL % 2 == 1:
        bottom = y > TALL // 2
    else:
        bottom = y >= TALL // 2
    if left and top:
        quadrants[0] += 1
    if right and top:
        quadrants[1] += 1
    if left and bottom:
        quadrants[2] += 1
    if right and bottom:
        quadrants[3] += 1
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])