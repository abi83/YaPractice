# import array


class Deque:
    """
    Classic Deque example: with fix sized array
    Value of item is in range -1000...0...1000
    -32768, the smallest value allowed by 'h' arrays means that value is empty
    head and tail indexes is None if Deque is empty
    head_index == tail_index if array is from one element
    """
    def __init__(self, max_size):
        # self.data = array.array['h', [-32768]*max_size]
        self.data = [None] * max_size  # TODO: getter and setter
        self._max_size = max_size
        self._size = 0
        self.head_index = None  # TODO: getters and setters
        self.tail_index = None  # TODO: getters and setters

    def __repr__(self):
        return f'Deque obj. Size: {self.size} of {self.max_size}'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if 0 <= value <= self.max_size:
            self._size = value
        else:
            raise ValueError(
                f'Value {value} is not in (0...{self.max_size})')

    @property
    def max_size(self):
        return self._max_size

    def push_back(self, value):
        if self.size >= self.max_size:
            print('error')
            return

        if self.size > 0:
            self.data[(self.tail_index + 1) % self.max_size] = value
            self.tail_index = (self.tail_index + 1) % self.max_size
            self.size += 1
        else:
            self.data[0] = value
            self.head_index = 0
            self.tail_index = 0
            self.size = 1

    def push_front(self, value):  # done
        if self.size >= self.max_size:
            print('error')
            return

        if self.size > 0:
            self.data[(self.head_index - 1) % self.max_size] = value
            self.head_index = (self.head_index - 1) % self.max_size
            self.size += 1
        else:
            self.data[0] = value
            self.head_index = 0
            self.tail_index = 0
            self.size = 1


    def pop_back(self):
        if self.size > 0:
            print(self.data[self.tail_index])
            self.data[self.tail_index] = None  # TODO: it is unnecessary
            self.tail_index = (self.tail_index - 1) % self.max_size
            self.size -= 1
        else:
            print('error')

    def pop_front(self):  # done
        if self.size > 0:
            print(self.data[self.head_index])
            self.data[self.head_index] = None  # TODO: it is unnecessary
            self.head_index = (self.head_index + 1) % self.max_size
            self.size -= 1
        else:
            print('error')


if __name__ == '__main__':
    with open('input.txt') as file:
        commands_count = int(file.readline().strip())
        stack_size = int(file.readline().strip())
        deque = Deque(stack_size)
        for i in range(commands_count):
            line = file.readline().strip().split()
            command = line[0]
            parameter = int(line[1]) if len(line) >= 2 else None
            if parameter is not None:
                getattr(deque, command)(parameter)
            else:
                getattr(deque, command)()
