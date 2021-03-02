# success try: 49053795, 2 мрт 2021, 15:59:17, 55ms, 3.98Mb

from collections.abc import Iterable


class Stack:
    """
    Extremely simple stack class with pop and append methods
    """
    def __init__(self):
        self.data = []

    def __repr__(self):
        return f'Stack obj. with {len(self.data)} elements'

    def append(self, element):
        self.data.append(element)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError as empty_data:
            raise IndexError(
                f'Cannot pop() from {self}. It is empty') from empty_data


def calculate_reverse_polish_notation(
        expression: Iterable,
        stack=Stack(),
        actions=None,
        element_validator=int,
) -> int:
    """
    Input: A 'reverse polish notation' iterable with numbers and
        operations symbols [+,-,*,/]. Example: [7, 2, '+', 4, '*', 2, '+']'
    Output: Calculated value or last calculated value in stack,
        if not enough operation symbols provided
    """
    if actions is None:
        actions = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y,
        }
    for element in expression:
        if element in actions.keys():
            last_digit = stack.pop()
            before_last_digit = stack.pop()
            stack.append(
                actions[element](before_last_digit, last_digit)
            )
            continue
        try:
            stack.append(element_validator(element))
        except ValueError as error:
            raise ValueError(f'Unexpected element "{element}".') from error

    return stack.pop()


if __name__ == '__main__':
    print(
        calculate_reverse_polish_notation(input().split(' '))
    )
