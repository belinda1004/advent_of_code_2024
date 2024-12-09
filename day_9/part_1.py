
import input


input = input.input
# input = "2333133121414131402"
# input = "12345"

index, pos, = 0, 0
blocks, spaces, sorted = [], [], []
odd = True

for number in input:
    number = int(number)
    if odd:
        sorted += [index] * number
        blocks += [_ for _ in range(pos, pos + number)]
        index += 1
    else:
        sorted += [-1] * number
        spaces +=  [_ for _ in range(pos, pos + number)]
    pos += number
    odd = not odd

space_index = 0
block_index = len(blocks) - 1
space_left_pointer = spaces[space_index]
block_right_pointer = blocks[block_index]

while block_right_pointer > space_left_pointer:
    sorted[space_left_pointer] = sorted[block_right_pointer]
    space_index += 1
    block_index -= 1
    space_left_pointer = spaces[space_index]
    block_right_pointer = blocks[block_index]

checksum = 0
for i in range(max(spaces[space_index - 1], block_right_pointer) + 1):
    checksum += sorted[i] * i

print(checksum)


