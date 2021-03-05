keyboard = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


def nokia_text(digits, pre_str='', combination=[]):
    try:
        digit = digits[0]
    except IndexError:
        digit = None
        combination.append(pre_str)

    for symbol in keyboard.get(digit) or []:
        nokia_text(digits[1:], pre_str + symbol, combination)
    return combination


if __name__ == '__main__':
    st = input()

    print(*nokia_text([int(x) for x in st]))
