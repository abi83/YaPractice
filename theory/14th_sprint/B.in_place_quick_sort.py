def in_place_quick_sort(arr, left, right, pivot):
    if right <= left:
        return arr
    left_origin = left
    right_origin = right
    double_pivot = False
    left_pivot_pos, right_pivot_pos = left, right
    while left <= right_pivot_pos:
        if double_pivot:
            if arr[left] < pivot:
                arr[left_pivot_pos], arr[left] = arr[left], arr[left_pivot_pos]
                left_pivot_pos += 1
                left +=1
            elif arr[left] > pivot:
                arr[left], arr[right_pivot_pos] = arr[right_pivot_pos], arr[left]
                right_pivot_pos -= 1
            else:
                left += 1
        else:
            if arr[left] >= pivot >= arr[right]:
                if arr[left] == pivot == arr[right]:
                    left_pivot_pos, right_pivot_pos = left, right
                    double_pivot = True
                arr[left], arr[right] = arr[right], arr[left]
            if arr[left] < pivot:
                left += 1
            if arr[right] > pivot:
                right -= 1

    good_pivot = arr[left_pivot_pos - 1]
    in_place_quick_sort(arr, left_origin, left_pivot_pos - 1, good_pivot)
    try:
        good_pivot = arr[right_pivot_pos+1]
    except IndexError:
        good_pivot = arr[-1]
    in_place_quick_sort(arr, right_pivot_pos + 1, right_origin, good_pivot)

    return arr


if __name__ == '__main__':
    with open('input.txt') as file:
        a = [int(x) for x in file.readline().split()]
        print(
            in_place_quick_sort(
                a,
                0,
                len(a)-1,
                7
            )
        )
