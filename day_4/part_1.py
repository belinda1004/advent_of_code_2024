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

# check = [['.'] * 10 for _ in range(10)]

l = [list(_) for _ in input.split("\n")[1:-1]]
# print(l)

result = 0
row = len(l)
col = len(l[0])
# horizontal
# print("horizontal")
for i in range(row):
    for j in range(col - 3):
        if "".join(l[i][j:j+4]) in ['XMAS', 'SAMX'] :
            # check[i][j] = l[i][j]
            # check[i][j+1] = l[i][j+1]
            # check[i][j+2] = l[i][j+2]
            # check[i][j+3] = l[i][j+3]
            result += 1

# vertical
# print("vertical")
for j in range(col):
    for i in range(row - 3):
        if "".join([l[i][j],l[i+1][j],l[i+2][j],l[i+3][j]] ) in ['XMAS', 'SAMX'] :
            # check[i][j] = l[i][j]
            # check[i+1][j] = l[i+1][j]
            # check[i+2][j] = l[i+2][j]
            # check[i+3][j] = l[i+3][j]
            result += 1

# diagonal
# print("diagonal")
for j in range(col-3):
    for i in range(row - 3):
        if "".join([l[i][j],l[i+1][j+1],l[i+2][j+2],l[i+3][j+3]] ) in ['XMAS', 'SAMX'] :
            # check[i][j] = l[i][j]
            # check[i+1][j+1] = l[i+1][j+1]
            # check[i+2][j+2] = l[i+2][j+2]
            # check[i+3][j+3] = l[i+3][j+3]
            result += 1

for i in range(row-3):
    for j in range(3,col):
        if "".join([l[i][j],l[i+1][j-1],l[i+2][j-2],l[i+3][j-3]] ) in ['XMAS', 'SAMX'] :
            # check[i][j] = l[i][j]
            # check[i+1][j-1] = l[i+1][j-1]
            # check[i+2][j-2] = l[i+2][j-2]
            # check[i+3][j-3] = l[i+3][j-3]
            result += 1

# for i in range(10):
#     print("".join(check[i]))
print(result)