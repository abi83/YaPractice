class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def items_from_file():
    items = []

    with open('input.txt') as file:
        n = int(file.readline())
        next_item = Node('fist one')

        for i in range(n):
            current_item = next_item
            current_item.value = file.readline().strip()
            next_item = Node('Some item')
            current_item.next_item = next_item
            items.append(current_item)
    items[-1].next_item = None
    return items[0]
