import input
import re

memory = input.input
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, memory)
# print(matches)
result = 0

for match in matches:
    a,b = int(match[0]), int(match[1])
    result += a * b

print(result)