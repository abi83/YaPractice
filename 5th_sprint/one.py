def we_crush_all(name: str) -> str:
    return 'Привет, ' + name + ', мы всё сломали!'


print(we_crush_all('Наташа'))
# print(we_crush_all(100))


from typing import Optional

# Переменная text ожидает данные типа str или None
text: Optional[str]

# Эксперимент: в переменную с типом "строка"...
var: str
# ...передадим None:
var = None
# Анализатор кода сообщит об ошибке:
# Incompatible types in assignment
# (expression has type "None", variable has type "str")

# А переменная text аннотирована через Optional, и если передать в неё None...
text = None
# ...проблем не будет.

from typing import Union

# Аргумент x может принимать целое число или строку


def hundreds(x: Union[int, str]) -> str:
    return str(x * 100)


print(hundreds(100))
print(hundreds('сто'))



from typing import Any

x: Any
x = 12210
x = 'Строка'
x = True
x = None
# Можно всё! Переменная x примет любой тип данных. 



