"""
Далее Тимофею нужно написать класс MyQueueSized, который принимает параметр
max_size, означающий максимально допустимое количество элементов в очереди.
"""


class MyQueueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self._size = 0
        self.data = [None] * max_size

    def push(self, x):
        if self._size < self.max_size:
            self.data[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self._size += 1
        else:
            print('error')

    def pop(self):
        if self._size > 0:
            print(self.data[self.head])
            self.data[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self._size -= 1
        else:
            print('None')

    def peek(self):
        if self._size > 0:
            print(self.data[self.head])
        else:
            print('None')

    def size(self) -> int:
        print(self._size)


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        max_size = int(file.readline())
        m = MyQueueSized(max_size)
        for i in range(n):
            line = file.readline().strip()
            try:
                command, parameter = line.split()
                parameter = int(parameter)
            except ValueError:
                command = line
                parameter = None
            if parameter is not None:
                getattr(m, command)(parameter)
            else:
                getattr(m, command)()
