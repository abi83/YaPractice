# success try: 48999073, 1 мрт 2021, 15:15:42, 97ms, 3.96Mb


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


def test_deque():
    test_cases = [
        {'stack_size': 10,
         'commands': [
             ("push_front", -855), ("push_front", 720), ("pop_back", None),
             ("pop_back", None), ("push_back", 844), ("pop_back", None),
             ("push_back", 823),
         ],
         'output': '-855 720 844',
         },
        {'stack_size': 4,
         'commands': [
             ("push_front", 861), ("push_front", -819), ("pop_back", None),
             ("pop_back", None)
         ],
         'output': '861 -819',
         },
        {'stack_size': 7,
         'commands': [
             ("pop_front", None), ("pop_front", None), ("push_front", 741),
             ("push_front", 648), ("pop_front", None), ("pop_back", None),
             ("pop_front", None),
         ],
         'output': 'error error 648 741 error',
         },
    ]

    for case in test_cases:
        deque = Deque(case['stack_size'])
        output = ''
        for command, parameter in case['commands']:
            try:
                if parameter is not None:
                    getattr(deque, command)(parameter)
                else:
                    answer = str(getattr(deque, command)())
                    output += answer if not output else ' ' + answer
            except KeyError:
                output += 'error' if not output else ' error'
        assert case['output'] == output, 'bla bla'


if __name__ == '__main__':
    test_deque()
    # commands_count = int(input())
    # stack_size = int(input())
    # deque = Deque(stack_size)
    #
    # for i in range(commands_count):
    #     line = input().split()
    #     command = line[0]
    #     parameter = int(line[1]) if len(line) > 1 else None
    #     try:
    #         if parameter is not None:
    #             getattr(deque, command)(parameter)
    #         else:
    #             print(getattr(deque, command)())
    #     except KeyError:
    #         print('error')

    with open('input.txt') as file:
        commands_count = int(file.readline())
        stack_size = int(file.readline())
        deque = Deque(stack_size)

        for i in range(commands_count):
            line = file.readline().strip().split()
            command = line[0]
            parameter = int(line[1]) if len(line) > 1 else None
            # breakpoint()
            try:
                if parameter is not None:
                    getattr(deque, command)(parameter)
                else:
                    print(getattr(deque, command)())
            except KeyError:
                print('error')
