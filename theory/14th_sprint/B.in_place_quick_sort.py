def in_place_quick_sort(
        array,
        from_index: int = None,
        to_index: int = None,
        pivot=None) -> None:
    """
    Just one more version of in place quick sort algorithm. Array is
    sorted on place, without extra memory usage. The sorting is ascending.
    @param array: Any iterable of objects with fully defined comparison methods
    @param from_index: Index to start sorting
    @param to_index: Index to end sorting
    @param pivot: Any element of array
    @return: None
    """
    from_index = 0 if from_index is None else from_index
    to_index = len(array) - 1 if to_index is None else to_index
    pivot = array[0] if pivot is None else pivot

    if to_index <= from_index:
        return
    left, right = from_index, to_index
    left_pivot_pos, right_pivot_pos = from_index, to_index
    double_pivot = False
    while left <= right_pivot_pos:
        if not double_pivot:
            if array[left] >= pivot >= array[right]:
                if array[left] == pivot == array[right]:
                    left_pivot_pos, right_pivot_pos = left, right
                    double_pivot = True
                    continue
                array[left], array[right] = array[right], array[left]
            if array[left] < pivot:
                left += 1
            if array[right] > pivot:
                right -= 1
        else:
            if array[left] < pivot:
                array[left_pivot_pos], array[left] =\
                    array[left], array[left_pivot_pos]
                left_pivot_pos += 1
                left += 1
            elif array[left] > pivot:
                array[left], array[right_pivot_pos] =\
                    array[right_pivot_pos], array[left]
                right_pivot_pos -= 1
            else:
                left += 1

    try:
        good_pivot_right = array[right_pivot_pos + 1]
    except IndexError:
        good_pivot_right = array[-1]

    in_place_quick_sort(array, from_index, left_pivot_pos - 1,
                        array[left_pivot_pos - 1])
    in_place_quick_sort(array, right_pivot_pos + 1, to_index,
                        good_pivot_right)

    return array


if __name__ == '__main__':
    with open('input.txt') as in_file:
        elements_number = int(in_file.readline())
        participants = []

        for index in range(elements_number):
            data = in_file.readline().split()
            participants[index] = tuple([-int(data[1]), int(data[2]), data[0]])

    # run
    in_place_quick_sort(participants)
    # output
    for participant_index in range(elements_number):
        print(participants[participant_index][2])
