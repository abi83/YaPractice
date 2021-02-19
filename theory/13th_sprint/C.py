def solution(node, number) -> None:
    previous_item = None
    next_item = node
    for n in range(1, number+1):
        current_item = next_item
        next_item = current_item.next_item
        previous_item = current_item
    try:
        previous_item.next_item = next_item.next_item
    except AttributeError:
        return node.next_item
    return node
