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


def items_from_file():
    items = []

    with open('input.txt') as file:
        n = int(file.readline())
        next_item = Node('First item')

        for i in range(n):
            current_item = next_item
            current_item.value = file.readline().strip()
            next_item = Node('Next item item')
            next_item.next_item = current_item
            items.append(current_item)
    return current_item


def two_way_items_from_file():
    items = []

    with open('input.txt') as file:
        n = int(file.readline())
        next_item = DoubleConnectedNode('First item')

        for i in range(n):
            current_item = next_item
            next_item = DoubleConnectedNode('Next item')

            current_item.value = file.readline().strip()
            current_item.next = next_item

            next_item.prev = current_item
            items.append(current_item)
    current_item.next = None
    breakpoint()
    return current_item
