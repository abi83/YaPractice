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
    """

    unclosed_brackets_stack = ''
    pairs_to_close = {
        '}': '{',
        ')': '(',
        ']': '[',
    }

    for symbol in string:
        if (symbol in '([{'
                or not unclosed_brackets_stack):
            unclosed_brackets_stack += symbol
        if (symbol in '}])'
                and unclosed_brackets_stack[-1] == pairs_to_close[symbol]):
            unclosed_brackets_stack = unclosed_brackets_stack[:-1]

    return unclosed_brackets_stack == ''


if __name__ == '__main__':
    import doctest
    doctest.testmod()
