def solution(node, seached_element) -> int:
    find_next = lambda x: x.next

    current_element = node
    n = 0
    while True:
        if current_element == seached_element:
            return n
        next_element = find_next(current_element)
        if next_element == None:
            return -1
        n += 1
        current_element = next_element