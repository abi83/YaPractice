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
    # полезный код
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
