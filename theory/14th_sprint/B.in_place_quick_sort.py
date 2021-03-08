def in_place_quick_sort(arr):
    left = 0
    right = len(arr) - 1
    pivot = arr[(right+left) // 2]
    print(pivot)
    while left < right:
        print('left: ', left, 'right: ', right, 'pivot: ', pivot)
        print(*arr)
        # breakpoint()
        if arr[left] < pivot:
            left += 1
        if arr[right] > pivot:
            right -= 1
        if (arr[left] >= pivot >= arr[right]
                # or arr[left] == pivot
                # or arr[right] == pivot
        ):
            arr[left], arr[right] = arr[right], arr[left]
            if arr[left] == pivot and arr[right] == pivot:
                arr[left], arr[left+1] = arr[left+1], arr[left]

    return arr


if __name__ == '__main__':
    with open('input.txt') as file:
        print(in_place_quick_sort([int(x) for x in file.readline().split()]))