
from collections import defaultdict
import input
from time import sleep
from functools import cache

# input = """
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
#
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176
#
# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450
#
# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
#  """
input = input.input

input = input.split("\n")[1:-1]


@cache
def win_prize(a, b, prize, max_a=100, max_b=100):
    # print(a,b,prize,max_a, max_b)

    if prize[0] == 0 and prize[1] == 0:
        return 0
    if prize[0] < 0 or prize[1] < 0:
        return -1
    if max_a > 0:
        press_a = win_prize(a, b, (prize[0] - a[0], prize[1] - a[1]), max_a-1, max_b)
    else:
        press_a = -1

    if max_b > 0:
        press_b = win_prize(a, b, (prize[0] - b[0], prize[1] - b[1]), max_a, max_b-1)
    else:
        press_b = -1
    # print(press_a, press_b)
    if press_a == -1 and press_b == -1:
        return -1
    if press_a == -1:
        return 1 + press_b
    if press_b == -1:
        return 3 + press_a

    return min(3+press_a, 1+press_b)


i = 0
total = 0
while i < len(input):
    button_a = input[i]
    button_b = input[i+1]
    prize = input[i+2]
    i += 4

    button_a = button_a.split(":")[1].strip().split(", ")
    button_b = button_b.split(":")[1].strip().split(", ")
    prize = prize.split(":")[1].strip().split(", ")

    button_a = (int(button_a[0][2:]), int(button_a[1][2:]))
    button_b = (int(button_b[0][2:]), int(button_b[1][2:]))
    prize = (int(prize[0][2:]), int(prize[1][2:]))

    tokens = win_prize(button_a, button_b, prize)
    total += tokens if tokens != -1 else 0

print(total)


