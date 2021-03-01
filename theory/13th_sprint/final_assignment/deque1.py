import array


class Deque:
    """
    Minimalistic Deque implementation with fix sized array.
    Methods provided:
        .push_back(value)
        .push_front(value)
        .pop_front()
        .pop_back()
    Value: Signed short int, abs(value) < 32767
    head_index, tail_index are indexes of first and last elements in array.
    head_index == tail_index if array is empty or contains one element only
    """
    def __init__(self, max_size):
        self._data = array.array('h', [0]*max_size)
        self._max_size = max_size
        self._size = 0
        self._head_index = 0
        self._tail_index = -1

    def __repr__(self):
        return f'Deque obj. Size: {self._size} of {self._max_size}'

    def push_back(self, value: int) -> None:
        if self._size == self._max_size:
            raise OverflowError(
                f'The {self} deque\'s maximum size of'
                f'{self._max_size} is exceeded')

        if self._size > 0:
            self._data[(self._tail_index + 1) % self._max_size] = value

            self._tail_index = (self._tail_index + 1) % self._max_size
            self._size += 1
        else:
            self._data[0] = value
            self._head_index = 0
            self._tail_index = 0
            self._size = 1

    def push_front(self, value: int) -> None:
        if self._size == self._max_size:
            raise OverflowError(
                f'The {self} deque\'s maximum size of'
                f'{self._max_size} is exceeded')

        if self._size > 0:
            self._data[(self._head_index - 1) % self._max_size] = value
            self._head_index = (self._head_index - 1) % self._max_size
            self._size += 1
        else:
            self._data[0] = value
            self._head_index = 0
            self._tail_index = 0
            self._size = 1

    def pop_back(self) -> None:
        if self._size == 0:
            print('error')
            return

        print(self._data[self._tail_index])
        self._size -= 1
        if self._size > 0:
            self._tail_index = (self._tail_index - 1) % self._max_size

    def pop_front(self) -> None:
        if self._size == 0:
            print('error')
            return

        print(self._data[self._head_index])
        self._size -= 1
        if self._size > 0:
            self._head_index = (self._head_index + 1) % self._max_size


if __name__ == '__main__':
    # commands_count = int(input())
    # stack_size = int(input())
    # deque = Deque(stack_size)
    #
    # for i in range(commands_count):
    #     line = input().split()
    #     command = line[0]
    #     parameter = int(line[1]) if len(line) > 1 else None
    #     if parameter is not None:
    #         getattr(deque, command)(parameter)
    #     else:
    #         getattr(deque, command)()

    with open('input.txt') as file:
        commands_count = int(file.readline())
        stack_size = int(file.readline())
        deque = Deque(stack_size)

        for i in range(commands_count):
            line = file.readline().strip().split()
            command = line[0]
            parameter = int(line[1]) if len(line) > 1 else None
            if parameter is not None:
                getattr(deque, command)(parameter)
            else:
                getattr(deque, command)()
