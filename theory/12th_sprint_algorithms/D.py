"""
Метеорологическая служба вашего города решила измерять нестабильность погоды
новым способом. Назовём хаотичностью погоды за n дней число дней, в которые
температура строго больше, чем в день до (если такой существует) и в день после
текущего (если такой существует). Например, если за 5 дней температура воздух
составляла 1 2 5 4 8 градусов, то хаотичность за этот период равна 2: в 3-й и
5-й дни выполнялись описанные условия. Определите по ежедневным показаниям
температуры хаотичность погоды за этот период.
"""


def main():
    with open('input.txt') as file:
        data = file.read().strip().split('\n')
        n = int(data[0])
        data = [int(element) for element in data[1].split()]
        count = 0
        for i in range(1, n-1):
            count += data[i] > data[i-1] and data[i] > data[i+1]

        try:
            count += data[0] > data[1]
            count += data[-1] > data[-2]
        except IndexError:
            count += 1
        print(count)


if __name__ == '__main__':
    main()
