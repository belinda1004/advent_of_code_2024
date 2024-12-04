from collections import Counter
import input

lists = input.input
lists = lists.split("\n")[1:-1]
left, right = [int(a.split("   ")[0]) for a in lists], [int(a.split("   ")[1]) for a in lists]

counts = Counter(right)

result = 0
for i in range(len(left)):
    result += left[i] * counts.get(left[i], 0)
print(result)
