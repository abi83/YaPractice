"""
Get all elements of a tree ordered by nesting level
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


def tree_to_array_of_rows(node):
    result = [[node.value], ]
    next_level = []
    if node.left:
        next_level.append(node.left)
    if node.right:
        next_level.append(node.right)
    while next_level:
        result.append([item.value for item in next_level])
        #  recombine next_level with next level elements
        next_level = [f(x) for x in next_level for f in (lambda x: x.left, lambda x: x.right) if f(x) is not None]
    return result


print(tree_to_array_of_rows(n1))
