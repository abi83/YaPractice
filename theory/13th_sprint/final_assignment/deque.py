# success try: 48647321, 71ms 3.97Mb            /with list
# success try: 48668879, 84ms 3.98Mb            /with array

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
        self._tail_index = 0

    def __repr__(self):
        return f'Deque obj. Size: {self.size} of {self.max_size}'

    def _get_element_by_index(self, index: int) -> int:
        """
        Checking if index is between head and tail indexes
        Return: element by index
        Raise: IndexError if index is incorrect
        """
        if index < 0 or index > self.max_size:
            raise IndexError(f'Index must be in (0...{self.max_size}))')
        if self.size == 0:
            raise IndexError(f'There are no elements in Deque')
        if (
            (self.tail_index <= self.head_index
                and self.tail_index <= index <= self.head_index)
            or (self.tail_index >= self.head_index
                and (self.tail_index >= index or index >= self.head_index))
        ):
            return self._data[index]

        raise IndexError(f'There is no element in {index} position')

    def _set_element_by_index(self, index: int, value: int) -> None:
        """
        Checking if index is between head and tail indexes
        Raise:
            IndexError if index is incorrect,
            ValueError if value is too big
        """
        if index < 0 or index > self.max_size:
            raise IndexError(f'Index must be in (0...{self.max_size}))')
        if abs(value) > 32767:
            raise ValueError(
                f'2-bytes integer is used. Restriction: abs(value) < 32768')
        if (
            (self.tail_index <= self.head_index
                and self.tail_index <= index <= self.head_index)
            or (self.tail_index >= self.head_index
                and (self.tail_index >= index or index >= self.head_index))
        ):
            self._data[index] = value

    @property
    def max_size(self) -> int:
        return self._max_size

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value) -> None:
        if 0 <= value <= self.max_size:
            self._size = value
        else:
            raise ValueError(
                f'Value {value} is not in (0...{self.max_size})')

    @property
    def head_index(self) -> int:
        return self._head_index

    @head_index.setter
    def head_index(self, value: int) -> None:
        if 0 <= value <= self.max_size:
            self._head_index = value
        else:
            raise ValueError(f'Head index must be in (0...{self.max_size})')

    @property
    def tail_index(self) -> int:
        return self._tail_index

    @tail_index.setter
    def tail_index(self, value: int) -> None:
        if 0 <= value <= self.max_size:
            self._tail_index = value
        else:
            raise ValueError(f'Tail index must be in (0...{self.max_size})')

    def push_back(self, value: int) -> None:
        if self.size == self.max_size:
            print('error')
            return

        if self.size > 0:
            self._set_element_by_index(
                (self.tail_index + 1) % self.max_size,
                value
            )
            self.tail_index = (self.tail_index + 1) % self.max_size
            self.size += 1
        else:
            self._set_element_by_index(0, value)
            self.head_index = 0
            self.tail_index = 0
            self.size = 1

    def push_front(self, value: int) -> None:
        if self.size == self.max_size:
            print('error')
            return

        if self.size > 0:
            self._set_element_by_index(
                (self.head_index - 1) % self.max_size,
                value
            )
            self.head_index = (self.head_index - 1) % self.max_size
            self.size += 1
        else:
            self._set_element_by_index(0, value)
            self.head_index = 0
            self.tail_index = 0
            self.size = 1

    def pop_back(self) -> None:
        if self.size == 0:
            print('error')
            return

        print(self._get_element_by_index(self.tail_index))
        self.size -= 1
        if self.size > 0:
            self.tail_index = (self.tail_index - 1) % self.max_size

    def pop_front(self) -> None:
        if self.size == 0:
            print('error')
            return

        print(self._get_element_by_index(self.head_index))
        self.size -= 1
        if self.size > 0:
            self.head_index = (self.head_index + 1) % self.max_size


if __name__ == '__main__':
    commands_count = int(input())
    stack_size = int(input())
    deque = Deque(stack_size)
    for i in range(commands_count):
        line = input()
        command = line[0]
        parameter = int(line[1]) if len(line) > 1 else None
        if parameter is not None:
            getattr(deque, command)(parameter)
        else:
            getattr(deque, command)()
