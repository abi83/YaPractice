# success try: 49009276, 11 мрт 2021, 18:19:27, 96ms, 4.00Mb


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
            raise KeyError(
                f'The {self} deque\'s maximum size of'
                f'{self._max_size} is exceeded')

        self._tail_index = (self._tail_index + 1) % self._max_size
        self._data[self._tail_index] = value
        self._size += 1

    def push_front(self, value: int) -> None:
        if self._size == self._max_size:
            raise KeyError(
                f'The {self} deque\'s maximum size of'
                f'{self._max_size} is exceeded')

        self._head_index = (self._head_index - 1) % self._max_size
        self._data[self._head_index] = value
        self._size += 1

    def pop_back(self) -> None:
        if self._size == 0:
            raise KeyError(f'The {self} deque\' is empty')

        index_to_pop = self._tail_index
        self._size -= 1
        self._tail_index = (self._tail_index - 1) % self._max_size
        return self._data[index_to_pop]

    def pop_front(self) -> None:
        if self._size == 0:
            raise KeyError(f'The {self} deque\' is empty')

        index_to_pop = self._head_index
        self._size -= 1
        self._head_index = (self._head_index + 1) % self._max_size
        return self._data[index_to_pop]


if __name__ == '__main__':
    commands_count = int(input())
    stack_size = int(input())
    deque = Deque(stack_size)

    for i in range(commands_count):
        line = input().split()
        command = line[0]
        parameter = int(line[1]) if len(line) > 1 else None
        try:
            if parameter is not None:
                getattr(deque, command)(parameter)
            else:
                print(getattr(deque, command)())
        except KeyError:
            print('error')
