import input

input = input.input
# input = """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """

l = [list(_) for _ in input.split("\n")[1:-1]]

result = 0
row = len(l)
col = len(l[0])

for i in range(1, row - 1):
    for j in range(1, col - 1):
        if "".join([l[i-1][j-1],l[i][j],l[i+1][j+1]] ) in ['MAS', 'SAM'] \
        and "".join([l[i-1][j+1],l[i][j],l[i+1][j-1]] ) in ['MAS', 'SAM']:
            result += 1

print(result)