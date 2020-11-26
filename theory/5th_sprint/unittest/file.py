def series_sum(incoming):
    """Конкатенирует все элементы списка, приводя их к строкам."""
    result = ''
    for i in incoming:
        result += str(i)
    return result