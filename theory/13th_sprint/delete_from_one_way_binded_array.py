def solution(number, node) -> None:
    find_next = lambda x: x.next

    current_item = node
    assert number > 1, 'Smth is wrong'
    for n in range(number):
        next_item = find_next(current_item)
        previous_item = current_item
        current_item = next_item

    previous_item.next = next_item
