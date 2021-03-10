def binary_search(array, required, from_index, to_index):
    if array[from_index] == required:
        return from_index
    if from_index == to_index:
        return -1
    middle_index = (from_index + to_index) // 2

    if array[from_index] < required <= array[middle_index]:
        return binary_search(array, required, from_index, middle_index)
    if array[middle_index+1] <= required <= array[to_index]:
        return binary_search(array, required, middle_index+1, to_index)
    return - 1


def find_in_partially_sorted_array(array, required):
    if len(array) == 0:
        return -1
    broken_index = find_broken_index(array, 0, len(array) - 1)
    if broken_index == 0:
        return binary_search(array, required, 0, len(array)-1)
    elif array[0] <= required <= array[broken_index - 1]:
        return binary_search(array, required, 0, broken_index-1)
    elif array[broken_index] <= required <= array[len(array)-1]:
        return binary_search(array, required, broken_index, len(array)-1)
    else:
        return -1


def find_broken_index_cool(arr, from_index, to_index):
    return arr.index(min(*arr))


def find_broken_index(arr, from_index, to_index):
    if to_index-from_index <= 1:
        b = arr.index(min(arr[from_index:to_index+1]))
        return b
    middle_index = (from_index + to_index) // 2

    if arr[middle_index] > arr[from_index]:
        #левая половина стабильно растет, разрыва в ней нет
        #отправляем рекурсию в правую половину
        return find_broken_index(arr, middle_index, to_index)
    else:
        return find_broken_index(arr, from_index, middle_index)


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        k = int(file.readline())
        arr = [int(x) for x in file.readline().split()]
    print(find_in_partially_sorted_array(arr, k))
    # print(find_broken_index(arr, 0, len(arr)-1))
    # print(binary_search(arr, k, 4, 10))

