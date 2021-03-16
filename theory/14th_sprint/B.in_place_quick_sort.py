def in_place_quick_sort(
        array,
        from_index: int = None,
        to_index: int = None,
        compare_func=None,
) -> None:
    """
    Just one more version of in place quick sort algorithm. Array is
    sorted on place, without extra memory usage. The sorting is ascending.
    @param array: Any iterable of objects with fully defined comparison methods
    @param from_index: Index to start sorting
    @param to_index: Index to end sorting
    @param compare_func: function of x,y returning any positive number if x>y,
    negative number if x<y and 0 if x==y
    @return: None
    """
    from_index = 0 if from_index is None else from_index
    to_index = len(array) - 1 if to_index is None else to_index
    if to_index <= from_index:
        return
    if compare_func is None:
        compare_func = lambda x, y: x - y
    pivot = array[to_index]

    left = from_index
    right_pivot_pos = to_index
    left_pivot_pos = to_index
    while left < left_pivot_pos:
        comparison = compare_func(array[left], pivot)
        if comparison < 0:
            left += 1
        elif comparison > 0:
            array[left], array[right_pivot_pos] = array[right_pivot_pos], \
                                                  array[left]
            right_pivot_pos -= 1
        elif comparison == 0:
            left_pivot_pos -= 1
            array[left], array[left_pivot_pos] = array[left_pivot_pos], array[
                left]

    in_place_quick_sort(array, from_index, left_pivot_pos - 1, compare_func=compare_func)
    in_place_quick_sort(array, right_pivot_pos + 1, to_index, compare_func=compare_func)

    return array


if __name__ == '__main__':
    from collections import namedtuple
    Participant = namedtuple('Participant', ['name', 'tasks', 'penalty'])

    with open('input.txt') as in_file:
        participants_count = int(in_file.readline())
        participants = []
        for _ in range(participants_count):
            data = in_file.readline().split()
            participants.append(
                Participant(
                    name=data[0],
                    tasks=int(data[1]),
                    penalty=int(data[2])
                ))

    def participants_compare(participant_x, participant_y):
        if participant_x == participant_y:
            return 0
        if participant_x.tasks - participant_y.tasks != 0:
            return participant_x.tasks - participant_y.tasks
        if participant_x.penalty - participant_y.penalty != 0:
            return participant_y.penalty - participant_x.penalty
        return 1 if participant_y.name > participant_x.name else -1
    in_place_quick_sort(participants, compare_func=participants_compare)

    for participant_index in range(1, participants_count+1):
        print(participants[-participant_index].name)
