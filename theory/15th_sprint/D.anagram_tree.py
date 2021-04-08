"""
Compare trees like an anagram
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return f'Node: {self.value}'

    def __repr__(self):
        return f'Node: {self.value}'


n31 = Node(7)
n32 = Node(7)
n33 = Node(7)
n34 = Node(7)
n21 = Node(28, left=n31, right=n32)
n22 = Node(28, left=n33, right=n34)
n1 = Node(99, left=n21, right=n22)


def solution(node):
    next_level_left, next_level_right = [], []
    if node.left:
        next_level_left.append(node.left)
    if node.right:
        next_level_right.append(node.right)
    while next_level_left or next_level_right:
        if not next_level_left and next_level_right:
            return False
        for left_item, right_item in zip(next_level_left, next_level_right[::-1]):
            if left_item.value != right_item.value:
                return False
        next_level_left = [f(x) for x in next_level_left for f in (lambda x: x.left, lambda x: x.right) if f(x) is not None]
        next_level_right = [f(x) for x in next_level_right for f in (lambda x: x.left, lambda x: x.right) if f(x) is not None]

    return True


print(solution(n1))
