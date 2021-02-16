import logging


def found_zeroes(street: list):
    """
    Returns a list of zero element's indexes
    """
    return [i for i in range(len(street)) if street[i] == '0']


def populate_until_first_zero(first_zero_index: int):
    """
    Returns a subarray of distances like [n, n-1, n-2, ..., 3, 2, 1]
    from beginning of street to first zero.
    Excludes the 0 at first_zero_index place
    """
    answer = [i for i in range(first_zero_index, 0, -1)]
    logging.debug(
        f'first_zero: {answer} for first index: {first_zero_index}')
    return answer


def populate_between_two_zeroes(from_index: int, until_index: int):
    """
    Returns a subarray of distances between two zeroes like
    [0, 1, 2, 3, ... top, ... 3, 2, 1,]
    Excludes the 0 at the last place
    """
    max_distance = (until_index - from_index) // 2
    top = (until_index-from_index) % 2

    # [0, 1, 2, ..., max_distance], including starting 0
    upp_stairs = [i for i in range(0, max_distance+1)]
    # [top(if exists), max_distance, ..., 2, 1, ], excluding 0
    down_stairs = [i for i in range(max_distance - 1 + top, 0, -1)]

    logging.debug(
        f'max_distance: {max_distance}', 'top: {top}')
    logging.debug(
        f'upper_stairs: {upp_stairs}, down_stairs: {down_stairs}')
    logging.debug(
        f'Between:{from_index} and {until_index}: {upp_stairs + down_stairs}')
    return upp_stairs + down_stairs


def populate_after_last_zero(last_zero_index: int, street_length: int):
    """
    Returns a subarray of distances like [0, 1, 2, 3,...n] after the last zero.
    Including the 0 at fist place
    """
    answer = [i for i in range(0, street_length - last_zero_index)]
    logging.debug(
        f'last_zero: {answer} for last index: {last_zero_index}')
    return answer


def console_input():
    street_length = int(input())
    street = [symbol for symbol in input().strip().split()]
    return street_length, street


def console_output(answer: list):
    print(*answer)


def file_input():
    with open('input.txt') as file:
        street_length = int(file.readline().strip())
        street = [symbol for symbol in file.readline().strip().split()]
    return street_length, street


def file_output(answer: list):
    with open('output.txt', 'w') as file:
        file.write(' '.join([str(element) for element in answer]))


def main():
    street = file_input()[1]
    zeroes_indexes = found_zeroes(street)
    answer = populate_until_first_zero(zeroes_indexes[0])
    for i in range(len(zeroes_indexes)-1):
        answer += populate_between_two_zeroes(
            zeroes_indexes[i], zeroes_indexes[i+1]
        )
    answer += populate_after_last_zero(zeroes_indexes[-1], len(street))
    file_output(answer)


if __name__ == '__main__':
    logging.basicConfig(
        filename=__file__ + '.log',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        datefmt='%d-%b-%y %H:%M:%S')
    main()
