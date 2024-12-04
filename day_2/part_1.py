import input
import input_sample

reports = input.input.split("\n")[1:-1]

result = 0

for report in reports:
    levels = [int(_) for _ in report.split()]
    if levels[1] < levels[0]:
        diff = -1
    elif levels[1] > levels[0]:
        diff = 1
    else:
        continue
    safe = True
    for i in range(1, len(levels)):
        if (levels[i] - levels[i - 1]) * diff < 1:
            safe = False
            break
        if (levels[i] - levels[i - 1]) * diff > 3:
            safe = False
            break
    result += 1 if safe else 0
print(result)