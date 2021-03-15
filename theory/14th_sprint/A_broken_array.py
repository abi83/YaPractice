def binary_search(array, required, from_index: int, to_index: int) -> int:
    """
    Just one more version of binary search in sorted array
    @param from_index: Index to search from
    @param to_index: Index to search to
    @return: Index of required element. -1 if not found
    """
    if array[from_index] == required:
        return from_index
    if from_index == to_index:
        return -1
    middle_index = (from_index + to_index) // 2
    if array[middle_index] == required:
        return middle_index

    if required < array[middle_index]:
        return binary_search(array, required, from_index, middle_index)
    return binary_search(array, required, middle_index+1, to_index)


def find_in_partially_sorted_array(array, required):
    if len(array) == 0:
        return -1
    broken_index = find_broken_index(array, 0, len(array) - 1)
    if broken_index == 0:
        return binary_search(array, required, 0, len(array)-1)
    if array[0] <= required <= array[broken_index - 1]:
        return binary_search(array, required, 0, broken_index-1)
    return binary_search(array, required, broken_index, len(array)-1)


def find_broken_index(arr, from_index, to_index):
    """
    O(log(n)) binary algorithm of broken index search
    """
    if to_index - from_index <= 1:
        return to_index if arr[to_index] < arr[from_index] else from_index
    middle_index = (from_index + to_index) // 2

    if arr[middle_index] > arr[from_index]:
        # left half of array increases, not break in it
        # trying to find broken index in right half
        return find_broken_index(arr, middle_index, to_index)
    return find_broken_index(arr, from_index, middle_index)


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        k = int(file.readline())
        arr = [int(x) for x in file.readline().split()]
    print(find_in_partially_sorted_array(arr, k))
