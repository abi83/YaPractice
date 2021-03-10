def find_in_partially_sorted_array(array, required, from_index, to_index):
    a_index = from_index
    middle_index = (from_index + to_index) // 2
    median = array[middle_index]
    
    b_index = to_index
    if array[from_index] == required:
        return from_index  # TODO: Ускорить тут
    if from_index == to_index:
        return -1
    found = False
    while not found:
        breakpoint()
        if array[a_index] < required < median:
            left = find_in_partially_sorted_array(
                array,
                required,
                from_index,
                middle_index,
            )
            found = True
            return left
        elif median <= required < array[b_index]:
            right = find_in_partially_sorted_array(
                array,
                required,
                middle_index+1,
                to_index)
            found = True
            return right
        else:
            if required > array[a_index]:  # 50% left
                b_index = middle_index
                middle_index = (middle_index + from_index) // 2
            elif required < array[a_index]:  # 50% right
                a_index = middle_index
                middle_index = (middle_index + to_index + 1) // 2
            median = array[middle_index]
            if a_index == b_index:
                found = True

    return -1


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        k = int(file.readline())
        arr = [int(x) for x in file.readline().split()]
    print(find_in_partially_sorted_array(arr, k, 0, n-1))
