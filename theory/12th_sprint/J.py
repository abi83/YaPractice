"""
Разложите число на простые множители.
"""

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
    return primes

@timeit
def main():
    with open('input.txt') as file:
        num = int(file.read().strip())
        primes = get_least_primes_linear(int(num**1/2)+1)
        primes.append(num)
        i = 0
        while i < len(primes):
            if num % primes[i] == 0:
                num = num / primes[i]
                yield primes[i]
            else:
                i += 1


if __name__ == '__main__':
    for element in main():
        print(element, end=' ')
