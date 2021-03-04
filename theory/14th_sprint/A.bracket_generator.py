"""
Bracket sequence generator
"""


def bracket_seq_generator(
        bracket_sequence_array: list,
        left, right, seq_candidate):
    if left == 0 and right == 0:
        bracket_sequence_array.append(seq_candidate)
    else:
        if left > 0:
            bracket_seq_generator(
                bracket_sequence_array,
                left - 1, right, seq_candidate + '(')
        if right > left:
            bracket_seq_generator(
                bracket_sequence_array,
                left, right - 1, seq_candidate + ')')
    return bracket_sequence_array


if __name__ == '__main__':
    n = int(input())
    print(*bracket_seq_generator([], n, n, ''), sep='\n')
