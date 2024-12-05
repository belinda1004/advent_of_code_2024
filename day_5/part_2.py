
from collections import defaultdict
from functools import cmp_to_key

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

def comparator(a, b):
    if b in d[a]:
        return 1
    elif a in d[b]:
        return -1
    else:
        return 0

def check_order(update):
    correct = True
    for i in range(len(update)- 1):
        for j in range(i+1, len(update)):
            if update[j] in d[update[i]]:
                correct = False
                break
        if not correct:
            break
    return correct

result = 0
for update in updates:
    update = update.split(",")
    if not check_order(update):
        sorted_update = sorted(update, key=cmp_to_key(comparator))
        result += int(sorted_update[len(update)//2])

print(result)
