class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def binary_tree_identical(a,b) -> bool:
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return (
                (a.value == b.value) and
                binary_tree_identical(a.left, b.left) and
                binary_tree_identical(a.right, b.right)
        )

    return False
