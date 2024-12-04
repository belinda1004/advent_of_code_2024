import input

lists = input.input
lists = lists.split("\n")[1:-1]
left, right = [int(a.split("   ")[0]) for a in lists], [int(a.split("   ")[1]) for a in lists]
left.sort()
right.sort()
result = 0
for i in range(len(left)):
    result += abs(left[i] - right[i])
print(result)
