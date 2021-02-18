def solution(head):
    current_item = head
    previous_item = None

    while True:

        next_item = current_item.next
        current_item.next, current_item.prev = previous_item, next_item
        current_item = next_item
