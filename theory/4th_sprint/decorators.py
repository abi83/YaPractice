from datetime import datetime


def timeit(func):
    """A decorator to measure time of running"""
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper


@timeit
def one(n):
    lm = []
    for i in range(10 ** n):
        if i % 2 == 0:
            lm.append(i ** 5)
    return lm


@timeit
def two(n):
    lm = [x ** 5 for x in range(10 ** n) if x % 2 == 0]
    return lm


def cache_args(func):
    """A cache decorator"""
    _cache = {}

    def added_features(*args, **kwargs):
        if args in _cache.keys():
            result = _cache[args]
        else:
            result = func(*args, **kwargs)
            _cache[args] = result
        return result

    return added_features


@cache_args
def long_heavy(num):
    print(f"Долго и сложно {num}")
    return num ** num


print(long_heavy(1))
# Долго и сложно 1
# 1
print(long_heavy(1))
# 1
print(long_heavy(2))
# Долго и сложно 2
# 4
print(long_heavy(2))
# 4
print(long_heavy(2))
# 4


# Напишите декоратор, оптимизирующий работу декорируемой функции. Декоратор
# должен сохранять результат работы функции на ближайшие 3 запуска и вместо
# выполнения функции возвращать сохранённый результат.

def cache3(func):
    """A 3_time_cache decorator"""
    _counts = {'counter': 0}

    def added_features(*args, **kwargs):
        if _counts['counter'] == 0:
            result = _counts['result'] = func(*args, **kwargs)
            _counts['counter'] += 1
        elif _counts['counter'] <3:
            result = _counts['result']
            _counts['counter'] += 1
        elif _counts['counter'] == 3:
            result = _counts['result'] = func(*args, **kwargs)
            _counts['counter'] = 0

        return result

    return added_features


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1
