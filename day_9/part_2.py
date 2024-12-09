
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
        blocks += [(pos, index, number)]
        index += 1
    else:
        sorted += [0] * number
        spaces += [[pos, number]]
    pos += number
    odd = not odd

for block in blocks[::-1]:
    for i in range(len(spaces)):
        space = spaces[i]
        if block[0] < space[0]:
            break
        if block[2] <= space[1]:
            sorted[space[0]:(space[0] + block[2])] = [block[1]] * block[2]
            spaces[i] = (space[0] + block[2], space[1] - block[2])
            sorted[block[0]:(block[0] + block[2])] = [0] * block[2]
            break

checksum = 0
for i, number in enumerate(sorted):
    checksum += number * i

print(checksum)

#
