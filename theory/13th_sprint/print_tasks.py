from utils import *


def solution(node) -> None:
    current = node
    while True:
        try:
            print(current.value)
            current = current.next_item
        except AttributeError:
            return


if __name__ == '__main__':
    solution(node_items_from_file())