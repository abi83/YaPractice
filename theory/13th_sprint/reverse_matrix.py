with open('input.txt') as file:
    lines_orifinal = int(file.readline())
    rows_original = int(file.readline())
    matrix_original = [row.split() for row in file.read().strip().split('\n')]

matrix_reversed = []
index = 0
for index in range(0, rows_original):
    new_row = []
    for row in matrix_original:
        new_row.append(row[index])
    matrix_reversed.append(new_row)

# breakpoint()
for row in matrix_reversed:
    print(*row)
