from typing import Dict


def movie_quotes(name: str) -> str:
    """Возвращает цитаты известных персонажей из фильмов

    >>> movie_quotes('Элли')
    'Тото, у меня такое ощущение, что мы не в Канзасе!'

    >>> movie_quotes('Шерлок')
    'Элементарно, Ватсон!'

    >>> movie_quotes('Дарт Вейдер')
    'Я — твой отец.'

    >>> movie_quotes('Леонид Тощев')
    'Персонаж пока не известен миллионам.'
    """
    quotes: Dict[str, str] = {
        'Элли': 'Тото, у меня такое ощущение, что мы не в Канзасе!',
        'Шерлок': 'Элементарно, Ватсон!',
        'Дарт Вейдер': 'Я — твой отец.',
        'Thomas A. Anderson': 'Меня. Зовут. Нео!',
    }
    # Метод словаря get() возвращает значение для указанного ключа.
    # Если запрошенный ключ не найден — get() вернёт значение,
    # указанное вторым аргументом.
    return quotes.get(name, 'Персонаж пока не известен миллионам.')


persons = [
    'Элли',
    'Шерлок',
    'Дарт Вейдер',
    'Чувак',
    'Thomas A. Anderson',
]

for person in persons:
    print(movie_quotes(person))
