def solution(node) -> None:
    print(node.value)
    try:
        solution(node.next)
    except Exception:
        pass
