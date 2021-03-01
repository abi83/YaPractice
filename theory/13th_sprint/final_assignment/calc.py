def calculate_reverse_polish_notation(rpn_string: str) -> int:
    """
    Input: A 'reverse polish notation' string with numbers and
        operations symbols [+,-,*,/] separated by space.
        Example: '7 2 + 4 * 2 +'
    Output: Calculated value or last calculated value in stack,
        if not enough operation symbols provided
    """
    rpn_array = rpn_string.split()
    stack = []
    actions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }

    for element in rpn_array:
        if element in '+-*/':
            last_digit = stack[-1]
            before_last_digit = stack[-2]
            stack = stack[:-2]
            stack.append(
                actions[element](before_last_digit, last_digit)
            )
            continue
        try:
            stack.append(int(element))
        except ValueError as error:
            raise ValueError(f'Unexpected element {element}.') from error

    return stack[-1]


if __name__ == '__main__':
    print(
        calculate_reverse_polish_notation(input())
    )
