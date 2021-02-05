# success try id: 47975118


def main():
    with open('input.txt') as file:
        k = int(file.readline().strip())
        data = file.read().strip().replace('\n', '')

    points = 0
    for t in range(1, 10):
        if 0 < data.count(str(t)) <= k*2:
            points += 1

    print(points)


if __name__ == '__main__':
    main()
