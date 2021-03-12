"""
some specific bubble sort
"""


def bubble_sort(arr):
    times = 0
    for i_index in range(len(arr)-1):
        j = 0
        changed = False
        while j < len(arr)-1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                changed, times = True, times+1
            j += 1
        if changed:
            print(*arr)
    if times == 0:
        print(*arr)
    return arr


if __name__ == '__main__':
    with open('input.txt') as file:
        n = file.readline()
        arr = [int(x) for x in file.readline().strip().split()]
    # print(array)
    bubble_sort(arr)