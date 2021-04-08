class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def find_max_value_in_binary_tree(node: Node) -> int:
    max_l, max_r = node.value, node.value
    if node.left:
        max_l = find_max_value_in_binary_tree(node.left)
    if node.right:
        max_r = find_max_value_in_binary_tree(node.right)
    return max(node.value, max_l, max_r)
