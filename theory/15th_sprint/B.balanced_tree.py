"""
Check if a binary tree is balanced
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


n31 = Node(32)
n32 = Node(17)
n33 = Node(21)
n21 = Node(28, left=n31, right=n32)
n22 = Node(54, left=n33)
n1 = Node(36, left=n21, right=n22)


def solution(node):
    if node.left is None and node.right is not None:
        return node.right.right is None and node.right.left is None

    if node.right is None and node.left is not None:
        return node.left.right is None and node.left.left is None

    left_check, right_check = True, True
    if node.left:
        left_check = solution(node.left)
    if node.right:
        right_check = solution(node.right)

    return left_check and right_check
