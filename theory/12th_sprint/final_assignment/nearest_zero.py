# success try id: 47973669

def first_iteration(street):
    """
    Outputting an 'upstairs' row from each 0 found in street.
    From left to right.
    None (unknown) values before first zero found
    """
    distance = None
    for element in street:
        if element == '0':
            distance = 0
            yield 0
        else:
            yield distance
        try:
            distance += 1
        except TypeError:  # distance = None. It is still unknown.
            pass


def back_iteration(street, n):
    """
    Populating 'upstairs' row for each 0 found in string from left to right
    If left zero is closer to current position distance remaining the same
    """
    distance = None
    zero_found = False
    for index in range(1, n+1):
        if zero_found:
            distance += 1
            try:
                if distance < street[-index]:
                    street[-index] = distance
                else:
                    # left zero is closer
                    # distance to right zero doesn't matter
                    zero_found = False
            except TypeError:  # street[-index] == None
                street[-index] = distance

        if street[-index] == 0:
            distance = 0
            zero_found = True

    return street


def main():
    street_length = int(input())
    street = (symbol for symbol in input().strip().split())
    left_side_generator = first_iteration(street)
    output = back_iteration(list(left_side_generator), street_length)
    print(*output)


if __name__ == '__main__':
    main()
