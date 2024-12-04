import input
import input_sample

reports = input.input.split("\n")[1:-1]

def is_safe(levels):
    if levels[1] < levels[0]:
        diff = -1
    elif levels[1] > levels[0]:
        diff = 1
    else:
        return False
    safe = True
    for i in range(1, len(levels)):
        if (levels[i] - levels[i - 1]) * diff < 1:
            safe = False
            break
        if (levels[i] - levels[i - 1]) * diff > 3:
            safe = False
            break
    return safe

result = 0
for report in reports:
    levels = [int(_) for _ in report.split()]
    safe = False
    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i + 1:]):
            safe = True
            break
    result += 1 if safe else 0
print(result)

