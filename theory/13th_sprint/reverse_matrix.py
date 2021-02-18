with open('input.txt') as file:
    lines_orifinal = int(file.readline())
    rows_original = int(file.readline())
    matrix_original = [row.split() for row in file.read().split('\n')]

matrix_reversed = []
for i in range(0, rows_original):
    matrix_reversed.append([row[i] for row in matrix_original])

for row in matrix_reversed:
    print(*row)
