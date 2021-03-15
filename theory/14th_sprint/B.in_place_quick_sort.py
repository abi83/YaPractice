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
    if to_index <= from_index:
        return
    pivot = array[to_index] if pivot is None else pivot

    left = from_index
    right_pivot_pos = to_index
    left_pivot_pos = to_index
    while left < left_pivot_pos:
        if array[left] < pivot:
            left += 1
        elif array[left] > pivot:
            array[left], array[right_pivot_pos] = array[right_pivot_pos], array[left]
            right_pivot_pos -= 1
        elif array[left] == pivot:
            left_pivot_pos -= 1
            array[left], array[left_pivot_pos] = array[left_pivot_pos], array[left]

    in_place_quick_sort(array, from_index, left_pivot_pos - 1)
    in_place_quick_sort(array, right_pivot_pos + 1, to_index)

    return array


if __name__ == '__main__':
    with open('input.txt') as in_file:
        participants = [int(x) for x in in_file.readline().split()]





    # from collections import namedtuple
    # Participant = namedtuple('Participant', ['name', 'tasks', 'penalty'])
    #
    # with open('input.txt') as in_file:
    #     elements_number = int(in_file.readline())
    #     participants = []
    #
    #     for index in range(elements_number):
    #         participants.append(Participant(*in_file.readline().split()))
    # run
    in_place_quick_sort(participants)
    # output
    # for participant in participants:
    #     print(participant)
    print(participants)
