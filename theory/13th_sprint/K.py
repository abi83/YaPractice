"""
Числа фибоначи f(0) = 1, f(1) = 1, f(2) = 2, f(i) = f(i-1) + f(i-2)
"""


def f(n):
    if n in [0, 1]:
        return 1
    return f(n-1) + f(n-2)


if __name__ == '__main__':
    n = int(input())
    print(f(n))