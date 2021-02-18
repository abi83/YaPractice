def calculate_distances(street):
    street_length = len(street)
    zeroes_indexes = [
        index for index, value in enumerate(street) if value == '0']
    # populate until first zero
    first_zero_index = zeroes_indexes[0]
    for position in range(0, first_zero_index):
        yield first_zero_index - position
    # for each pair of zero indexes populate the distances between
    for left_zero_position, right_zero_position in \
            zip(zeroes_indexes[0:-1], zeroes_indexes[1:]):
        yield 0  # for left_zero_position, then inner loop
        # excluding right zero, it will be populated later
        for position in range(left_zero_position + 1, right_zero_position):
            yield min(
                position - left_zero_position,
                right_zero_position - position
            )
    # populate from last zero, including it
    last_zero_index = zeroes_indexes[-1]
    for position in range(last_zero_index, street_length):
        yield position - last_zero_index


if __name__ == '__main__':
    input()
    print(*calculate_distances(input().split()))
