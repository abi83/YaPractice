"""
Найти самое длинное слово в строке
"""


def main():
    with open('input.txt') as file:
        data = file.read().strip().split('\n')
        m = int(data[0])
        words = data[1].split(' ')

        max_len, max_word = 0, ''
        for word in words:
            if len(word) > max_len:
                max_word = word
                max_len = len(word)

        print(max_word)
        print(max_len)


if __name__ == '__main__':
    main()
