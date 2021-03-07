def merge(arr: list, left: int, mid: int, right: int) -> list:
    lef_arr_index = left
    right_arr_index = mid
    merged_arr = [None] * (right - left)
    for i in range(right-left):
        if arr[lef_arr_index] <= arr[right_arr_index]:
            merged_arr[i] = arr[lef_arr_index]
            lef_arr_index = (
                lef_arr_index + 1 if lef_arr_index < mid - 1
                else arr.index(max(arr[mid-1], arr[right-1])))
        else:
            merged_arr[i] = arr[right_arr_index]
            right_arr_index = (
                right_arr_index + 1 if right_arr_index < right - 1
                else arr.index(max(arr[mid-1], arr[right-1])))
    return merged_arr


def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left > 1:
        merge_sort(arr, left, (left + right) // 2)
        merge_sort(arr, (left + right) // 2, right)
    # breakpoint()
    #     for i in range(left, right):
        a = merge(arr, left, (left + right) // 2, right)
        arr[left:right] = a
        breakpoint()





    # for i in range(len(arr) // 2):
    #     # print(i)
    #     # print(merge(arr, i * 2, i * 2 + 1, (i + 1) * 2))
    #     arr[i*2], arr[i*2 + 1] = merge(arr, i*2, i*2 + 1, (i + 1)*2)
    # for i in range(len(arr) // 4):
    #     print(merge(arr, i*4, i*4 + 2, (i + 1)*4))


if __name__ == '__main__':
    with open('input.txt') as file:
        arr = [int(x) for x in file.readline().split()]
        arr1 = [int(x) for x in file.readline().split()]

    print(arr)
    merge_sort(arr, 0, 8)
    print(arr)

    # print(merge(arr1, 0, 1, 2))
