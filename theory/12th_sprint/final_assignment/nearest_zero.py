"""
Улица, на которой хочет жить Тимофей, имеет длину n, то есть состоит из n
одинаковых идущих подряд участков. На каждом участке либо уже построен дом,
либо участок пустой. Тимофей ищет место для строительства своего дома. Тимофей
очень общителен и не хочет жить далеко от знакомых, которых у него вся улица.
Чтобы оптимально выбрать место для строительства, он хочет для каждого участка
знать расстояние до ближайшего пустого участка. (Для пустого участка эта
величина будет равна нулю — расстояние до самого себя.)

Ваша задача — помочь Тимофею посчитать искомые расстояния. Для этого у вас есть
карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором
троились, поэтому их номера на карте никак не упорядочены. Пустые участки
обозначены нулями.
"""


def first_iteration(street):
    distance = 'unknown'
    for element in street:
        if element == 0:
            distance = 0
            yield 0
        else:
            yield distance
        try:
            distance += 1
        except TypeError:
            pass


def back_iteration(street, n):
    distance = 'unknown'
    zero_found = False
    for index in range(1, n+1):
        if zero_found:
            distance += 1
            try:
                if distance < street[-index]:
                    street[-index] = distance
                else:
                    # left house is closer, our zero doesn't matter
                    zero_found = False
            except TypeError:  # street[-index] == 'unknown'
                street[-index] = distance

        if street[-index] == 0:
            distance = 0
            zero_found = True

    return street


def main():
    with open('input.txt') as file:
        n = int(file.readline().strip())
        street = (int(x) for x in file.readline().strip().split())

    output1 = first_iteration(street)
    output2 = back_iteration(list(output1), n)
    for element in output2:
        print(element, end=' ')


if __name__ == '__main__':
    main()
