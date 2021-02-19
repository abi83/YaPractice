def solution(node) -> None:
    current = node
    while True:
        try:
            print(current.value)
            current = current.next_item
        except AttributeError:
            return
