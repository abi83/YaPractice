class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
    #
    # def __str__(self):
    #     return f'Node: {self.value}'
    #
    # def __repr__(self):
    #     return f'Node: {self.value}'
    #
    #
    # def __str__(self):
    #     return f'Node {self.node.value}, level:{self.level}, leftness: {self.leftness}'
    #
    # def __repr__(self):
    #     return f'Node {self.node.value}, level:{self.level}, leftness: {self.leftness}'


def solution(node):
    class EElement:
        def __init__(self, level, leftness, node):
            self.level = level
            self.leftness = leftness
            self.node = node

    elements = [EElement(0, 0, node)]

    def populate_elements_with_metadata(node, level, leftness):
        if node.left is not None:
            elements.append(EElement(level + 1, leftness + 1, node.left))
            populate_elements_with_metadata(node.left, level+1, leftness+1)
        if node.right is not None:
            elements.append(EElement(level + 1, leftness - 1, node.right))
            populate_elements_with_metadata(node.right, level+1, leftness-1)

    populate_elements_with_metadata(node, 0, 0)

    elements_by_level = {}
    for element in elements:
        try:
            elements_by_level[element.level].append(element)
        except KeyError:
            elements_by_level[element.level] = [element]
    # print(elements_by_level)
    output = []
    for level in elements_by_level:
        output.append(
            [y.node for y in elements_by_level[level] if y .leftness == max([x.leftness for x in elements_by_level[level]])]
        )

    return [x[0] for x in output]


n41 = Node(41)
n31 = Node(33, left=n41)
n32 = Node(32)
n33 = Node(31)
n21 = Node(21, left=n31, right=n32)
n22 = Node(22, left=n33)
n1 = Node(10, left=n21, right=n22)

o = solution(n1)
# breakpoint()
print(o)