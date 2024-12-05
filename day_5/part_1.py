
from collections import defaultdict

import input
import input_sample

input = input.input
# input = input_sample.input

lines = input.split("\n")[1:-1]
separator = lines.index("")

rules = lines[:separator]
updates = lines[separator+1:]

d = defaultdict(list)
for rule in rules:
    rule = rule.split("|")
    d[rule[1]].append(rule[0])

result = 0
for update in updates:
    update = update.split(",")
    correct = True
    for i in range(len(update)- 1):
        for j in range(i+1, len(update)):
            if update[j] in d[update[i]]:
                correct = False
                break
        if not correct:
            break
    if correct:
        result += int(update[len(update)//2])

print(result)
