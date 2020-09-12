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

# здесь вызовите функцию print_contact(),
# и она напечатает на экране данные контактов mike и vlad

print_contact()
