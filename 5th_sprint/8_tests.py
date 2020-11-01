from typing import Callable


def est_invertor(invertaser) -> None:
    """Тест алогритма инвертирования строки."""

    print(f'{est_invertor.__doc__}')
    print(f'Тестирование алгоритма {invertaser.__name__}')

    source = 'Попугай'
    inversed = 'йагупоП'

    assert invertaser(source) == inversed, (
        f'Алгоритм в {invertaser.__name__} работает неправильно с строкой "{source}" ')

    source = ''
    inversed = ''

    assert invertaser(source) == inversed, (
        f'Алгоритм {invertaser.__name__} работает неправильно с пустой строкой')

    print(f'Тест для {invertaser.__name__} пройден успешно')


# Ниже - несколько функций, инвертирующих строку.
# Их и будем тестировать.
def recursion_invertor(text: str) -> str:
    """Инвертирует строчку рекурсивно."""
    if len(text) == 0:
        return text
    else:
        return recursion_invertor(text[1:]) + text[0]


def slice_invertor(text: str) -> str:
    """Инвертирует строчку срезом."""
    return text[::-1]


def iterator_invertor(text: str) -> str:
    """Инвертирует строчку обратной итерацией."""
    return ''.join(reversed(text))


def reverselist_invertor(text: str) -> str:
    """Инвертирует строчку переворотом списка."""
    inversed_list = list(text)
    inversed_list.reverse()
    return ''.join(inversed_list)


# Вызов тестирующей функции для каждого из инверторов
est_invertor(recursion_invertor)
est_invertor(slice_invertor)
est_invertor(iterator_invertor)
est_invertor(reverselist_invertor)