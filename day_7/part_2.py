
import input
import input_sample

input = input.input
# input = input_sample.input

equations = input.split("\n")[1:-1]

def calculate(pre_result, numbers, value):
    if pre_result > value:
        return False
    if len(numbers) == 0:
        return pre_result == value
    return calculate(pre_result + numbers[0], numbers[1:], value) \
           or calculate(pre_result * numbers[0], numbers[1:], value) \
           or calculate(pre_result * (10 ** len(str(numbers[0]))) + numbers[0], numbers[1:], value)

sum = 0
for equation in equations:
    value, numbers = equation.split(": ")
    value = int(value)
    numbers = [int(_) for _ in numbers.split(" ")]
    sum += value if calculate(numbers[0], numbers[1:], value) else 0

print(sum)