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


# Протестируйте методы programmer_define() и age_define() класса Contact.
# Тестировать нужно все состояния: метод programmer_define() должен по очереди
# принять False и True, а в age_define() должны быть проверены все возрастные
# категории.


test_values = {
    ('Testman', 1945, True): ['Старейшина', 'Программист'],
    ('Testman', 1979, True): ['Олдскул', 'Программист'],
    ('Testman', 1980, True): ['Молодой', 'Программист'],
    ('Testman', 1981, True): ['Молодой', 'Программист'],
    ('Testman', 1945, False): ['Старейшина', 'Нормальный'],
    ('Testman', 1979, False): ['Олдскул', 'Нормальный'],
    ('Testman', 1980, False): ['Молодой', 'Нормальный'],
    ('Testman', 1981, False): ['Молодой', 'Нормальный'],
}

for key in test_values:
    loop_man = Contact(*key)

    test_methods = [
        loop_man.age_define,
        loop_man.programmer_define,
    ]
    print('Testing', loop_man.show_contact(), 'OK!')

    for i in range(len(test_methods)):
        print('    Testing', test_methods[i].__name__, 'OK!')
        assert test_methods[i]() == test_values[key][i], f'Method {i} is down'
