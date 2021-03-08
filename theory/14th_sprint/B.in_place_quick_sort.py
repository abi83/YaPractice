import time


def in_place_quick_sort(arr):
    left = 0
    right = len(arr) - 1
    pivot = arr[0]
    print(pivot)
    pivots_count = 1
    while left < right:
        print('left: ', left, 'right: ', right, 'pivot: ', pivot)
        print(*arr)
        # time.sleep(0.5)
        left_element = arr[left]
        right_element = arr[right]
        breakpoint()
        if (arr[left] > pivot >= arr[right]):
            arr[left], arr[right] = arr[right], arr[left]
            continue
        if arr[left] == pivot and arr[right] == pivot:
            arr[left], arr[right-pivots_count] = arr[right-pivots_count], arr[left]
            pivots_count += 1
            right += 1
            # left -=1
            continue
        if arr[left] < pivot:
            left += 1
        if arr[right] > pivot:
            right -= 1


    return arr


if __name__ == '__main__':
    with open('input.txt') as file:
        print(in_place_quick_sort([int(x) for x in file.readline().split()]))