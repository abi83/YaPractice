from utils import DoubleConnectedNode, two_way_items_from_file
from print_tasks import solution as s


def solution(head):
    current_item = head
    previous_item = None

    while True:

        next_item = current_item.next
        current_item.next, current_item.prev = previous_item, next_item
        current_item = next_item


if __name__ == '__main__':
    s(two_way_items_from_file())