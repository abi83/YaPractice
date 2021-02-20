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

    unclosed_brackets = ''
    paares_to_close = {
        '}': '{',
        ')': '(',
        ']': '[',
    }

    for symbol in string:
        unclosed_brackets += symbol

        if (
                symbol in '}])'
            and unclosed_brackets[-2:] == paares_to_close[symbol] + symbol):
            unclosed_brackets = unclosed_brackets[:-2]

    return not bool(unclosed_brackets)


with open('input.txt') as file:
    bracket_string = file.readline().strip()

print(is_correct_bracket_seq(bracket_string))

