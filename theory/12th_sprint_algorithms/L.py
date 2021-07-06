"""
 Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена
 перемешиванием букв строки s и добавлением 1 буквы в случайную позицию.
 Нужно найти добавленную букву.
"""

def main():
    with open('input.txt') as file:
        data = file.read().strip().split('\n')
        s1 = data[0]
        s2 = data[1]

        s1_dict = {element: 0 for element in s1}
        s2_dict = {element: 0 for element in s2}

        for s1_index, s2_index in zip(s1, s2):
            s1_dict[s1_index] += 1
            s2_dict[s2_index] += 1

        s2_dict[s2[-1]] += 1

        for key in s2_dict:
            try:
                if s1_dict[key] != s2_dict[key]:
                    return key
            except KeyError:
                return key


if __name__ == '__main__':
    print(main())
