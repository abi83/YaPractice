class Contact:
    def __init__(self,
                 name: str,
                 year_birth: int,
                 is_programmer: bool) -> None:
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self) -> str:
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self) -> str:
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self) -> str:
        return(f'{self.name}, '              
               f'возраст: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self) -> None:
        print(self.show_contact())

    def __dir__(self):
        return ['age_define', 'programmer_define']


# Протестируйте методы programmer_define() и age_define() класса Contact.
# Тестировать нужно все состояния: метод programmer_define() должен по очереди
# принять False и True, а в age_define() должны быть проверены все возрастные
# категории.

# первый вариант
test_values = {
    (1945, True): ['Старейшина', 'Программист'],
    (1979, True): ['Олдскул', 'Программист'],
    (1980, True): ['Молодой', 'Программист'],
    (1981, True): ['Молодой', 'Программист'],
    (1945, False): ['Старейшина', 'Нормальный'],
    (1979, False): ['Олдскул', 'Нормальный'],
    (1980, False): ['Молодой', 'Нормальный'],
    (1981, False): ['Молодой', 'Нормальный'],
}

for key in test_values:
    loop_man = Contact('Test Man', *key)

    test_methods = [
        loop_man.age_define,
        loop_man.programmer_define,
    ]

    for i in range(len(test_methods)):
        assert test_methods[i]() == test_values[key][i],\
            f'Method {test_methods[i].__name__} is down'


# второй вариант
test_methods = Contact('friend', 1900, False).__dir__()
# создаем список названий методов класса. Метод __dir__ переопределен
test_values = {
    (1945, True): {'age_define': 'Старейшина', 'programmer_define': 'Программист'},
    (1979, True): {'age_define': 'Олдскул', 'programmer_define': 'Программист'},
    (1980, True): {'age_define': 'Молодой', 'programmer_define': 'Программист'},
    (1981, True): {'age_define': 'Молодой', 'programmer_define': 'Программист'},
    (1945, False): {'age_define': 'Старейшина', 'programmer_define': 'Нормальный'},
    (1979, False): {'age_define': 'Олдскул', 'programmer_define': 'Нормальный'},
    (1980, False): {'age_define': 'Молодой', 'programmer_define': 'Нормальный'},
    (1981, False): {'age_define': 'Молодой', 'programmer_define': 'Нормальный'},
}

for key in test_values:
    loop_man = Contact('Test Man', *key)
    for method in test_methods:
        # вызываем метод по его названию
        assert loop_man.__getattribute__(method)() == test_values[key][method],\
            f'Method {method} is down'
