class Participant:
    def __init__(self, name, tasks, penalty):
        self.name = name
        self.tasks = int(tasks)
        self.penalty = int(penalty)

    def __gt__(self, other):
        if self.tasks != other.tasks:
            return self.tasks > other.tasks
        if self.penalty != other.penalty:
            return self.penalty < other.penalty
        return self.name < other.name

    def __lt__(self, other):
        if self.tasks != other.tasks:
            return self.tasks < other.tasks
        if self.penalty != other.penalty:
            return self.penalty > other.penalty
        return self.name > other.name

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __eq__(self, other):
        return (self.tasks == other.tasks
                and self.penalty == other.penalty
                and self.name == other.name)

    def __repr__(self):
        return f'Participant "{self.name}" with {self.tasks} tasks and {self.penalty} penalty'

    def __str__(self):
        return self.name


def in_place_quick_sort(arr, from_index=None, to_index=None, pivot=None):
    from_index = 0 if from_index is None else from_index
    to_index = len(arr) - 1 if to_index is None else to_index
    pivot = arr[0] if pivot is None else pivot

    if to_index <= from_index:
        return arr
    left, right = from_index, to_index
    left_pivot_pos, right_pivot_pos = from_index, to_index
    double_pivot = False
    while left <= right_pivot_pos:
        if not double_pivot:
            if arr[left] == pivot == arr[right]:
                left_pivot_pos, right_pivot_pos = left, right
                double_pivot = True
                continue
            if arr[left] >= pivot >= arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
            if arr[left] < pivot:
                left += 1
            if arr[right] > pivot:
                right -= 1
        else:
            if arr[left] < pivot:
                arr[left_pivot_pos], arr[left] = arr[left], arr[left_pivot_pos]
                left_pivot_pos += 1
                left += 1
            elif arr[left] > pivot:
                arr[left], arr[right_pivot_pos] = arr[right_pivot_pos], arr[left]
                right_pivot_pos -= 1
            else:
                left += 1

    good_pivot_left = arr[left_pivot_pos - 1]

    try:
        good_pivot_right = arr[right_pivot_pos + 1]
    except IndexError:
        good_pivot_right = arr[-1]

    in_place_quick_sort(arr, from_index, left_pivot_pos - 1, good_pivot_left)
    in_place_quick_sort(arr, right_pivot_pos + 1, to_index, good_pivot_right)

    return arr


if __name__ == '__main__':
    # console input
    # n = int(input())
    # participants = [None] * n
    # for i in range(n):
    #     participants[i] = Participant(*input().split())

    # file input
    with open('input.txt') as file:
        n = int(file.readline())
        participants = [None] * n
        for i in range(n):
            # participants[i] = Participant(*file.readline().split())
            data = file.readline().split()
            participants[i] = tuple([-int(data[1]), int(data[2]), data[0]])

    # print(participants)
    # run
    in_place_quick_sort(participants)
    # print(participants)
    for participant_index in range(n):
        print(participants[participant_index][2])