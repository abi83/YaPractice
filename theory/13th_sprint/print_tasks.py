from utils import *


def solution(node) -> None:
    try:
        solution(node.next_item)
    except AttributeError:
        return
    print(node.value)


if __name__ == '__main__':
    solution(items_from_file())