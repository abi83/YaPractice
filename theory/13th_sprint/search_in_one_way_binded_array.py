from utils import *


def solution(node, searched_element) -> int:
    current_element = node
    n = 0
    while True:
        if current_element.value == searched_element:
            return n
        next_element = current_element.next_item
        if next_element == None:
            return -1
        n += 1
        current_element = next_element


if __name__ == '__main__':
    print(solution(node_items_from_file(), 'n kkt yb ct'))
