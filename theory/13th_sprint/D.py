def solution(node, searched_element):
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
