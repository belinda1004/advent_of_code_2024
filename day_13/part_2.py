from collections import defaultdict
import input

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
# """
input = input.input

input = input.split("\n")[1:-1]

# DP is the least efficient solution !!!
# def win_prize_dp(a, b, prize):
#     print("win_prize", a, b, prize)
#     max_x, max_y = prize
#     dp = defaultdict(lambda: float('inf'))
#     dp[(0, 0)] = 0
#
#     for x in range(max_x + 1):
#         for y in range(max_y + 1):
#             if dp[(x, y)] == float('inf'):
#                 continue
#             # print(x, y, dp[(x, y)])
#             if x + a[0] <= max_x and y + a[1] <= max_y:
#                 dp[(x + a[0], y + a[1])] = min(dp[(x + a[0], y + a[1])], dp[(x, y)] + 3)
#             if x + b[0] <= max_x and y + b[1] <= max_y:
#                 dp[(x + b[0], y + b[1])] = min(dp[(x + b[0], y + b[1])], dp[(x, y)] + 1)
#
#     result = dp[prize]
#     return result if result != float('inf') else -1


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
    prize = (int(prize[0][2:])+10000000000000, int(prize[1][2:])+10000000000000)

    # This is actually a Linear equation in two unknowns problem
    
    xa, ya = button_a
    xb, yb = button_b
    X, Y = prize
    a = (X * yb - Y * xb) / (xa * yb - ya * xb)
    b = (Y * xa - X * ya) / (xa * yb - ya * xb)
    if a == int(a) and b == int(b):
        total += int(3 * a + b)

print(total)


