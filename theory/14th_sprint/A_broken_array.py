def find_in_partially_sorted_array(array, required):
    left_index, right_index = 0, len(array)
    median = array[left_index]
    middle = array[(right_index - left_index) // 2]
    found = False
    while not found:
        if middle == required:
            found = True
        breakpoint()
        way = ''
        if required < median:
            go = 'right'
        if median < required < middle:
            right_index = (right_index - left_index) // 2
            print('right_index: ', right_index)
            middle = array[(right_index + left_index) // 2]
        else:
            left_index = (right_index + left_index) // 2
            print('left_index: ', left_index)
            middle = array[(right_index + left_index) // 2]

    return middle


if __name__ == '__main__':
    with open('input.txt') as file:
        n = file.readline()
        k = int(file.readline())
        arr = [int(x) for x in file.readline().split()]
    print(find_in_partially_sorted_array(arr, k))
