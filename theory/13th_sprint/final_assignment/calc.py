# success try: 49009361, 11 мрт 2021, 18:20:45, 53ms, 3.98Mb

from collections.abc import Iterable


class Stack:
    """
    Extremely simple stack class with pop and append methods
    """
    def __init__(self):
        self.data = []

    def append(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()


def calculate_reverse_polish_notation(expression: Iterable) -> int:
    """
    Input: A 'reverse polish notation' iterable with numbers and
        operations symbols [+,-,*,/]. Example: [7, 2, '+', 4, '*', 2, '+']'
    Output: Calculated value or last calculated value in stack,
        if not enough operation symbols provided
    """
    stack = Stack()
    actions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }

    for element in expression:
        if element in '+-*/':
            last_digit = stack.pop()
            before_last_digit = stack.pop()
            stack.append(
                actions[element](before_last_digit, last_digit)
            )
            continue
        try:
            stack.append(int(element))
        except ValueError as error:
            raise ValueError(f'Unexpected element "{element}".') from error

    return stack.pop()


if __name__ == '__main__':
    print(
        calculate_reverse_polish_notation(input().split(' '))
    )
