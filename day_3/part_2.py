import input
import re

memory = input.input
# memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
number_pattern = r"mul\((-?\d+),(-?\d+)\)"
number_matches = re.finditer(number_pattern, memory)

do_pattern = r"do"
do_matches = []

for match in re.finditer(do_pattern, memory):
    do_matches.append((False if memory[match.start():match.start()+5] == "don't" else True, match.start()))

print(do_matches)

result = 0

do = True
i = 0

for match in number_matches:
    # print(match.group(1), match.group(2))
    if match.start() > do_matches[i][1]:
        do = do_matches[i][0]
        if i < len(do_matches) - 1:
            i += 1
    a, b = int(match.group(1)), int(match.group(2))
    result += a * b * (1 if do else 0)



print(result)