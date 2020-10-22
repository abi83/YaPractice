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
    (1945, True): [['simple_name', 1945, True], ['Старейшина', 'Программист']],
    (1979, True): [['simple_name', 1979, True], ['Олдскул', 'Программист']],
    (1980, True): [['simple_name', 1980, True], ['Молодой', 'Программист']],
    (1981, True): [['simple_name', 1981, True], ['Молодой', 'Программист']],
    (1945, False): [['simple_name', 1945, False], ['Старейшина', 'Нормальный']],
    (1979, False): [['simple_name', 1979, False], ['Олдскул', 'Нормальный']],
    (1980, False): [['simple_name', 1980, False], ['Молодой', 'Нормальный']],
    (1981, False): [['simple_name', 1981, False], ['Молодой', 'Нормальный']],
}

test_base = []

for key in test_values:
    loop_man = Contact(*test_values[key][0])
    assert loop_man.age_define() == test_values[key][1][0], 'Жопа с age_define'
    assert loop_man.programmer_define() == test_values[key][1][1], 'Жопа с programmer_define'
    print('=====', loop_man.show_contact(),'=====')

