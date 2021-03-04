from typing import List


class Deque:
    """
    Minimalistic Deque implementation with fix-sized array.
    Methods provided:
        .push_back(value)
        .push_front(value)
        .pop_front()
        .pop_back()
    head_index, tail_index are indexes of first and last elements in array.
    """
    def __init__(self, max_size):
        self._data = [0] * max_size
        self._max_size = max_size
        self._size = 0
        self._head_index = 0
        self._tail_index = -1

    def __repr__(self):
        return f'Deque obj. (Size: {self._size} of {self._max_size})'

    def push_back(self, value) -> None:
        if self._size == self._max_size:
            raise IndexError(f'The {self} maximum size  is exceeded')
        self._tail_index = (self._tail_index + 1) % self._max_size
        self._data[self._tail_index] = value
        self._size += 1

    def push_front(self, value) -> None:
        if self._size == self._max_size:
            raise IndexError(f'The {self} maximum size  is exceeded')
        self._head_index = (self._head_index - 1) % self._max_size
        self._data[self._head_index] = value
        self._size += 1

    def pop_back(self):
        if self._size == 0:
            raise IndexError(f'The {self} deque is empty')
        index_to_pop = self._tail_index
        self._size -= 1
        self._tail_index = (self._tail_index - 1) % self._max_size
        return self._data[index_to_pop]

    def pop_front(self):
        if self._size == 0:
            raise IndexError(f'The {self} deque is empty')
        index_to_pop = self._head_index
        self._size -= 1
        self._head_index = (self._head_index + 1) % self._max_size
        return self._data[index_to_pop]


def run(command_parameter_list: List[tuple]):
    for command, *parameter in command_parameter_list:
        try:
            method = getattr(deque, command)
        except AttributeError as error:
            raise AttributeError(
                f'Method "{command}" in Deque class not found.') from error
        try:
            if command in ['pop_front', 'pop_back']:
                yield method()
            else:
                method(*parameter)
        except IndexError:
            yield 'error'


if __name__ == '__main__':
    commands_count = int(input())
    deque = Deque(int(input()))
    command_list = []
    for line in range(commands_count):
        command_list.append(tuple(input().split()))
    for result in run(command_list):
        print(result)
