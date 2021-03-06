from utils import *


def solution(head):
    next_item = head
    current_item = None
    # items = []
    while True:
        try:
            previous_item = current_item
            current_item = next_item
            next_item = current_item.next
            current_item.next, current_item.prev = previous_item, next_item

            # items.append(current_item)

        except AttributeError:
            return previous_item


if __name__ == '__main__':
    print_double_connected_node_array(double_connected_node_from_file())
    print('=======================')
    print_double_connected_node_array(solution(double_connected_node_from_file()))