# success try id: 48475209. 1.43s, 117.06Mb

def found_zeroes(street: list):
    """
    Returns a list of zero element's indexes
    """
    return [i for i in range(len(street)) if street[i] == '0']


def console_input():
    return int(input()), input().split()


def main():
    street_length, street = console_input()
    answer: list = [None] * street_length
    zeroes_indexes = found_zeroes(street)
    # populate until first zero
    for index in range(0, zeroes_indexes[0]):
        answer[index] = zeroes_indexes[0] - index
    # for each pair of zero indexes populate the distances between
    for left_zero_position, right_zero_position in zip(
            zeroes_indexes[0:-1], zeroes_indexes[1:]):
        for inner_index in range(left_zero_position, right_zero_position):
            assert answer[inner_index] is None,\
                'Something is going absolutely wrong'
            answer[inner_index] = min(
                inner_index - left_zero_position,
                right_zero_position - inner_index
            )
    # populate from last zero
    for index in range(zeroes_indexes[-1], street_length):
        answer[index] = index - zeroes_indexes[-1]

    print(*answer)


if __name__ == '__main__':
    main()
