def check_subsequence(short, long) -> bool:
    """
    Checking string subsequence recursively
    @param short: This substring is searching
    @param long: Here we search in
    @return: False or None
    """
    try:
        return check_subsequence(short[1:], long[long.index(short[0])+1:])
    except ValueError:  # Index was not found
        return False
    except IndexError:  # The last element exceeded without false
        return True


def check_subsequence2(short, long):
    previous_index = -1
    for element in short:
        try:
            index = long[previous_index + 1:].index(element)
        except ValueError:  # Index was not found
            return False
        previous_index = index
    return True


if __name__ == '__main__':
    with open('input.txt') as file:
        inner = file.readline().strip()
        big_one = file.readline().strip()

    print(check_subsequence2(inner, big_one))
