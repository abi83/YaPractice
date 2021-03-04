"""
Binary tree search
"""


def binary_tree_search(values_list, value, left=None, right=None):
    """
    Searching the value in sorted list with binary tree algorithm
    @param right: right index of sublist
    @param left: left index of sublist
    @param values_list: list, where we searching the value
    @param value: searching value
    @return: Index ef list element with value or -1 if not found
    """
    left = 0 if left is None else left
    right = len(values_list)-1 if right is None else right
    middle = (right+left) // 2
    if right <= left:
        return -1
    if middle == 0 or values_list[middle-1] < value <= values_list[middle]:
        return middle + 1

    if values_list[middle] >= value:
        return binary_tree_search(
            values_list, value, left, middle
        )
    elif values_list[middle] < value:
        return binary_tree_search(
            values_list, value, middle+1, right
        )


if __name__ == '__main__':
    n = int(input())
    l = [int(x) for x in input().split()]
    x = int(input())
    print(binary_tree_search(l, x), end=' ')
    print(binary_tree_search(l, x*2))

