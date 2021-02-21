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
    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item
        self.previous = None

    def __str__(self):
        return self.value


class LinkedQuene:
    def __init__(self, head: Node):
        self._size = 0
        self.head = head
        self.last = head
        pass
    
    def get(self):
        pass

    def put(self, x):
        self.last
        pass
    
    def size(self):
        pass
