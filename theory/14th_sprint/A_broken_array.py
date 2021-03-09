def find_in_partially_sorted_array(array, required, from_index, to_index):
    a = array[from_index]
    middle_index = (from_index + to_index) // 2
    median = array[middle_index]
    
    b = array[to_index]
    if array[from_index] == required:
        return from_index
    if from_index == to_index:
        return -1
    found = False
    while not found:
        # breakpoint()
        if a < required < median:
            left = find_in_partially_sorted_array(
                array,
                required,
                from_index,
                middle_index,
            )
            found = True
            return left
        elif median <= required < b:
            right = find_in_partially_sorted_array(
                array,
                required,
                middle_index,
                to_index)
            found = True
            return right
        else:
            if required > a:  # 50% left
                b = array[middle_index]
                middle_index = (middle_index + from_index) // 2
            elif required < a:  # 50% right
                a = array[middle_index]
                middle_index = (middle_index + to_index) // 2
            median = array[middle_index]
    # breakpoint()
    return -1


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        k = int(file.readline())
        arr = [int(x) for x in file.readline().split()]
    print(find_in_partially_sorted_array(arr, k, 0, n-1))
