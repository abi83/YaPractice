"""
написать программу, которая определяет, будет ли
положительное целое число степенью четверки.
"""


def main():
    with open('input.txt') as file:
        a = int(file.read().strip())
        if a == 1:
            return True
        num = 4
        while num <= a:
            if num == a:
                return True
            num *= 4
        return False


if __name__ == '__main__':
    print(main())
