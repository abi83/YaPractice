def is_correct_bracket_seq(string: str) -> bool:
    """
    >>> is_correct_bracket_seq('{}()[]')
    True
    >>> is_correct_bracket_seq('{}}')
    False
    >>> is_correct_bracket_seq(')(')
    False
    >>> is_correct_bracket_seq('([)]')
    False
    >>> is_correct_bracket_seq('()-')
    Traceback (most recent call last):
        ...
    KeyError: ' "-" is not accepted '
    """

    unclosed_brackets_stack = ''
    pairs_to_close = {
        '}': '{',
        ')': '(',
        ']': '[',
    }

    for symbol in string:
        if symbol in '([{':
            unclosed_brackets_stack += symbol
        if (symbol in '}])'
                and unclosed_brackets_stack[-1] == pairs_to_close[symbol]):
            unclosed_brackets_stack = unclosed_brackets_stack[:-1]

    return not bool(unclosed_brackets_stack)


with open('input.txt') as file:
    bracket_string = file.readline().strip()

print(is_correct_bracket_seq(bracket_string))

