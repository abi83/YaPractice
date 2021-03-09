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

    try:
        good_pivot_left = arr[left_pivot_pos - 1]
        good_pivot_right = arr[right_pivot_pos + 1]
    except IndexError:
        good_pivot_left = arr[0]
        good_pivot_right = arr[-1]

    in_place_quick_sort(arr, from_index, left_pivot_pos - 1, good_pivot_left)
    in_place_quick_sort(arr, right_pivot_pos + 1, to_index, good_pivot_right)

    return arr


if __name__ == '__main__':
    with open('input.txt') as file:
        a = [int(x) for x in file.readline().split()]
        print(
            in_place_quick_sort(a)
        )
