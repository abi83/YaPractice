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


def first_iteration(street, n):
    index = 0
    street_list = list(street)
    distance = 'unknown'
    while index < n:
        if street_list[index] == 0:
            print(f'index: {index}. element: {street_list[index]}. distance: {distance}')
            distance = 0
            yield 0
        else:
            print(f'index: {index}. element: {street_list[index]}. distance: {distance}')
            yield distance
        index += 1
        if distance != 'unknown':
            distance += 1


def main():
    with open('input.txt') as file:
        n = int(file.readline().strip())
        street = map(int, file.readline().strip().split())
    # print(n, street)

    output1 = first_iteration(street, n)
    print(list(output1))



if __name__ == '__main__':
    main()
