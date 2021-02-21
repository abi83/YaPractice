"""
Любимый вариант очереди Тимофея — очередь, написанная с использованием связного
списка. Помогите ему с реализацией. Очередь должна поддерживать выполнение
трёх команд:

get — вывести элемент в голове очереди и удалить его. Если очередь пуста,
то вывести «error».
put x — добавить число x в очередь
size — вывести текущий размер очереди
"""


class Node:
    def __init__(self, value, next_item=None, previous=None):
        self.value = value
        self.next = next_item
        self.previous = previous

    def __str__(self):
        return self.value


class LinkedQuene:
    def __init__(self, head: Node = None):
        self.data = []
        self._size = 0
        self.head = head
        self.last = head
        pass

    def get(self):
        if self.data:
            print(self.head.value)
            self.head = self.head.next
            self.data.pop(0)
            self._size -= 1
        else:
            print('error')
        pass

    def put(self, x):
        current_last = self.last
        new_last = Node(x, previous=current_last)
        self.data.append(new_last)
        if not self.head:
            self.head = self.data[0]
        self._size += 1
        try:
            current_last.next = new_last
        except AttributeError:
            pass
        self.last = new_last

    def size(self):
        print(self._size)


if __name__ == '__main__':
    linked_quene = LinkedQuene()
    with open('input.txt') as file:
        n = int(file.readline().strip())
        for i in range(n):
            line = file.readline().strip()
            try:
                command, parameter = line.split()
                parameter = int(parameter)
            except ValueError:
                command = line
                parameter = None
            if parameter is not None:
                getattr(linked_quene, command)(parameter)
            else:
                getattr(linked_quene, command)()
