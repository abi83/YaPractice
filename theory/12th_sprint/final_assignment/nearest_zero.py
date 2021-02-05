# success try id: 47973669

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
        except TypeError:  # distance = 'unknown'
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
        street = (int(symbol) for symbol in file.readline().strip().split())

    left_side_generator = first_iteration(street)
    output = back_iteration(list(left_side_generator), n)
    for element in output:
        print(element, end=' ')


if __name__ == '__main__':
    main()
