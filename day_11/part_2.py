from functools import cache

'''
！！！！ORDER IS NOTHING!!!
'''

input = '1950139 0 3 837 6116 18472 228700 45'
# input = '125 17'
blinks = 75

input = [int(_) for _ in input.split()]

@cache
def blink_stone(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return blink_stone(1, blinks - 1)
    if len(str(stone)) % 2 == 0:
        left, right = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
        return blink_stone(left, blinks - 1) + blink_stone(right, blinks - 1)
    return blink_stone(stone * 2024, blinks - 1)

print(sum([blink_stone(_, blinks) for _ in input]))