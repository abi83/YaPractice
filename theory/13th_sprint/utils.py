class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value


def node_items_from_file():
    items = []

    with open('input.txt') as file:
        n = int(file.readline())
        next_item = Node('First item')

        for i in range(n):
            current_item = next_item
            current_item.value = file.readline().strip()
            next_item = Node('Next item')
            next_item.next_item = current_item
            items.append(current_item)
    return current_item


def print_node_array(node) -> None:
    current = node
    while True:
        try:
            print(current.value)
            current = current.next_item
        except AttributeError:
            return


def double_connected_node_from_file():
    items = []

    with open('input.txt') as file:
        n = int(file.readline())
        new_prev_item = DoubleConnectedNode(file.readline().strip())
        new_prev_item.next = None

        for i in range(n):
            current_item = new_prev_item
            new_prev_item = DoubleConnectedNode('Prev item')
            current_item.prev = new_prev_item
            new_prev_item.next = current_item
            new_prev_item.value = file.readline().strip()

            items.append(current_item)

    current_item.prev = None
    # breakpoint()
    return current_item


def print_double_connected_node_array(node) -> None:
    current = node
    while True:
        try:
            print(current.value)
            current = current.next
        except AttributeError:
            return

