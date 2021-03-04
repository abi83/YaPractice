"""
bracket sequence generator
"""


# def bracket_sequence_generator(n: int):
#     if n == 0:
#         return ''
#     if n == 1:
#         return '()'
#
#     return ( ' ' +
#             '(' + bracket_sequence_generator(n-1) + ')'
#             + bracket_sequence_generator(n - 2) + bracket_sequence_generator(n - 1)
#             + bracket_sequence_generator(n - 1) + bracket_sequence_generator(n - 2)
#     )
#
#
#
# if __name__ == '__main__':
#     a = 3
#     print(bracket_sequence_generator(a))

n = int(input())
parentheses = []
left = n
right = n
index = 0
str_ = ''


def parenthesis_generator(parentheses: list, left, right, str_two, index):
    if left < 0 or right < left:
        return None
    if left == 0 and right == 0:
        parentheses.append(str_two)
    else:
        if left > 0:
            str_two += '('
            parenthesis_generator(parentheses, left - 1, right, str_two, index + 1)
        if right > left:
            str_two += ')'
            parenthesis_generator(parentheses, left, right - 1, str_two, index + 1)
    return parentheses


print(parenthesis_generator(parentheses, left, right, str_, index))