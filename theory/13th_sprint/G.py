"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None. При этом push и pop также
должны выполняться за константное время.
"""


class StackMaxEffective:
    def __init__(self):
        self.data = []

    def push(self, x):
        try:
            previous_max = self.data[-1][1]
            self.data.append(
                (x, max(x, previous_max))
            )
        except IndexError:
            self.data.append(
                (x, x)
            )

    def pop(self):
        try:
            self.data.pop()
        except IndexError:
            print('error')

    def get_max(self):
        if self.data:
            print(self.data[-1][1])
        else:
            print('None')


if __name__ == '__main__':
    s = StackMaxEffective()
    with open('input.txt') as file:
        n = int(file.readline())
        for i in range(n):
            line = file.readline().strip()
            try:
                command, parameter = line.split()
                parameter = int(parameter)
            except ValueError:
                command = line
                parameter = None
            breakpoint()
            if parameter is not None:
                getattr(s, command)(parameter)
            else:
                getattr(s, command)()
