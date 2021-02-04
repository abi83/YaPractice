"""
Младший брат Аллы Вася делает тест по математике: вычисляет значение функций в
различных точках. Стоит отличная погода, и друзья зовут Васю гулять. Но мама
разрешила мальчику пойти на улицу только после того, как он закончит тест.
К сожалению, Вася пока не умеет программировать. Зато Алла умеет. Она решила
помочь брату и написала код функции y = ax2 + bx + c. Повторите успех Аллы.
Напишите программу, которая будет по коэффициентам a, b, c и числу x выводить
значение функции в точке x.
"""


def main():
    input_data = input().strip()
    a, x, b, c = input_data.split()
    a, x, b, c = int(a), int(x), int(b), int(c)
    y = a * x ** 2 + b * x + c
    print(y)


if __name__ == '__main__':
    main()
