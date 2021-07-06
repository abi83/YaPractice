"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его
соседей. Соседним считается элемент, находящийся от текущего на одну ячейку
влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.
"""


def main():
    with open('input.txt') as file:
        data = file.read().strip().split('\n')
        matrix = [data[n].split() for n in range(2, len(data)-2)]
        x = int(data[-2])
        y = int(data[-1])
        for m, n in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            try:
                if x+m >= 0 and y+n >= 0:
                    yield int(matrix[x+m][y+n])
            except IndexError:
                pass


for element in sorted(list(main())):
    print(element, end=' ')
