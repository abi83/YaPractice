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
def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(2 * num, n + 1, num):
                numbers[j] = False
    return numbers


@timeit
def eratosthenes_effective(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


@timeit
def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


n = 10000000

one = eratosthenes(n)
two = eratosthenes_effective(n)
three = get_least_primes_linear(n)