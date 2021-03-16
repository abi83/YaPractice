def in_place_quick_sort(array, compare_func=None) -> None:
    """
    Just one more version of in place quick sort algorithm. Array is
    sorted on place, without extra memory usage. Default sorting is ascending.
    @param array: Any iterable of objects with defined comparison methods
    @param from_index: Index to start sorting
    @param to_index: Index to end sorting
    @param compare_func: function of x,y returning True if x > y, esle False
    @return: None
    """
    from_index = 0
    to_index = len(array) - 1
    if compare_func is None:
        compare_func = lambda x, y: x > y

    def inner_in_place_quick_sort(array, from_index, to_index, compare_func):
        if to_index <= from_index:
            return

        pivot = array[(to_index + from_index)//2]
        left, right = from_index, to_index
        while left < right:
            while compare_func(pivot, array[left]):
                left += 1
            while compare_func(array[right], pivot):
                right -= 1
            if left < right:
                array[left], array[right] = array[right], array[left]

        inner_in_place_quick_sort(array, from_index, left,
                                  compare_func=compare_func)
        inner_in_place_quick_sort(array, left+1, to_index,
                                  compare_func=compare_func)

    inner_in_place_quick_sort(array, from_index, to_index, compare_func)


if __name__ == '__main__':
    from collections import namedtuple
    Participant = namedtuple('Participant', ['name', 'tasks', 'penalty'])

    with open('input.txt') as in_file:
        participants_count = int(in_file.readline())
        participants = [None] * participants_count
        data = in_file.read().split('\n')
        for index in range(participants_count):
            line = data[index].split()
            participants[index] = Participant(
                name=line[0], tasks=int(line[1]), penalty=int(line[2]))

    # def participants_compare(participant_x, participant_y):
    #     if participant_x.tasks != participant_y.tasks:
    #         return participant_x.tasks < participant_y.tasks
    #     if participant_x.penalty != participant_y.penalty:
    #         return participant_x.penalty > participant_y.penalty
    #     return participant_x.name > participant_y.name

    def participants_compare(participant_x, participant_y):
        if participant_x.tasks < participant_y.tasks:
            return True
        if participant_x.tasks > participant_y.tasks:
            return False
        if participant_x.penalty > participant_y.penalty:
            return True
        if participant_x.penalty < participant_y.penalty:
            return False
        return participant_x.name > participant_y.name

    in_place_quick_sort(participants, compare_func=participants_compare)

    with open('output.txt', 'w') as out_file:
        out_file.write('\n'.join(x.name for x in participants))
