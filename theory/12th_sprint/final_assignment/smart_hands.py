"""
Гоша и Кондратий нашли необычный тренажёр для скоростной печати и хотят освоить
его. Тренажёр представляет собой поле из клавиш 4x4, в котором каждый раунд
появляется конфигурация цифр и точек. На каждой клавише написана либо точка,
либо цифра от 1 до 9.
В момент времени t игрок должен одновременно нажать на все клавиши, на которых
написана цифра t. Гоша и Кондратий могут нажать в один момент времени на k
клавиш каждый. Если в момент времени t были нажаты все нужные клавиши, то
игроки получают 1 балл.
Найдите число баллов, которое смогут заработать Гоша и Кондратий, если будут
нажимать на клавиши вдвоём.
"""


def main():
    with open('input.txt') as file:
        k = int(file.readline().strip())
        data = file.read().strip().replace('\n', '')

    points = 0
    for t in range(1, 10):
        if 0 < data.count(str(t)) < k*2:
            print(f't: {t}, count: {data.count(str(t))}')
            points += 1

    print(points)


if __name__ == '__main__':
    main()
