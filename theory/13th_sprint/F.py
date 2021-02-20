"""
Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс должен поддерживать операции
push, pop и get_max.
"""


class StackMax:
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def push(self, x):
        self.data.append(int(x))

    def pop(self):
        try:
            self.data.pop()
        except IndexError:
            print('error')

    def get_max(self):
        if self.data:
            print(max(self.data))
        else:
            print('None')


if __name__ == '__main__':
    s = StackMax()
    with open('input.txt') as file:
        n = int(file.readline())
        for i in range(n):
            line = file.readline().strip()
            try:
                command, parameter = line.split()
            except ValueError:
                command = line
                parameter = None
            if parameter:
                getattr(s, command)(parameter)
            else:
                getattr(s, command)()
