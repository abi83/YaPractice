def solution(head):
    next_item = head
    current_item = None
    while True:
        try:
            previous_item = current_item
            current_item = next_item
            next_item = current_item.next
            current_item.next, current_item.prev = previous_item, next_item

        except AttributeError:
            return previous_item
