def merge(arr: list, left: int, mid: int, right: int) -> list:
    lef_arr_index = left
    right_arr_index = mid
    merged_arr = [None] * (right - left)
    for i in range(right-left):
        if arr[lef_arr_index] <= arr[right_arr_index]:
            merged_arr[i] = arr[lef_arr_index]
            if lef_arr_index < mid - 1:
                lef_arr_index += 1
            else:
                lef_arr_index = right - 1
        else:
            merged_arr[i] = arr[right_arr_index]
            if right_arr_index < right - 1:
                right_arr_index += 1
            else:
                right_arr_index = mid - 1
    return merged_arr


def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left > 1:
        merge_sort(arr, left, (left + right) // 2)
        merge_sort(arr, (left + right) // 2, right)
        arr[left:right] = merge(arr, left, (left + right) // 2, right)


if __name__ == '__main__':
    with open('input.txt') as file:
        arr = [int(x) for x in file.readline().split()]
        arr1 = [int(x) for x in file.readline().split()]

    print(arr)
    merge_sort(arr, 0, 12)
    print(arr)
