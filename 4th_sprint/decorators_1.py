import math as m
from datetime import datetime


def timeit(func):
    """A decorator to measure time of running"""

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper  # returning a function, not a value


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
@timeit
def heavy_function(n):
    for i in range(n**n):
        result = m.tan(n)
        result = result**n
        result = m.sin(result)
        result = m.exp(result)
        result = m.sqrt(result)
        result = m.sqrt(result)
        if i % 10**(n-3) == 0:
            print(i)
    return result


if __name__ == '__main__':
    print('heavy_function result: ', heavy_function(7))

    print('heavy_function result: ', heavy_function(6))

    print('heavy_function result: ', heavy_function(7))
