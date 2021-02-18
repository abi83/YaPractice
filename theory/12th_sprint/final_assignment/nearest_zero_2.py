def calculate_distances(street, required='0'):
    street_length = len(street)
    zeroes_pos = [
        pos for pos, value in enumerate(street) if value == required]
    # populate until first zero
    first_zero_pos = zeroes_pos[0]
    for pos in range(0, first_zero_pos):
        yield first_zero_pos - pos
    # for each pair of zero positions populate the distances between
    for left_zero_pos, right_zero_pos in (
                zip(zeroes_pos[0:-1], zeroes_pos[1:])):
        yield 0  # for left_zero_pos, then inner loop
        # excluding right zero, it will be populated later
        for pos in range(left_zero_pos + 1, right_zero_pos):
            yield min(
                pos - left_zero_pos,
                right_zero_pos - pos
            )
    # populate from last zero, including it
    last_zero_pos = zeroes_pos[-1]
    for pos in range(last_zero_pos, street_length):
        yield pos - last_zero_pos


if __name__ == '__main__':
    input()
    print(*calculate_distances(input().split()))
