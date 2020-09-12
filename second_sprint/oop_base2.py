class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday # добавьте свойство birthday
        print(f"Создаём новый контакт {name}")


# здесь создайте объекты mike и vlad
mike = Contact(
    'Михаил Булгаков',
    '2-03-27',
    'Россия, Москва, Большая Пироговская, дом 35б, кв. 6',
    '15.05.1891',
)

vlad = Contact(
    'Владимир Маяковский',
    '73-88',
    'Россия, Москва, Лубянский проезд, д. 3, кв. 12',
    '19.07.1893',
)


def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")


# здесь измените адрес для объекта mike
mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
# здесь измените телефон для объекта mike
mike.phone = 'К-058-67'

# здесь измените адрес для объекта vlad
vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
# здесь измените телефон для объекта vlad
vlad.phone = '2-35-71'

print_contact()  # выводим данные на экран
