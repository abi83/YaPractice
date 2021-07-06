"""
is_anti_list(["1", "0", "0", "1"],
             ["0", "1", "1", "0"]) ➞ True
is_anti_list(["apples", "bananas", "bananas"],
             ["bananas", "apples", "apples"]) ➞ True
is_anti_list([3.14, True, 3.14],
             [3.14, False, 3.14]) ➞ False
"""


def is_anti_list(list1, list2) -> bool:
    if len(list1) != len(list2):
        return False
    if (set(list1) != set(list2)) or len(set(list1)) != 2:
        return False
    for element1, element2 in zip(list1, list2):
        if element1 == element2:
            return False
    return True


print(is_anti_list(["1", "0", "0", "1"], ["0", "1", "1", "0"]))
print(is_anti_list(["apples", "bananas", "bananas"], ["bananas", "apples", "apples"]))
print(is_anti_list([3.14, True, 3.14], [3.14, False, 3.14]))
print(is_anti_list(["1", "1", "0", "1"], ["0", "1", "1", "0"]))
